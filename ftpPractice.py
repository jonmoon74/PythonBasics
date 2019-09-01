from ftplib import FTP
import os


def ftpDownloader(host, path, fileName):
    aftp = FTP(host)
    aftp.login()
    aftp.cwd(path)
    os.chdir("~/Downloads")
    with open("fileName", "wb") as file:
        aftp.retrbinary("RETR fileName", file.write)
    aftp.close()


host = ""
path = ""
fileName = ""

ftpDownloader(host, path, fileName)
