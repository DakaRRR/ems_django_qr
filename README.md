
<!-- ABOUT THE PROJECT -->
## О проекте

Система менеджмента сотрдуников для выставления их данных, должности, статуса, подразделения и дальнейшего генирования qr кода(с ссылкой на их профиль). 
  ![image](https://user-images.githubusercontent.com/82327788/193603342-dadba70f-e6ba-485c-8b61-1b12c82a1184.png)

## Построено с

[![My Skills](https://skills.thijs.gg/icons?i=python,django,postgresql,html,css,js&theme=dark)](https://skills.thijs.gg)


## Справочник
У компании есть свои подразделения, которые как и все последующие данные выбираются при добавлении сотрудника. 

У сотрудников есть свои статусы(пр. "Уволен" и тд.) и должности.
<br>

Данные отоброжаются по индексам, к примеру при присвоение главному подразделению индекс 1, в таблице оно будет отображаться первым, как и его сотрудники. 
![image](https://user-images.githubusercontent.com/82327788/193606064-623134d7-9ba2-47ce-9af6-b3dd6b7e3b5b.png)

Так же работает с должностями.

## Сотрудники

Во время добавления сотрудника создается персональный qr код, который хранит в себе ссылку на переход в страницу его данных.
Страница с данными сотрудника 
![image](https://user-images.githubusercontent.com/82327788/193604298-c0fd4653-ca96-49e7-b719-2cce543c1f5c.png)
<br>


Сотрудники отоброжаются по индексам их филиалов и должности.
<div align="center"> 
  <img src="https://user-images.githubusercontent.com/82327788/193607938-c5e8c89b-28f9-4995-afbc-bdb9d9553dc8.png" alt="screenshot" />
</div>
<br>
У каждого подразделения отдельный список сотрудников

### Установка

1. Клонировать данный репозиторий 
   ```sh
   git clone https://github.com/DakaRRR/ems_django_qr.git
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





 




