# NASA APOD Wallpaper
This is a little program that I wrote which downloads the current NASA APOD (Astronomy Picture of the Day),
saves it on the harddrive and sets it as the wallpaper. Currently works only on Windows.

## Requirements
* Python 3
* Pillow (pip install Pillow)

## Usage
First get a NASA API-Key here (https://api.nasa.gov/). This key will be used to query the NASA API and
to grab the images. Replace "YOUR_API_KEY_GOES_HERE" in the source code with your API and start
the program. The program will then create the directory "images" in the path where its executed
and save the current AOPD in the directory if it does not already exist. To set it as wallpaper, the
image is converted to a bitmap (had problems with setting jpegs as wallpaper).
