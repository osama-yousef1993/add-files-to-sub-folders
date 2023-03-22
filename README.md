# add-files-to-sub-folders

## To Run Code

- python3 -m app

# Code Explanation

## Code Structure

- the code contains main function that the execution will start from it.
- there are Two main folders:
  - the Handler Folder.
  - the Helper Folder.

    #### Handler Folder
    - it contains FolderProcess class with process function
    - init function will call another class that will check if the folders are created or not based on unique files names.
    - the process function will get the list of files from files folders and move it to it's folder.

    #### Helper Folder
    - it contains Helper class with two functions:
        - ***check_folders_existents***
        - ***create_languages_folders***
    - create_languages_folders: in this function will get all files and create list with unique names.
    - Then will use check_folders_existents to check if folder exist or not exists
    - after that the folder for each language will be created.
