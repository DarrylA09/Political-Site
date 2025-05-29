# Political Campaign Site
This project is a political campaign site for political candidate John Wick (JW). The site provides the ability for JW supporters to signup to the campaign, ask questions, view previous questions, view campaign event dates and time and understand the vision and mission of the political party.

## Table of Contents
[Political Campaign Site](#political-campaign-site) 

[Description](#description)

[Table of Contents](#table-of-contents)

[Installation](#installation)

[Usage](#usage)

[URL To GitHub Repository](#url-to-github-repository)

## Description
This project is a political campaign site for political candidate John Wick (JW). The site provides the ability for JW supporters to signup to the campaign, ask questions, view previous questions, view campaign event dates and time and understand the vision and mission of the political party

## Installation
Here are the step to setup and run this project locally:

**Prerequisites**

Ensure you have the following installed:

  * Python 3.12.9 or later

  * Git

  * SQLite3

  * Pip

  * Django 5.1.6 or later

  * Bootstrap

  * Docker

**Environment Variables**

1. Before running the project, create a .env file in the root of your project (the same directory as manage.py).

2. Add the following line to your .env file, replacing the value with your own secret key:   
SECRET_KEY=your-very-secret-django-key

(You can generate a new Django secret key using an online generator or python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())".)

3. Save the file.

4. Make sure .env is listed in your .gitignore so it is not committed to version control.


**Use Python Virtual Environment**

**Step 1: Clone the Repository**
1. git clone https://github.com/DarrylA09/Political-Site.git
2. cd DjangoCapstoneProject

**Step 2: Create and Activate Virtual Environment**
1. Create Virual Environment
 1. python -m venv venv
2. Activate Virtual Environment
 2. On Windows: venv\Scripts\activate
 2. On macOS/Linux: source venv/bin/activate

**Step 3: Install Dependencies**
1. pip install -r requirements.txt

**Apply Migrations**
1. python manage.py migrate

**Collect Static Files**
1. python manage.py collectstatic

**Run the Development Server**
python manage.py runserver**

**Use Docker**

**Build the Docker Image**
1. docker build -t darryla89/politicalsite:political .

**Run Database Migrations in the Container**
1. docker run --rm darryla89/politicalsite:political
2. python manage.py migrate

**Run the Docker Container**
1. docker run -d -p 80:80 darryla89/politicalsite:political

**Access the Application**
1. Open your browser and go to http://localhost:80 (or the mapped port)

## Usage

**Step 1: Here are the key features of the project:**

**Landing Page**
* When the site is load a user will land on the landing page. This page allows a user to sign up, login and view the political party's mission.
![Landing page](<Screenshot 2025-05-29 183926.png>)

**View Vision Page**
* A user can view the vision the party has set out to achieve.
![Vision page](<Screenshot 2025-05-29 183954.png>)

**Ability to Sign up**
* A user can sign up to the site to ask questions to John Wick and check out when campaign event are taking place. 
![Signup page](<Screenshot 2025-05-29 184059.png>)

**Ability to Login**
* A user can login to their account to ask questions and checkout campaign events.
![Login page](<Screenshot 2025-05-29 184124.png>)

**Ability to ask political candidate questions**
* A user can ask important question to the candidate.
![Home page](<Screenshot 2025-05-29 184353.png>)
![Success page](<Screenshot 2025-05-29 184438.png>)

**Ability to view all previously asked questions**
* A user can view all questions from supporters.
![Question List page](<Screenshot 2025-05-29 184457.png>)

**Ability to view campaign events**
* A user can view all events taking place for the party.
![Campaign Date page](<Screenshot 2025-05-29 184534.png>)

## URL To GitHub Repository

Here is a link to access the GitHub repository

[GitHub Repository Political Site](https://github.com/DarrylA09/Political-Site.git)
