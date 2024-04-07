import subprocess
from random import choice
import os

DIRECTORY = "C:\\Users\\aadis\\OneDrive\\Pictures\\collection\\"
COMMAND = "C:\\Users\\aadis\\lively-commandline\\lively_command_utility\\Livelycu.exe setwp --file "


files = [os.path.join(DIRECTORY, f) for f in os.listdir("C:\\Users\\aadis\\OneDrive\\Pictures\\collection\\") if os.path.isfile(os.path.join(DIRECTORY, f))]
#pprint(len(files))
random_wallpaper = choice(files)
subprocess.run(COMMAND + random_wallpaper)
exit(0)