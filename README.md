# Microservices
## Step 1:
> Move to Current Downloaded Location using cmd or terminal, if you see the Project in your current directory <br>
> Check if, req.txt file exists

## Step 2:
> If you want install in seperate location using virtaulenv or else continue step<br>
> In windows,<br>
`pip install virtualenvwrapper-win` <br>
> Once Completed, create virtual environment using <br>
`mkvirtualenv env_name `<br>
> If want Use it again use, <br>
`workon env_name `<br>

## Step 3:
  ` pip install -r req.txt `
  
## step 4:
  ` python manage.py collectstatic`
  
## setp 5:
  `python manage.py makemigrations`
  
## setp 6:
  `python manage.py migrate`
 > Basic updation in database in **sqlite.db** file in your project
 
## step 7:
 > Create Superuser in django admin <br>
  `python manage.py createsuperuser`<br>
 
 > Remember Username and pwd
## Step 8:
 > Run django server <br>
 `python manage.py runserver`
 

## Step 9:
 > Add Datas to Books Table, go to this url <br>
 `http://localhost:8000/admin` <br>
 > Login using superuser, username and pwd <br>
 > Use Books table, click and insert records
 
 ## step 10:
 > Check Working Correctly in api, go to this url <br>
 `http://localhost:8000/api/book/` <br>
 > Insert data are display <br>
 > Change format json using **?format=json**<br>
 `http://localhost:8000/api/book/?format=json` <br>
 
 
 
 
 
 
 
 
