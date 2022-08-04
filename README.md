## c-updater

### Update software via makefile execution  

Each time the user executes the makefile, this code fetches via URL, if it exists, a new version of the code and replaces old code with the new one. <br> 
This can update any kind of code as long as the tree structure is identical between the old and new versions. i.e : You cannot send out new files, that didn't exist. You can _only_ update/replace existing code/images/documents... <br>
If the fetched version has the same version number as the current version the update is not carried out. <br>

### How to use
 - You will have to modify the paths and names in ```src/update/python_downloader.py``` and  ```src/update/Updater.h``` <br>
 - The version number will also have to be changed in ```src/update/version.txt``` <br>
 - Type : ```make clean && make && ./bin/main``` <br>

### Dependencies

```Python3.8``` and ```C/C++ with makefile```

Libraries          | Use                            | 
------------------ | ------------------------------ | 
wget               | Fecth URL's                    |    
ZipFile            | Unzip documents                |
os and sys         | Os and system access           | 
shutil             | Creating/deleting directories  |
glob               | Loop through directories       | 
   
                                            

### Compatibility

Tested on _Ubuntu_ systems.

