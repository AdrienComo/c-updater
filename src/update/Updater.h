#ifndef C_UPDATER_UPDATER_H
#define C_UPDATER_UPDATER_H

#include "python3.8/Python.h"

char const * defaultPythonScriptPath = "src/update/python_downloader.py";

bool checkEmpty(const char * userPath){
    if((userPath != NULL) && (userPath[0] == '\0')){
    	return true;
    }else{
    	return false;
    }
}

bool update(const char * userPath){ 
    bool success = false;
    
    Py_Initialize();
    
    char const * scriptPath;
    char const * modes = "r";
    
    if(checkEmpty(userPath)){
    	scriptPath = defaultPythonScriptPath;
    }else{
    	scriptPath = userPath;
    }
    
    FILE * PythonScriptFile = fopen(scriptPath, modes);
    
    if(PythonScriptFile){
        PyRun_SimpleFile(PythonScriptFile, scriptPath);
        fclose(PythonScriptFile);
        success = true;
    }
    
    Py_Finalize();
    
    return success;
}

#endif //C_UPDATER_UPDATER_H
