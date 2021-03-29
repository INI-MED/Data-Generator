# Data-Generator
Simple data generator for bank user accounts

- Clone this repository to your pc __https://github.com/INI-MED/Data-Generator.git__
- Specify the _number of users_ to create in the class instance creation line in the file ___user.py___

```python
def data_entry():
    user_create = User(10000)
    count = user_create.new_user()
```

- Run: `python user.py`
### This project uses sqlite3. To view the contents of the created database use any online sql editor.
### As example: __https://sqliteonline.com__


# Генератор данных
Простой генератор данных для карточек пользователей банков

- Клонируйте репозиторий __https://github.com/INI-MED/Data-Generator.git__
- Установите количество генерируемых пользователей в строке создания класса в файле ___user.py___

```python
def data_entry():
    user_create = User(10000)
    count = user_create.new_user()
```

- Запустите: `python user.py`
### В этом проекте используется sqlite3. Чтобы посмотреть содержимое созданной базы данных используйте любой онлайн редактор sql.
### Как пример: __https://sqliteonline.com__

