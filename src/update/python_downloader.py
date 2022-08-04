import os
import sys
import glob
import wget
import shutil
from zipfile import ZipFile



temporary_directory = 'temporary/' #Name of the temp directory 

local_version_name = 'c-updater-main/' #Name of the decompressed directory
sub_local_version_name = 'c-updater/' #Name of the sub directory

local_version_name_zip = 'c-updater-main.zip' #name of the compressed directory
local_version_path = temporary_directory + local_version_name_zip #Path to the local copy

remote_url         = '..........' #URL to fecth the new version


updatePath = 'src/update/'


def getSoftwareVersion():
    mode = 'r'
    versionFile = updatePath + 'version.txt'

    file = open(versionFile, mode)
    for line in file:
	    softwareVersion = line.strip()
    file.close()
    print(softwareVersion)
 

def checkDirectory():
    isExist = os.path.exists(temporary_directory)
    if(isExist):
        dir = os.listdir(temporary_directory)
        if len(dir) == 0:
    	    shutil.rmtree(temporary_directory, ignore_errors=True)
        else:
            print('The "' + temporary_directory + '" directory is already in use. Cannot update.')
            sys.exit()


def downloadRemoteData():
    os.mkdir(temporary_directory)
    wget.download(remote_url, local_version_path)  

def unzipFiles():
    mode = 'r'
    with ZipFile(local_version_path, mode) as zipObj:
        zipObj.extractall(temporary_directory)
    os.remove(local_version_path)

def checkNewVersion():
    mode = 'r'
    newVersionFile = temporary_directory + local_version_name + sub_local_version_name + updatePath + 'version.txt'

    file = open(newVersionFile, mode)
    for line in file:
	    newSoftwareVersion = line.strip()
    file.close()
    print(newSoftwareVersion)

def replaceFiles():
    path = temporary_directory
    files = [src_files_path for src_files_path in glob.glob(path + "**/*.*", recursive=True)]
    for src_files_path in files:
        dst_files_path = src_files_path.replace(temporary_directory + local_version_name + sub_local_version_name, '')
        os.replace(src_files_path, dst_files_path)
        print(dst_files_path)
        print(src_files_path)



#Main 
getSoftwareVersion()
checkDirectory()  
downloadRemoteData()
unzipFiles()	
checkNewVersion()
replaceFiles()
shutil.rmtree(temporary_directory, ignore_errors=True)
#End main






