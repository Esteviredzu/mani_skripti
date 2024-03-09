import sys
import os

def create_cpp_project(folder_name):
    try:
        os.system(f"mkdir {folder_name}")
        
        os.system(f"mkdir -p {folder_name}/src")
        os.system(f"mkdir -p {folder_name}/include")
        os.system(f"mkdir -p {folder_name}/build")

        with open(f"{folder_name}/build/CMakeLists.txt", "w") as cmake_file:
            text = '''cmake_minimum_required(VERSION 3.10)
project(testo)
            
set(CMAKE_CXX_STANDARD 14)
            
include_directories(../include)
file(GLOB SOURCES ../src/*.cpp)
            
add_executable(testo ${SOURCES})'''
            
            cmake_file.write(text)

        with open(f"{folder_name}/src/main.cpp", "w") as main_file:
            text = '''#include <iostream>
            
int main() {
    std::cout << "Hello, World!" << std::endl;
return 0;
            }
            '''
            main_file.write(text)

        with open(f"{folder_name}/compile_and_run.sh", "w") as CAI_file:
            text = f"""
#!/bin/bash

if [ -f ".buildpath" ]; then
    previous_path=$(cat .buildpath)

    if [ "$previous_path" != "$(pwd)" ]; then
        cd build
        shopt -s extglob
        find . ! -name 'CMakeLists.txt' -delete
        cd ..

        echo "$(pwd)" > .buildpath
    fi
else
    echo "$(pwd)" > .buildpath
fi

cd build
cmake .
cmake --build .
./{folder_name}
            """
            CAI_file.write(text)
            
        print(f"Проект '{folder_name}' успешно создан.")
    except FileExistsError:
        print(f"Проект '{folder_name}' уже существует.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python program.py <название_проекта>")
    else:
        folder_name = sys.argv[1]
        create_cpp_project(folder_name)
