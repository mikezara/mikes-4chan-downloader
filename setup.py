from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["urllib.request","lxml.html","wx","os","math","validators","mimetypes"], "optimize":2}


setup(
    name="4chanDownloader",                           
    version="0.2",                              
    options = {"build_exe": build_exe_options}, 
    executables=[Executable("main.py")]
)
