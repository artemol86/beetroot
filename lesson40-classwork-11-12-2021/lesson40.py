'''
1. Создать сайт организации визитов деда мороза
2. Добавить возможность записи ребенка, указывать имя ребенка, адрес, возраст, желаемый подарок 
    
3. Добавить разделение дитей по возрасту # select 
4. Реализовать вывод всех записаных дитей и всех возрасных групп ##вывод всей таблицы
5. Реализовать метод отображения посещенных дитей # via visited column check

def write_to_file(file):
    with open(f'{file}','w+') as f:
        for i in range(10000):
            f.write('Hello World\n')

BD name = children.db
table = children
columns = id(primary key), name, address, age, gift, visited
Как вручную создавать записи о детях и саму базу:
(venv) artem@KHLT-00002:~/beetroot/lesson40-classwork-11-12-2021$ sqlite3 children.db
SQLite version 3.37.0 2021-11-27 14:13:22
Enter ".help" for usage hints.
sqlite> .databases
main: /home/artem/beetroot/lesson40-classwork-11-12-2021/children.db r/w
sqlite> CREATE TABLE IF NOT EXISTS children(id integer PRIMARY KEY, name text, address text, age integer, gift text, visited integer default 0);
sqlite> select * from children;
sqlite> insert into children(name, address, age, gift) values('Petr Ivanov', 'Kiev Khreshatyk 19/25', '3', 'fire truck');   
sqlite> insert into children(name, address, age, gift) values('Petr Ivanov', 'Kiev Khreshatyk 19/25', '3', 'fire truck');
sqlite> select * from children;
1|Ivan Petrov|Kiev Khreshatyk 18/23|3|fire truck|0
2|Petr Ivanov|Kiev Khreshatyk 19/25|3|fire truck|0
sqlite>



'''

