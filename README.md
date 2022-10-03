
<!-- ABOUT THE PROJECT -->
## О проекте

Система менеджмента сотрдуников для выставления их данных, должности, статуса, подразделения и дальнейшего генирования qr кода(с ссылкой на их профиль). 
Стек: Python, Django, PostgreSQL.
  ![image](https://user-images.githubusercontent.com/82327788/193603342-dadba70f-e6ba-485c-8b61-1b12c82a1184.png)

## Справочник
У компании есть свои подразделения - 
![image](https://user-images.githubusercontent.com/82327788/193602440-1985c38d-45d7-42ed-85f2-43a2d59329eb.png).
У сотрудников есть свои статусы -
![image](https://user-images.githubusercontent.com/82327788/193603580-31afc793-f8b3-4932-b99d-9d2bd080129d.png)![image](https://user-images.githubusercontent.com/82327788/193604192-067ef7c5-33f1-4f31-b060-699bec4137a3.png)

У сотрудников есть свои должности -
![image](https://user-images.githubusercontent.com/82327788/193603861-d9d8e8d8-ea18-4d47-9ed8-ea33b22a3061.png)

## Сотрудники
Сотрудника можно добавить, изменить, удалить.
![image](https://user-images.githubusercontent.com/82327788/193604085-2d3112c5-3967-4bf0-b60f-92d465319107.png)
Страница с данными сотрудника 
![image](https://user-images.githubusercontent.com/82327788/193604298-c0fd4653-ca96-49e7-b719-2cce543c1f5c.png)

### Установка

1. Клонировать данный репозиторий 
   ```sh
   git clone https://github.com/DakaRRR/gs_to_pgsql.git
   ```
2. Зарузить библиотеки.
   ```sh
   pip install -r requirements.txt
   ```
3. Пропишите данные в env файл, в данном формате:
   ```sh
   POSTGRES_DB_NAME=your_db
   etc.
   ```
4.Создание и установка миграций и запуск локального серверва.
   ```sh
     python manage.py makemigrations 
     python manage.py migrate
     python manage.py runserver
   ```
5.Перейти по локальному адресу.





 




