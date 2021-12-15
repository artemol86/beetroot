from PIL import Image
import requests
import os
import threading
import multiprocessing
import time

#1. Створити декоратор, який засікає час виконання задекорованої функції
def time_decor(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print(f'{func.__name__} {args} {time.time() - start_time}')
        return func(*args)
    return wrapper
    
#2. Створити функцію load_image(url), яка завантажує картинку з заданого url

url = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'

def load_image(url, filename='example.jpg' ):
    image = Image.open(requests.get(url,stream=True).raw)
    image.save(os.path.join(os.getcwd(), filename))

#3. Створити функцію rotate_image(file, degrees), яка обертає обраний файл на задану кількість градусів
def rotate_image(file, degrees):
    image = Image.open(f'{file}')
    rotated = image.rotate(degrees)
    rotated.save(f'rotated_{file}')

#4. Створити функцію write_to_file(file), яка записуватиме в обраний файл 10 000 рядків (наприклад, 'Hello World'*10000)

def write_to_file(file):
    f = open(f'{file}', 'w')
    f.write("Hello World\n"*10000)
    f.close()


#5. Створити функцію delete_file(file), яка видалятиме обраний файл, якщо він існує.

def delete_file(file):
    if os.path.abspath(f'{file}'):
            os.remove(f'{file}')
    else:
        raise FileNotFoundError('No such file!')

#6. Відімпортувати threading та multiprocessing DONE
'''7. для кожної функції з пунктів 2 - 5 створити по три функції, кожна з которих робитиме три виклики цільової 
функції у потоках, процессах та без конкуренції. Наприклад, для функції load_image мають бути створені такі функції: 
    - load_image_threading - створює три потоки, які отримують load_image як target;
    - load_image_processes - створює три процеси, які отримують load_image як target
    - load_image_noconcurrent - тричі піряд викликає load_image без жодної конкуренції
'''

url = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'
url2 = 'https://jpeg.org/images/jpeg-home.jpg'
url3 = 'https://www.imgonline.com.ua/examples/jpeg-artifacts_3x.png'
t1 = threading.Thread(target=load_image, args=(url, 't1.jpg'))
t2 = threading.Thread(target=load_image, args=(url2, 't2.jpg'))
t3 = threading.Thread(target=load_image, args=(url3,'t3.jpg'))
m1 = multiprocessing.Process(target=load_image, args=(url, 't1.jpg'))
m2 = multiprocessing.Process(target=load_image, args=(url2, 't2.jpg'))
m3 = multiprocessing.Process(target=load_image, args=(url3,'t3.jpg'))

######load_image_threadings
@time_decor
def load_image_threading():
    for t in t1, t2, t3:
        t.start()

######load_image_processes
@time_decor
def load_image_processes():
    for m in m1, m2, m3:
        m.start()
        m.join()

######load_image_noconcurrent
@time_decor
def load_image_noconcurrent():
    load_image(url, filename='example1.jpg' )
    load_image(url2, filename='example2.jpg' )
    load_image(url3, filename='example3.jpg' )

######rotate_image_threadings
@time_decor
def rotate_image_threading():
    t1=threading.Thread(target=rotate_image, args=('example1.jpg', 45))
    t1.start()
    t2=threading.Thread(target=rotate_image, args=('example2.jpg', 45))
    t2.start()
    t3=threading.Thread(target=rotate_image, args=('example3.jpg', 45))
    t3.start()

######rotate_image_processes
@time_decor
def rotate_image_processes():
    m1 = multiprocessing.Process(target=rotate_image, args=('example1.jpg', 45))
    m1.start()
    m2 = multiprocessing.Process(target=rotate_image, args=('example2.jpg', 45))
    m2.start()
    m3 = multiprocessing.Process(target=rotate_image, args=('example3.jpg', 45))
    m3.start()

######rotate_image_noconcurent
@time_decor
def rotate_image_noconcurrent():
    rotate_image('example1.jpg', 45)
    rotate_image('example1.jpg', 45)
    rotate_image('example1.jpg', 45)

#######write_to_file_threadings
@time_decor
def write_to_file_threading():
    thread1=threading.Thread(target=write_to_file, kwargs={'file': 'hi10000_1.txt'})
    thread1.start()
    thread2=threading.Thread(target=write_to_file, kwargs={'file': 'hi10000_2.txt'})
    thread2.start()
    thread3=threading.Thread(target=write_to_file, kwargs={'file': 'hi10000_3.txt'})
    thread3.start()

#######write_to_file_processes

@time_decor
def write_to_file_processes():
    m4 = multiprocessing.Process(target=write_to_file, kwargs={'file': 'hi10000_1.txt'})
    m4.start()
    m5 = multiprocessing.Process(target=write_to_file, kwargs={'file': 'hi10000_2.txt'})
    m5.start()
    m6 = multiprocessing.Process(target=write_to_file, kwargs={'file': 'hi10000_3.txt'})
    m6.start()

#write_to_file_noconcurrent already realised func in task#4 
######rotate_image_noconcurent
@time_decor
def write_to_file_noconcurrent():
    write_to_file('hi10000_1.txt')
    write_to_file('hi10000_2.txt')
    write_to_file('hi10000_3.txt')


#######delete_file_threadings
@time_decor
def delete_file_threading():
    t4=threading.Thread(target=delete_file, kwargs={'file': 'hi10000_1.txt'})
    t4.start()
    t5=threading.Thread(target=delete_file, kwargs={'file': 'hi10000_2.txt'})
    t5.start()
    t6=threading.Thread(target=delete_file, kwargs={'file': 'hi10000_3.txt'})
    t6.start()

#delete_file_processes
@time_decor
def delete_file_processes():
    m4 = multiprocessing.Process(target=delete_file, kwargs={'file': 'hi10000_1.txt'})
    m4.start()
    m5 = multiprocessing.Process(target=delete_file, kwargs={'file': 'hi10000_2.txt'})
    m5.start()
    m6 = multiprocessing.Process(target=delete_file, kwargs={'file': 'hi10000_3.txt'})
    m6.start()
#delete_file_processes_noconcurrent 
@time_decor
def delete_file_noconcurrent():
    delete_file('hi10000_1.txt')
    delete_file('hi10000_2.txt')
    delete_file('hi10000_3.txt')

#######


# 8. Усі сторені у пункті 7 функції задекорувати декоратором з пункту 1 
#Done

# 9. Викликати усі створені та задекоровані функції
#Done

# 10. Порівняти результати виконання кожної функції '''

'''
Results:
load_image_threading () 0.0013606548309326172
load_image_processes () 2.8377907276153564
load_image_noconcurrent () 2.3433165550231934
rotate_image_threading () 0.0019233226776123047
rotate_image_processes () 0.0032150745391845703
rotate_image_noconcurrent () 0.47600626945495605
write_to_file_threading () 0.0008311271667480469
write_to_file_processes () 0.0033495426177978516
write_to_file_noconcurrent () 0.001249551773071289
delete_file_threading () 0.0005457401275634766
delete_file_processes () 0.0028035640716552734
delete_file_noconcurrent () 0.00025391578674316406

'''


if __name__ == '__main__':
    #hello(5)
    #write_to_file('hi10000.txt')
    #delete_file('hi10000.txt')
    #load_image_threading()
    #load_image_processes()
    #load_image_noconcurrent()
    #rotate_image_threading()
    #rotate_image_processes()
    #rotate_image_noconcurrent()
    #write_to_file_threading()
    #write_to_file_processes()
    #write_to_file_noconcurrent()
    #delete_file_threading()
    #delete_file_processes()
    delete_file_noconcurrent()