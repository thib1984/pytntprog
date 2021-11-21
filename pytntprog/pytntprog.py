"""
pytntprog use case
"""

import argparse
import sys
import requests
import urllib.request
import xml.etree.ElementTree as ET
import os
import time
from pytntprog.args import compute_args
import datetime
import colorama
from termcolor import colored
from columnar import columnar
from pathlib import Path


DOSSIER_CONFIG_PYTNTPROG = "pytntprog"

def find():
    alll = compute_args().all
    idd = compute_args().id
    ffilter = compute_args().filter
    ccurrent = compute_args().current
    nocolor = compute_args().nocolor

    colorama.init()


    xml_tnt = "tnt.xml"
    if (
        compute_args().cache
        or not os.path.exists(
            get_user_config_directory_pytntprog() + xml_tnt
        )
        or (
            time.time()
            - os.stat(
                get_user_config_directory_pytntprog() + xml_tnt
            ).st_mtime
            > 86400 * 30
        )
    ):
        url = "https://xmltv.ch/xmltv/xmltv-tnt.xml"
        print("download the distant xml file...")
        urllib.request.urlretrieve(
            url, get_user_config_directory_pytntprog() + xml_tnt
        )
        print("download is finished")

    

    tree = ET.parse(get_user_config_directory_pytntprog() + xml_tnt)
    root = tree.getroot()
    T = []
    i = 1
    for neighbor in root.iter("programme"):
        start = neighbor.get("start")
        stop = neighbor.get("stop")
        channel = neighbor.get("channel")
        for c in root.iter("channel"):
            if c.get("id") == channel:
                channel = c.find("display-name").text
                break
        title = neighbor.find("title").text
        subtitle = ""
        if neighbor.find("sub-title") != None:
            subtitle = neighbor.find("sub-title").text
        desc = ""
        if neighbor.find("desc") != None:
            desc = neighbor.find("desc").text
        category = ""
        if neighbor.find("category") != None:
            category = neighbor.find("category").text
        date = ""
        if neighbor.find("date") != None:
            date = neighbor.find("date").text
        episode = ""
        if neighbor.find("episode-num") != None:
            episode = neighbor.find("episode-num").text
        age = ""
        if neighbor.find("rating") != None:
            age = neighbor.find("rating").find("value").text
        T.append(
            {
                "time": start,
                "time_end": stop,
                "day": start[0:8],
                "start": start[8:10] + ":" + start[10:12],
                "end": stop[8:10] + ":" + stop[10:12],
                "channel": channel,
                "title": title,
                "id": str(i).zfill(5),
                "subtitle": subtitle,
                "description": desc,
                "category": category,
                "age": age,
                "episode": episode,
                "date": date,
            }
        )

        i = i + 1
    T.sort(key=lambda x: x["time"])

    if idd:
        for w in T:
            if w["id"] == idd.zfill(5):
                print(
                    "titre       : "
                    + w["title"]
                    + " "
                    + w["subtitle"]
                )
                print("chaine      : " + w["channel"])
                print("jour        : " + w["day"])
                print("heure debut : " + w["start"])
                print("heure fin   : " + w["end"])
                print("resume      : " + w["description"])
                print("episode     : " + w["episode"])
                print("date        : " + w["date"])
                print("categorie   : " + w["category"])
                print("age         : " + w["age"])
                break
    else:
        if alll:
            headers = ["id", "jour", "heure", "chaine", "programmes"]
        else:
            headers = ["id", "heure", "chaine", "programmes"]
        data = []
        for w in T:

            if alll:
                resume = [
                    my_colored("[" + w["id"] + "] ", "red", nocolor),
                    w["day"],
                    my_colored(w["start"], "green", nocolor),
                    my_colored(w["channel"], "yellow", nocolor),
                    my_colored(
                        w["title"] + " " + w["subtitle"],
                        "cyan",
                        nocolor,
                    ),
                ]

            else:
                resume = [
                    my_colored("[" + w["id"] + "] ", "red", nocolor),
                    my_colored(w["start"], "green", nocolor),
                    my_colored(w["channel"], "yellow", nocolor),
                    my_colored(
                        w["title"] + " " + w["subtitle"],
                        "cyan",
                        nocolor,
                    ),
                ]

            trouve = False

            if not ffilter:
                trouve = True
            else:
                trouve = True
                for search in ffilter:
                    if search.lower() not in " ".join(resume).lower():
                        trouve = False
                        break

            if ccurrent:
                until = (
                    datetime.datetime(
                        int(w["time"][0:4]),
                        int(w["time"][4:6]),
                        int(w["time"][6:8]),
                        int(w["time"][8:10]),
                        int(w["time"][10:12]),
                        0,
                    ).timestamp()
                    - time.time()
                )
                since = (
                    datetime.datetime(
                        int(w["time_end"][0:4]),
                        int(w["time_end"][4:6]),
                        int(w["time_end"][6:8]),
                        int(w["time_end"][8:10]),
                        int(w["time_end"][10:12]),
                        0,
                    ).timestamp()
                    - time.time()
                )
                if (until > 3600) or (since < 0):
                    trouve = False
                if until > 3600:
                    break
            if alll:
                if trouve:
                    data.append(resume)
            else:
                if (
                    w["day"]
                    == datetime.date.today().strftime("%Y%m%d")
                    and trouve
                ): 
                    data.append(resume)
                if w["day"] > datetime.date.today().strftime(
                    "%Y%m%d"
                ):
                    break
        if data != []:        
            table = columnar(data, headers, no_borders=True, wrap_max=0)
            print(table)
        else:
            print(my_colored("attention : aucun résultat", "yellow", nocolor))  


def my_colored(message, color, nocolor):
    if nocolor:
        return message
    return colored(message, color)

def get_user_config_directory_pytntprog():
    nocolor = compute_args().nocolor
    if os.name == "nt":
        appdata = os.getenv("LOCALAPPDATA")
        if appdata:
            ze_path = os.path.join(
                appdata, DOSSIER_CONFIG_PYTNTPROG, ""
            )
            Path(ze_path).mkdir(parents=True, exist_ok=True)
            return ze_path
        appdata = os.getenv("APPDATA")
        if appdata:
            ze_path = os.path.join(
                appdata, DOSSIER_CONFIG_PYTNTPROG, ""
            )
            Path(ze_path).mkdir(parents=True, exist_ok=True)
            return ze_path
        print(
            my_colored(
                "erreur : impossible de créer le dossier de config",
                "red",nocolor
            )
        )
        sys.exit(1)
    xdg_config_home = os.getenv("XDG_CONFIG_HOME")
    if xdg_config_home:
        ze_path = os.path.join(xdg_config_home, "")
        Path(ze_path).mkdir(parents=True, exist_ok=True)
        return ze_path
    ze_path = os.path.join(
        os.path.expanduser("~"),
        ".config",
        DOSSIER_CONFIG_PYTNTPROG,
        "",
    )
    Path(ze_path).mkdir(parents=True, exist_ok=True)
    return ze_path    
