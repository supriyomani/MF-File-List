import socket
import ftplib
import re
from ftplib import FTP
import csv

global RAWfile
port=21
ip=""
user = ''
password = ''

def COBList(FileName):
    global reader, writer
    MFData = (FileName[0:8],FileName[0:])
    CsvData = reader.__next__()
    if MFData[0] == CsvData[0] and MFData[1] == CsvData[1]:
        print('match', reader.line_num)
        ModData = (reader.line_num, CsvData[0], CsvData[1])
        writer.writerow(ModData)
    else:
        print(MFData)
        print(CsvData)

def main():
    global reader, writer 
    inpfilename = "ProgList.csv" ##include directory
    newcsvfile = open(inpfilename, 'r+', newline='')
    reader = csv.reader(newcsvfile, delimiter=',', quotechar='"')
    writer = csv.writer(newcsvfile)
    try:
        s=socket.socket()
        s.connect((ip,port))
        ##print("port",port,"is open")
    except:
        print("port",port,"is closed")

    ftp = FTP(ip)
    ftp.login(user,password)
    ftp.retrlines('LIST \'PKMO.DP.SRCLIB(*)',COBList)
    ftp.quit()
    s.close()
    newcsvfile.close()

if __name__ == '__main__':
    main()
