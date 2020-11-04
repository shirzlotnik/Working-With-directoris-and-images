#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:14:40 2020

@author: shirzlotnik
"""

import os
import shutil
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from IPython.display import Image

directory = 'Dirfile'
parent_dir = '/Users/shirzlotnik/Desktop'

full_path =  '/Users/shirzlotnik/Desktop/Dirfile'

img_path = '/Users/shirzlotnik/Desktop/minion.jpg'
img = 'minion.jpg'


def extinct_directory(directory, parent_dir):
    """
    directory: directory name - string
    parent_dir: where am i 
    the function make sure the directory is not already exicst, if so it delete and 
    everything in that directory
    """
    path = os.path.join(parent_dir, directory)
    try:
        os.rmdir(path)
    except OSError:
        shutil.rmtree(path)
        
def create_directory_(directory, parent_dir):
    """
    directory: directory name - string
    parent_dir: where am i 
    the function crate directory and 2 subdirectories - test, train.
    """
    path = os.path.join(parent_dir, directory)
    # check if directory doesnt alredy exist
    if os.path.isdir(path):
        extinct_directory(directory, parent_dir)
    os.mkdir(path)
    print(f'Directory {directory} was created')
    create_subdirectory_(path,'train',directory)
    create_subdirectory_(path,'test',directory)
    return path
        


def create_subdirectory_(parent_dir, directory, prev_dir):
    """
    directory: directory name - string
    parent_dir: where am i 
    prev_dir: name of parent directory
    the function crate subdirectory.
    """
    path = os.path.join(parent_dir, directory)
    # check if directory doesnt alredy exist
    
    if os.path.isdir(path):
        extinct_directory(directory, parent_dir)
        
    os.mkdir(path) 
    print(f'Directory {prev_dir}/{directory} was created') 
    
    
    
def add_file(file_name, file_path, path):
    """
    file_name: the name of the file .jpg
    file_path: the file path
    path: where do i want to add this file
    the function check that the file is not in one of the directories if not
    it add it to directory Dirfile
    """
    new_path = os.path.join(path, file_name)
    if file_name in os.listdir(path) or file_name in os.listdir(os.path.join(path, 'train')) or file_name in os.listdir(os.path.join(path, 'test')):
        print('file already exist')
    else:
        #print(f'Before -> {os.listdir(path)}')
        dest = shutil.copy(file_path, new_path)
        #print(f'After -> {os.listdir(path)}')
        #print('Destanation -> {}'.format(dest))
    
    
def check_if_correct_path(full_path, path_from_func):
    """
    path_from_func: the path directory from the function that created it
    full_path: string
    the function checks if the directory was created in the correct location.
    """
    return full_path == path_from_func

def plottt(path):
    """
    path: directory path
    the function print the directory files and plot the image
    using matplotlib.pyplot,  matplotlib.image
    """
    files = [f for f in os.listdir(path) if f.endswith('.jpg')]
    for file in files:
        img = os.path.join(path,file)
        img_data = mpimg.imread(img)
        plt.imshow(img_data)
        plt.show()
    
def plot_from_directory(path):
    """
    path: directory path
    the function print the directory files and plot the image
    using IPython.core.display.Image
    """
    print('\n {} \n'.format(os.listdir(path)))
    files = [f for f in os.listdir(path) if f.endswith('.jpg')]
    for file in files:
        img = Image(filename=os.path.join(path,file))
        display(img)
        
    

    
    
PATH = create_directory_(directory, parent_dir)
print(f'\n{os.path.join(PATH, img)}')
add_file(img,img_path, PATH)
print(f'\n{os.listdir(PATH)}\n')
for a in range(3):
    add_file(img,img_path, PATH)
print(check_if_correct_path(full_path, PATH))
plot_from_directory(PATH)