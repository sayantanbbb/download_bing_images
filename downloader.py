from icrawler.builtin import BingImageCrawler
import cv2
import os
from tqdm import tqdm
import numpy as np
import pickle

def save(array,name):
    try:
        np.save(open(name,'wb'),array)
        print('saved succesfully')
    except:
        print(' This is an error "could not save at given destination" ')
        
        
def convert_to_matrix(dir,flag,pad,slash):
    matrixes=[]
    for x in tqdm(os.listdir(dir),desc='converting'):
        x=dir+slash+x

        try:
          mat=cv2.resize(cv2.imread(x,flags=flag),pad)
          
          #print(type(mat[0][0][0]))
          matrixes.append(mat)
          
        except:
          print('could not read file')
    return matrixes
def download(key='cat',max_num=100,storage_dir=None,store_to_array={'convert':False,'return':False},flag=0,array_name=None,pad=(28,28),slash='\\'):
    if storage_dir==None:
        raise Exception("Please, please mention storage_dir it cannot be None")
    if type(max_num)!=type(0):
        raise ValueError(f'max number is not in type int type_found :-{type(max_num)}')
    if max_num<=0:
        raise ValueError("Sorry, max_num must be greater than 0")
    if type(key)!=type('cat'):
        raise ValueError(f'key is not in type str type_found :-{type(key)}')
    google=BingImageCrawler(storage={'root_dir':storage_dir})
    google.crawl(keyword=key,max_num=max_num)
    if store_to_array['convert']==True:
        array=convert_to_matrix(storage_dir,flag,pad,slash)
        if array_name!=None:
            save(array,array_name)
        if store_to_array['return']==True:
            return np.array(array)

if __name__=='__main__':
    array=download('hot_dogs',5,'C:\\Users\\USER\\Documents\\downloaded',{'convert':True,'return':True},1,'C:\\Users\\USER\\Documents\\saves\\1.npy')
    

    


