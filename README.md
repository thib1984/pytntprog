# :tv: pytntprog

pytntprog displays the program of tnt tv in France


# 💫 demo

![demo](https://user-images.githubusercontent.com/45128847/137587565-c2dc81ef-95ca-4312-89ae-e9085ac964c7.gif)
# How install **pytntprog**

``pip3 install pytntprog``
or
``pip install pytntprog``

# 🚀 How use **pytntprog**

- ``pytntprog`` display the tnt programm for the current day with id index
- ``pytntprog -i [id]`` display the details of the programm with id
- ``pytntprog -c`` display current programm
- ``pytntprog -a`` display all tnt programm (current day by default)
- ``pytntprog -f "TF1"`` display the tnt programm for the current day with filter TF1
- ``pytntprog -f "Stade 2" "France 3"`` display the tnt programm for the current day with filter Stade 2 + France 3
- ``pytntprog -n`` or ``pytntprog --no-chache`` download the distant xml file event if the cache is not finished (24h by default)
- ``pytntprog -u`` to update pytntprog

# :package: Changelog

## 0.4.0

- Increase performance and time response
