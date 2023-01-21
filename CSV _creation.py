Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def creating ():
...      file = 'data-2016-10-10T00-00-structure-2016-10-10T00-00.csv'
...       with open (file, 'w', encoding = 'utf-8') as data:
...           
SyntaxError: unexpected indent
>>> with open (file, 'w', encoding = 'utf-8') as data:
...     data.write(f'Органы управления дорожным хозяйством, в оперативное управление которых переданы автомобильные дороги федерального значения;Телефоны оперативных дежурных служб'\n')
...                
SyntaxError: unexpected character after line continuation character
>>> data.write(f'Органы управления дорожным хозяйством, в оперативное управление которых переданы автомобильные дороги федерального значения;Телефоны оперативных дежурных служб\n')
...                
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data.write(f'Органы управления дорожным хозяйством, в оперативное управление которых переданы автомобильные дороги федерального значения;Телефоны оперативных дежурных служб\n')
NameError: name 'data' is not defined
>>> def creating ():
...    file = 'data-2016-10-10T00-00-structure-2016-10-10T00-00.csv'
...     with open (file, 'w', encoding = 'utf-8') as data:
...         
SyntaxError: unexpected indent
>>>  with open (file, 'w', encoding = 'utf-8') as data:
...      
SyntaxError: unexpected indent
>>> with open (file, 'w', encoding = 'utf-8') as data:
... data.write(f'Органы управления дорожным хозяйством, в оперативное управление которых переданы автомобильные дороги федерального значения;Телефоны оперативных дежурных служб\n')
SyntaxError: expected an indented block after 'with' statement on line 1
>>> with open (file, 'w', encoding = 'utf-8') as data:
...     data.write(f'Органы управления дорожным хозяйством, в оперативное управление которых переданы автомобильные дороги федерального значения;Телефоны оперативных дежурных служб\n')
