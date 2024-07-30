# [Flashsend](https://flashsend.pythonanywhere.com/)

Flashsend is a Django-based web application for sharing text snippets. Users can paste text, which will be available for retrieval for 15 minutes before being automatically deleted. Each snippet is associated with a 4-digit retrieval code.

## Features

- Share text snippets with a 4-digit code.
- Snippets are automatically deleted after 15 minutes.
- Simple and clean user interface.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x
- Git

### Installing

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prox004/flashsend.git
   cd flashsend

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup the database:**

```bash
python manage.py migrate
```

4. **Create a superuser:**

```bash
python manage.py createsuperuser
```

5. **Run the development server:**

```bash
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000.


## Built With
- [Django](https://www.djangoproject.com/) - The web framework used
- [Python](https://www.python.org/) - Programming language



## Authors

- [@prox004](https://github.com/prox004)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/prox004/flashsend/blob/main/LICENSE) file for details.

