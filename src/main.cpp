#include <iostream>

#include "update/Updater.h"

int main(int argc, char * argv[]){

    char const * user_path = "src/update/python_downloader.py";
    	
    bool up = update(user_path);
    
    if(up){
    	std::cout<<"Successfull update."<<std::endl;
    }else{
    	std::cout<<"Unsuccessfull update attempt."<<std::endl;
    }


    return 0;
}
