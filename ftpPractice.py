from ftplib import FTP
import os


def ftpDownloader(host, path, fileName):
    aftp = FTP(host)
    aftp.login()
    aftp.cwd(path)
    with open("fileName", "wb") as file:
        aftp.retrbinary("RETR %s" % fileName, file.write)
    aftp.close()


host = ""
path = ""
fileName = ""

ftpDownloader(host, path, fileName)
