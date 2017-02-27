import json
import os
import urllib.request
import urllib.parse
import urllib.error
import ctypes
import winreg
import shutil
from PIL import Image

############################### Constants ######################################
SPI_SETDESKTOPWALLPAPER = 20
TEMP_PICTURE = "temp.BMP"
CONTROL_PANEL_SUB_KEY = "Control Panel\Desktop"
BASE_DIR = os.getcwd()
PIC_DIR = os.path.join(os.getcwd(), "images")

############################# API Constants ####################################
API_KEY = "YOUR_API_KEY_GOES_HERE"
BASE_URL = "https://api.nasa.gov"
APOD = "/planetary/apod"
API_CALL = BASE_URL + APOD + "?api_key=" + API_KEY

internet_connection = True

# get the response as json
try:
    json_data = urllib.request.urlopen(API_CALL, timeout=2)
except urllib.error.URLError:
    internet_connection = False

if not internet_connection:
    print("No Network connection! ")
    exit(0)

data = json.load(json_data)

# extract date and hd_url (best quality ftw)
date = data['date']
hd_url = data['hdurl']

# name of picture is date, path is working_dir/images
pic_name = date + ".jpg"
pic_path = os.path.join(PIC_DIR, pic_name)
if not os.path.exists(PIC_DIR):
    os.makedirs(PIC_DIR)

# check if picture already exists, if not --> download it
if not os.path.isfile(pic_path):
    urllib.request.urlretrieve(hd_url, pic_name)
    shutil.move(pic_name, os.path.join(pic_path))

# convert image to RGB Bitmap
img = Image.open(pic_path)
img = img.convert("RGB")
img.save(TEMP_PICTURE)

# set registry values to fit the picture on the desktop
key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, CONTROL_PANEL_SUB_KEY, 0,
    winreg.KEY_SET_VALUE)
winreg.SetValue(key, "WallpaperStyle", winreg.REG_SZ, "1")
winreg.SetValue(key, "TileWallpaper", winreg.REG_SZ, "0")

# change the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0,
    os.path.join(os.getcwd(), TEMP_PICTURE), 0)
