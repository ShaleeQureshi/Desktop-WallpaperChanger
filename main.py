import requests
import ctypes
import urllib.request


NASA_API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"  # API
print("USING API\n", NASA_API)
response = requests.get(NASA_API)
data = response.json()

url = data['url']
print(url)
urlSplit = url.split('/')
imageName = urlSplit[len(urlSplit)-1]
print("IMAGE NAME\n", imageName)
req = urllib.request.urlopen(data['url'])
with open(imageName, "wb") as f:
    print("DOWNLOADING...")
    f.write(req.read())
print("Image saved in local directory")
SPI_SETDESKWALLPAPER = 20
SPIF_SENDCHANGE = 2
SPIF_UPDATEINIFILE = 1
ctypes.windll.user32.SystemParametersInfoW(20, 2, imageName, 1)

ctypes.windll.user32.MessageBoxW(
    0, "Wallpaper has been set!", "Wallpaper Changer by Shahrukh Qureshi", 1)
