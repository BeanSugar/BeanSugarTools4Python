__author__ = 'archmagece'

import paramiko
import os
import errno
import ftplib


class SftpSender():

    def __init__(self, settings):
        if settings.protocol not in ("sftp", "ssh"):
            raise Exception("parameter error")
        self.settings = settings
        self.remoteClient = self.generateConnection(settings)
        pass

    def sendFile(self, fileFullName):
        fileName = os.path.basename(fileFullName)

        # print fileName, file_patterns.patternCheck(fileName)
        if self.settings.startPatternCheck(fileName) or self.settings.regexPatternCheck(fileName):
            ##upload
            uploadFileName = os.path.join(self.settings.remoteUploadDir, fileName+".tmp")
            #path exist check
            # self.createPath(uploadFileName)
            # uploadFileName = os.path.join(self.settings.remoteDir, fileName+".tmp")
            #TODO Exception is better?
            if self.exists(uploadFileName):
                self.remove(uploadFileName)
            self.upload(fileFullName, uploadFileName)

            ##uploadSuccessCheck
            newPath = os.path.join(self.settings.remoteDir, fileName)
            #TODO Exception is better?
            if self.exists(newPath):
                self.remove(newPath)
            self.rename(uploadFileName, newPath)
            self.chmod(newPath, 0777)
            pass
        pass

    def generateConnection(self, settings):
        transport = paramiko.Transport((settings.url, settings.port))
        # print "fjjkfwlw   ", settings.username, settings.password
        transport.connect(username=settings.username, password=settings.password)

        remoteClientLocal = paramiko.SFTPClient.from_transport(transport)
        return remoteClientLocal
        pass

    def createPath(self, remote_abspath):
        pathList = remote_abspath.split("/")
        self.remoteClient.chdir("/")
        for path in pathList:
            try:
                # if self.exists(path):
                #     return
                self.remoteClient.chdir(path)  # Test if remote_path exists
            except IOError:
                self.remoteClient.mkdir(path)  # Create remote_path
                self.remoteClient.chdir(path)

    def upload(self, localFilePath, remoteFilePath):
        print "upload log :", localFilePath, remoteFilePath
        print self.remoteClient.put(localFilePath, remoteFilePath)
        self.remoteClient.chmod(remoteFilePath, 0777)
        pass

    def rename(self, remoteFileOriginalPath, remoteFileNewPath):
        print "rename log :", remoteFileOriginalPath, remoteFileNewPath
        print self.remoteClient.rename(remoteFileOriginalPath, remoteFileNewPath)
        pass
    pass

    def exists(self, path):
        """os.path.exists for paramiko's SCP object
        """
        try:
            self.remoteClient.stat(path)
        except IOError, e:  # or "as" if you're using Python 3.0
            # if 'No such file' in str(e):
            if e.errno == errno.ENOENT:
                return False
            raise
        else:
            return True

    def remove(self, path):
        self.remoteClient.remove(path)
        pass

    def chmod(self, path, permissionNumber):
        self.remoteClient.chmod(path, permissionNumber)
        pass


class FtpSender():

    def __init__(self, settings):
        if settings.protocol not in ("ftp", "ftps"):
            raise Exception("parameter error")
        self.settings = settings
        self.remoteClient = self.generateConnection(settings)
        pass

    def sendFile(self, fileFullName):
        fileName = os.path.basename(fileFullName)

        # print fileName, file_patterns.patternCheck(fileName)
        if self.settings.startPatternCheck(fileName) or self.settings.regexPatternCheck(fileName):
            ##upload
            uploadFileName = os.path.join(self.settings.remoteUploadDir, fileName+".tmp")
            # uploadFileName = os.path.join(self.settings.remoteDir, fileName+".tmp")
            # TODO Exception is better?
            # if self.exists(uploadFileName):
            #     self.remove(uploadFileName)
            self.upload(fileFullName, uploadFileName)

            ##uploadSuccessCheck
            newPath = os.path.join(self.settings.remoteDir, fileName)
            #TODO Exception is better?
            # if self.exists(newPath):
            #     self.remove(newPath)
            self.rename(uploadFileName, newPath)
            self.chmod(newPath, 0777)
            pass
        pass

    def generateConnection(self, settings):
        # conn = ftplib.FTP(host=settings.url, user=settings.username, passwd=settings.password)
        conn = ftplib.FTP()
        conn.connect(host=settings.url, port=settings.port)
        conn.login(user=settings.username, passwd=settings.password)
        return conn

    def upload(self, localFilePath, remoteFilePath):
        print "upload log :", localFilePath, remoteFilePath
        # ext = os.path.splitext(file)[1]
        # if ext in (".txt", ".htm", ".html"):
        #     self.remoteClient.storlines("STOR " + file, open(file))
        # else:
        #     self.remoteClient.storbinary("STOR " + file, open(file, "rb"), 1024)
        self.remoteClient.storbinary("STOR " + remoteFilePath, open(localFilePath, "rb"), 1024)
        # self.remoteClient.chmod(remoteFilePath, 0777)
        pass

    def rename(self, remoteFileOriginalPath, remoteFileNewPath):
        print "rename log :", remoteFileOriginalPath, remoteFileNewPath
        self.remoteClient.rename(remoteFileOriginalPath, remoteFileNewPath)
        pass
    pass

    def exists(self, path):
        """os.path.exists for paramiko's SCP object
        """
        try:
            self.remoteClient.nlst(path)
        except IOError, e:  # or "as" if you're using Python 3.0
            # if 'No such file' in str(e):
            if e.errno == errno.ENOENT:
                return False
            # raise
        else:
            return True

    def remove(self, path):
        self.remoteClient.rmd(path)
        pass

    def chmod(self, path, permissionNumber):
        # self.remoteClient.chmod(path, permissionNumber)
        pass


def main():

    # site = config.domain.Site()
    # remote = SftpSender(site)
    # remote.upload("/Users/archmagece/data.txt", "/home/data.txt")
    # remote.rename("/home/data.txt")

    pass

if __name__ == '__main__':
    main()
