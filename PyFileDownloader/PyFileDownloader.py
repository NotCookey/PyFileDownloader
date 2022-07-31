import re
import sys
import random
import requests
import werkzeug


class Downloader:
	def __init__(self, url):
		self.url = url

	def validate_url(self) -> bool:
		response = requests.get(self.url, stream=True)
		if response.status_code in range(200, 299):
			return True
		else:
			return False

	def headers(self) -> dict:
		response = requests.head(self.url)

		filename = response.headers.get("Content-Disposition")
		filesize = response.headers.get("Content-Length")
		filetype = response.headers.get("Content-Type").split(";")[0]

		if filename:
			parsed_headers = werkzeug.http.parse_options_header(
				re.findall("filename=(.+)", filename)[0]
			)

			for keys in parsed_headers:
				if "filename" in keys:
					filename = keys["filename"]
			return {"filename": filename, "filesize": filesize, "filetype": filetype}
		else:
			if "image" in filetype:
				return {
					"filename": "download.jpg",
					"filesize": filesize,
					"filetype": filetype,
				}
			else:
				return {
					"filename": "download.html",
					"filesize": filesize,
					"filetype": filetype,
				}

	def get_file_chunks(self, filename: str = None):
		file_info = self.headers()
		file_name = file_info["filename"]
		response = requests.get(self.url, stream=True)

		if filename:
			file_name = filename
			
		with open(file_name, "wb") as file:
			if file_info["filesize"]:
				size = int(file_info["filesize"])
				current = 0
				for chunk in response.iter_content(chunk_size=4096):
					current += len(chunk)
					downloaded = current / size * 100
					file.write(chunk)
			else:
				file.write(requests.get(self.url, stream=True).content)

		return file_name

	def save(self, filename: str = None):
		if filename:
			self.get_file_chunks(filename)
			return True
		else:
			self.get_file_chunks()
			return True
		return False
