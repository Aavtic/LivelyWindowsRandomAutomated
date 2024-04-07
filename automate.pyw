import subprocess
from random import choice
import os

# Specify the directory of your live wallpaper collection
DIRECTORY = "C:\\Users\\<username>\\OneDrive\\Pictures\\collection\\"
# Download Lively command line utility form github and specify the path below
# Link: https://github.com/rocksdanister/lively/releases/download/v2.0.2.8/lively_command_utility.zip
COMMAND = "C:\\Users\\<username>\\lively-commandline\\lively_command_utility\\Livelycu.exe setwp --file "


files = [os.path.join(DIRECTORY, f) for f in os.listdir("C:\\Users\\<username>\\OneDrive\\Pictures\\collection\\") if os.path.isfile(os.path.join(DIRECTORY, f))]
#pprint(len(files))
random_wallpaper = choice(files)
subprocess.run(COMMAND + random_wallpaper)
exit(0)