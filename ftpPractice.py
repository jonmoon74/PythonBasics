from ftplib import FTP
import os


def ftpDownloader(host, path, fileName):
    aftp = FTP(host)
    aftp.login()
    aftp.cwd(path)
    os.chdir("/Users/jonmoon/Downloads")
    with open(fileName, "wb") as file:
        aftp.retrbinary("RETR %s" % fileName, file.write)
    aftp.close()


host = input("Enter the host URL:")
path = input("Enter the path where you want to save the download:")
fileName = input("Enter the name for the downloaded file:")

ftpDownloader(host, path, fileName)
