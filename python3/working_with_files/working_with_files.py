import os, fnmatch


def list_dir(folder_path,):
    for i in os.listdir(folder_path):
        print(i)


def ends_with(folder_path, search):
    for i in os.listdir(folder_path):
        if i.endswith(search):
            print(i)

def starts_with(folder_path, search):
    for i in os.listdir(folder_path):
        if i.startswith(search):
            print(i)

def math(folder_path, search):
    for i in os.listdir(folder_path):
        if fnmatch.fnmatch(i, search):
            print(i)

#list_dir('./files')
# ends_with('./files', '.txt')
# starts_with('./files', 'text')
math('./files', '*1*_test.csv')
