from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'A Python module to download any file-type from the internet.'
LONG_DESCRIPTION = 'A Python module to download any file-type from the internet.'

setup(
    name="FileDownloader",
    version=VERSION,
    author="NotCookey",
    url='https://github.com/NotCookey/FileDownloader',
    author_email="kanao.nishimiya@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['werkzeug'],
    keywords=['python', 'file', 'stream', 'download', 'downloader', 'file downloader', 'requests', 'save file', 'download file'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)