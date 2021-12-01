from PIL import Image
import requests
import os
import threading


url = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'
url2 = 'https://jpeg.org/images/jpeg-home.jpg'
url3 = 'https://www.imgonline.com.ua/examples/jpeg-artifacts_3x.png'
url4 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/JPEG_example_down.jpg/350px-JPEG_example_down.jpg'
url5 = 'https://cdn.fstoppers.com/styles/full/s3/media/2019/12/04/nando-jpeg-quality-099.jpg'


def load_image(url, filename='example.jpg' ):
    image = Image.open(requests.get(url,stream=True).raw)
    image.save(os.path.join(os.getcwd(), filename))

def printImageData(file):
    image = Image.open(file)
    print(image.size, image.mode)
def is_square_image(file):
    image = Image.open(file)
    if image.size[0] != image.size[1]:
        print('Not a square')
    else:
        print('This is a square image')    
    
def create_thumbnail(file):
    #TODO: handle all errors on thumbnail creation
    thumbnail_size = (200, 200)
    image = Image.open('example.jpg')
    image.thumbnail(thumbnail_size)
    image.save('thumbnail.jpg')

def is_thumbnail(file):
    thumbnail_size = (200, 200)
    image = Image.open(file)
    return image.size == thumbnail_size


def rotate_image(file, degrees):
    image = Image.open('example.jpg')
    rotated = image.rotate(degrees)
    rotated.save('rotated.jpg')

def flip_image(file, direction):
    directions = {'LT': Image.FLIP_LEFT_RIGHT, 'TB':Image.FLIP_TOP_BOTTOM}
    image = Image.open(file)
    out = image.transpose(directions[direction])
    out.save('flipped.jpg')
def copy_images_to_dir(dirname):
    '''Copies all images from current folder into subfolder'''
    for file in os.listdir(os.path.join(os.getcwd())):
        try:
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))
        except:
            break
def delete_images():
    for file in os.listdir(os.path.join(os.getcwd())):
        if file.endswith('.jpg'):
            os.remove(file)
#TODO: create a function that will save rectangle area from given image to the separate file
#with name 'rectangle.jpg'. Coordinates of rectangle have to be passed as tuple of 4 integers
def crope_file(file):
    image = Image.open(os.path.join(os.getcwd(), 'images', file)) 
    file_cropped = image.crop((100, 100, 200, 200))  
    file_cropped.save('rectangle.jpg')


t1 = threading.Thread(target=load_image, args=(url, 't1.jpg'))
t2 = threading.Thread(target=load_image, args=(url2, 't2.jpg'))
t3 = threading.Thread(target=load_image, args=(url3,'t3.jpg'))
t4 = threading.Thread(target=load_image, args=(url4, 't4.jpg'))
t5 = threading.Thread(target=load_image, args=(url5, 't5.jpg'))

for t in t1, t2, t3, t4, t5:
    t.start()


#if __name__ == '__main__':
#    load_image(URL)
#    printImageData('example.jpg')
#    is_square_image('example.jpg')
#    create_thumbnail('example.jpg')
#    print(is_thumbnail('thumbnail.jpg'))
#    rotate_image('example.jpg', 45)
#    flip_image('example.jpg', 'LT')
#    copy_images_to_dir('images')
#    delete_images()
#    crope_file('example.jpg')
print('Done!')