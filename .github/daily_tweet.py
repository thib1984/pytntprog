from twython import Twython
import os

# get emails and password from environment variables
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

message = "Programme #TNT du soir. Image obtenue depuis l'outil #pytntprog. Source data : https://xmltv.ch "
image = open('export.png', 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]

twitter.update_status(status=message, media_ids=media_id)

print("Tweeted: %s" % message)