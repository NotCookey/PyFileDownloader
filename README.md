# PyFileDownloader
**A Python module to download any file-type from the internet**

## How to install
> **pip3 install PyFileDownloader**

## How To Use
- **Downloading a File**
```py
from PyFileDownloader import Downloader

download=Downloader(url="DOWNLOAD LINK")

headers=download.headers()

is_downloadable=download.validate_url()

download.save() 
```
## Code Breakdown
- **`.headers()` returns you about the file data like filename, filetype, filesize**
- **`.validate_url()` returns True if the provided url is valid**
- **`.save()` downloads the file and saves it with the name provided in the file header**

## Save A File With A Custom Name
- **If you would like to download and save a file with a custom name, you can do so with the `.save()` method. It takes a `filename` parameter that is set to `None` by default.**
```py
from PyFileDownloader import Downloader

download=Downloader(url="DOWNLOAD LINK")
download.save(filename="custom_name.extension") 
```
## Thank you <3
> **Hope you found this useful!**
