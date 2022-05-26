# About
This is a simple python script that allows to generate a .txt that contains the file structure of you project files and folders. This as and option to incorporate icons, such as folder and file icons.
- Here is an example without icons:
```txt
    |--folder1
    |   |-file2.txt
    |   |-file3.txt
    |
    |--folder2
    |   |-file1.txt
    |   |--folder3
    |   |   |-hello_world.txt
    |
    |
    |-hello.txt
    |-main.py
    |-output.txt
    |-README.md
    |-test.txt
```

- Here is an example with icons:
```txt
    |📂 folder1
    |   |📄 file2.txt
    |   |📄 file3.txt
    |
    |📂 folder2
    |   |📄 file1.txt
    |   |📂 folder3
    |   |   |📄 hello_world.txt
    |
    |
    |📄 hello.txt
    |📄 main.py
    |📄 out.txt
    |📄 output.txt
    |📄 README.md
    |📄 test.txt
```

# Instructions
In order to execute the script one just needs to type this command `python main.py [FLAGS]` or `python3 main.py [FLAGS]` depending on your version.

The available flags are:

- **-p**: specify the path to the directory in question *Mandatory*
- **-i**: if set, will enable the icons.
- **-f**: path and/or name of the output file where it should write the output. *If none set, the program will simply print to the console*
