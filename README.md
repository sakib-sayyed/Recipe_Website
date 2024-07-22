# Recipe_Website

Welcome to **Recipe Website**, a comprehensive web application built using Django, designed for food enthusiasts and home cooks. This project offers a seamless and interactive platform to discover, share, and manage a variety of recipes from around the world.

## Features

- **User Authentication**: Secure sign-up and login functionality with email verification and password reset options.
- **Recipe Management**: Create, edit, and delete recipes with ingredients, instructions, cooking time, and serving size.
- **Search**: Powerful search functionality.
- **Favorites**: Save favorite recipes to help others find the best dishes.
- **Responsive Design**: User-friendly interface that works across all devices, including desktops, tablets, and smartphones.
- **Admin Panel**: Manage users, recipes, and site content efficiently through a comprehensive admin panel.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/recipe_project.git
   cd recipe_project
   
2. **Activate Virtual Environment**:
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. **Setup Your Database**:
### For Using default SQLite
Open your settings.py file and find the DATABASES section.and add that :
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
### For Using MySQL
1. pip install mysqlclient
2. Create a MySQL Database and update the settings
Create a new database for your Django project using the MySQL Workbench or Xampp and update the DATABASES in settings.py.
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recipe_db',         # Name of your database
        'USER': 'your_mysql_user',   # Your MySQL username
        'PASSWORD': 'your_password', # Your MySQL password
        'HOST': 'localhost',         # Set to empty string for localhost
        'PORT': '3306',              # Default MySQL port
    }
}

4. **run migrations**:
python manage.py makemigrations
python manage.py migrate

5. **Create SuperUser**:
python manage.py createsuperuser

6.  **Start the development Server**:
python manage.py runserver

7. **Access the application**:
Open your browser and go to http://127.0.0.1:8000.

## Usage
- Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin with your superuser credentials to manage users and recipes.
- Browse Recipes: Explore and search for recipes on the homepage.
- User Actions: Sign up, log in, create, edit, and delete recipes. Rate and comment on recipes to share your feedback.
Contributing

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute.
