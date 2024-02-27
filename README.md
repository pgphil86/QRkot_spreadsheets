# 'QRKot_spreadsheets' created by Pavel.
```
https://github.com/pgphil86
```
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
### Languages:
### I. [Русский язык.]()
### II. [English language.]()
## I. Проект 'QRKot_spreadsheets'.

### Описание проекта.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых,
на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели,
связанные с поддержкой кошачьей популяции. В приложении реализована возможность формирования отчёта в гугл-таблице.
В таблице должны быть закрытые проекты, отсортированные по скорости сбора средств: от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.
### Работа с проектом.
Для начала необходимо клонировать репозиторий и зайти в рабочую директорию проекта.
```
git clone git@github.com:pgphil86/cat_charity_fund.git
```
```
cd QRkot_spreadsheets
```
Далее создаем и активируем виртуальное окружение.
```
python3 -m venv venv
```
```
source venv/bin/activate
```
После устанавливаем зависимости из requirements.txt.
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
В корневой директории проекта создаем файл .env с переменными:
```
APP_TITLE=Благотворительного фонда поддержки котиков QRKot
APP_DESCRIPTION=Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=YOUR_SECRET_KEY
FIRST_SUPERUSER_EMAIL=EMAIL_SUPERUSER
FIRST_SUPERUSER_PASSWORD=PASSWORD_SUPERUSER
DATABASE_URL=DATA_SUPERUSER
FIRST_SUPERUSER_EMAIL=DATA_SUPERUSER
FIRST_SUPERUSER_PASSWORD=DATA_SUPERUSER
TYPE=DATA_SUPERUSER
PROJECT_ID=DATA_SUPERUSER
PRIVATE_KEY_ID=DATA_SUPERUSER
PRIVATE_KEY=DATA_SUPERUSER
CLIENT_EMAIL=DATA_SUPERUSER
CLIENT_ID=DATA_SUPERUSER
AUTH_URI=DATA_SUPERUSER
TOKEN_URI=DATA_SUPERUSER
AUTH_PROVIDER_X509_CERT_URL=DATA_SUPERUSER
CLIENT_X509_CERT_URL=DATA_SUPERUSER
EMAIL=YOUR_EMAIL
```
Проект можно запускать:
```
uvicorn app.main:app --reload
```

[Вверх.]()

## I. The 'QRKot_spreadsheets' project.

### Description of the project.
The Foundation collects donations for various targeted projects: for medical care of tailed cats in need,
for the establishment of a cat colony in the basement, for food for cats left without care — for any purpose
related to the support of the feline population. The application implements the ability to generate a report in a Google spreadsheet.
The table should contain closed projects sorted by the speed of fundraising: from those that closed the fastest to those that took a long time to collect the required amount.
### Working with the project.
First, you need to clone the repository and go to the working directory of the project.
```
git clone git@github.com:pgphil86/cat_charity_fund.git
```
```
cd QRkot_spreadsheets
```
Next, we create and activate a virtual environment.
```
python3 -m venv venv
```
```
source venv/bin/activate
```
After that, we install the dependencies from requirements.txt .
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Create a file in the root directory of the project.env with variables:
```
APP_TITLE=The Charitable Foundation for the Support of QRKot Seals
APP_DESCRIPTION=The Foundation collects donations for various targeted projects: for medical care of tailed cats in need, for the establishment of a cat colony in the basement, for food for cats left without care — for any purpose related to the support of the feline population.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=YOUR_SECRET_KEY
FIRST_SUPERUSER_EMAIL=EMAIL_SUPERUSER
FIRST_SUPERUSER_PASSWORD=PASSWORD_SUPERUSER
DATABASE_URL=DATA_SUPERUSER
FIRST_SUPERUSER_EMAIL=DATA_SUPERUSER
FIRST_SUPERUSER_PASSWORD=DATA_SUPERUSER
TYPE=DATA_SUPERUSER
PROJECT_ID=DATA_SUPERUSER
PRIVATE_KEY_ID=DATA_SUPERUSER
PRIVATE_KEY=DATA_SUPERUSER
CLIENT_EMAIL=DATA_SUPERUSER
CLIENT_ID=DATA_SUPERUSER
AUTH_URI=DATA_SUPERUSER
TOKEN_URI=DATA_SUPERUSER
AUTH_PROVIDER_X509_CERT_URL=DATA_SUPERUSER
CLIENT_X509_CERT_URL=DATA_SUPERUSER
EMAIL=YOUR_EMAIL
```
The project can be run:
```
uvicorn app.main:app --reload
```

[Up.]()
