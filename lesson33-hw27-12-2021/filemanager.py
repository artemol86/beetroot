# За допомогою вбудованого модуля os реалізувати простий консольний файловий менеджер. Програма має виконувати наступні дії:
# 1. Виводити список вкладених файлів і папок у поточній папці.
# 2. Виводити розгонутий список вкладений об'єктів, рекурсивно відображаючи зміст усіх вкладених папок,
# незважаючи на глибину вкладеності. Вивід має бути зорганізований таким чином6 щоб наочно представляти вкладеність (наприклад,
# вкладені об'єкти зміщуються відносно батьківських на позицію табуляції)
# 3. Зберігати повну структуру вкалдених файлів і папок у JSON файл.
# 4. Створювати нові папки.
# 5. Переіменовувати папки.
# 6. Видаляти папки з усім їх змістом. Якщо заданий об'єкт не є папкою - не видаляти та виводити повідомлення про помилку.
# 7. Створювати нові файли.
# 8. Переіменовувати файли.
# 9. Переміщати файли між папками.
# 10. Видаляти файли. Якщо об'єкт не є файлом - виводити відповідну помилку.
# 11. Виконувати будь-яку додаткову дію на ваш вибір (наприклад, виведення додаткової інформації про файл - розмір, дата модифікації тощо).
# 12. Якщо при переіменуванні/переміщенні/видаленні запитаного файла або папки не існує - виводити повідомлення про помилку.
# 13. Послідовний список усіх дій, виконаних програмою, має зберігатися у файл log.txt у довільному форматі.
# 14. Кожен реалізований метод має мати щонайменше один автоматизований тест до нього.

import os
import json
import shutil
from pathlib import Path

class FileManage:

    def __init__(self):
        self.path = os.path.join(os.getcwd())
        self.my_listdir = os.listdir(self.path)
        self.del_file_list = []

    def del_file_dir(self, *args):
        for item in self.my_listdir:
            for val in args:
                if item == val:
                    self.del_file_list.append(self.my_listdir.pop(self.my_listdir.index(item)))

    def print_tree_dir(self, path=os.path.join(os.getcwd())):
        list_d = os.listdir(path)
        for item in list_d:
            if os.path.isdir(f'{self.path}{item}'):
                return self.print_tree_dir(f'{self.path}{item}')
            else:
                pass

    def dump_json(self):
        path = f'{self.path}file_json.json'
        with open(path, 'w') as file:
            json.dump(self.print_tree_dir(), file)

    def new_dir(self, name):
        if str(name) not in self.my_listdir:
            os.mkdir(os.path.join(os.getcwd(), str(name)))

    def rename_dir(self, old, new):
        os.rename(old, new)

    def del_dir(self, name):
        if os.path.isdir(os.path.join(os.getcwd(), str(name))):
            shutil.rmtree(os.path.join(os.getcwd(), str(name)))
        else:
            raise FileNotFoundError('Is not dir!!!')

    def new_file(self, name):
        with open(os.path.join(os.getcwd(), str(name)), 'w') as file:
            pass

    def rename_file(self, old, new):
        os.rename(old, new)

    def move_file(self, name, new_dir):
        path_name = os.path.join(os.getcwd(), str(name))
        path_dir = os.path.join(os.getcwd(), str(new_dir), str(name))
        shutil.move(path_name, path_dir)

    def del_file(self, name):
        path = os.path.abspath(name)
        print(path)
        if os.path.isfile(path):
            os.remove(path)
        else:
            raise FileNotFoundError('No file!!!')








if __name__ == '__main__':
    file_manager = FileManage()
    # print(file_manager.my_listdir)
    # file_manager.del_file_dir('test_dir', 'test.txt')
    # print(file_manager.del_file)
    # file_manager.print_tree_dir()
    # file_manager.new_dir('test_dir3')
    # file_manager.rename_dir('test_dir3', 'test_dir_renamed')
    # file_manager.del_dir('test.txt')
    # file_manager.new_file('testtest.txt')
    # file_manager.rename_file('testtest.txt', 'test4.txt')
    # file_manager.move_file('test1.txt', 'test_dir')
    #file_manager.del_file('test.txt')


    print(os.listdir(file_manager.path))