# download_bing_images 😊

### Download images from bing with python

#### [Download images in colab](https://colab.research.google.com/drive/1wzrjoyO5VUcbZigz3dI51p716aXveWlq?usp=sharing)

## Set up requirements

```bash
cd download_bing_images
pip install -r requirements.txt
```
## Clone repo

```bash
!git clone https://github.com/sayantanbbb/download_bing_images.git
```
## Import

```bash
import download_bing_images as db
db.__version__
```
## Output

```bash
0.0.1
```
## Params 


#### key : What you want to download
#### max_num : How many images you want to download 'Note :- Warning the module may not be able to download all images because of connection problem always incrase 'max_num' by 200 or 300'
#### storage_dir : Where you want to store the images
#### store_to_array : Takes a dictionary of two params 'convert' and 'return' ex:-{'convert':True,'return':True} if convert is set to True then it will load all the images in storage_dir with cv2 and resize them to pad if 'return' is also True then it will also return the array
#### array_name : 'Only works if convert is True' it saves the array as array_name 
#### slash : If path contains '\\\' slash='\\\\' slash in path is also dubbled ('C:\users' is changed to 'C:\\\\users') it neatly , do the same for '/' (path='/content',storage_dir='//content',slash='//')
#### flag : if 0 loads the image matrixes (store_to_array['convert']) in gray_scale if 1 then colorfull
#### pad : resizes loaded image matrixes to pad ex:-(28,28)

## Download

```bash
downloader=db.downloader
key='cat'
path='//content//cats'
images=downloader.download(key,storage_dir=path,store_to_array={'convert':True,'return':True},array_name='//content//cats.npy',pad=(60,60),slash='//',max_num=500,flag=1)
```
```bash
images.shape
```
##### (497,60,60,3)

