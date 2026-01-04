Job Board API using Django REST Framework

1. Project Title
   
   Job Board API using Django REST Framework

3. Project Description
   
   This is a RESTful backend API built with Django and Django REST Framework for a job board platform. It allows employers to post job listings and manage their companies, while enabling job seekers to browse jobs and submit applications. The API handles user authentication, company management, job postings, and application tracking with secure role-based access control.

4. Features
   
User Authentication - Register, login, and logout with token-based authentication

Company Management - Create, read, update, and delete company profiles

Job Posting System - Employers can post and manage job listings

Job Applications - Job seekers can apply for jobs with resume and cover letter

Role-Based Access Control - Different permissions for employers and job seekers

Job Filtering - Filter jobs by location, company, and status

Admin Interface - Django admin panel for easy data management

Browsable API - User-friendly interface for testing endpoints

5. Tech Stack
   
 Python, Django, Django REST Framework

SQLite database

Token authentication

6. Project Structure

job-board-api/

├── config/ # Django project configuration

│ ├── settings.py # Project settings

│ ├── urls.py # Main URL routing

│ └── wsgi.py # WSGI configuration

├── users/ # User authentication app

│ ├── models.py # User-related models

│ ├── views.py # User authentication views

│ ├── serializers.py # User serializers

│ └── urls.py # User API endpoints

├── companies/ # Company management app

│ ├── models.py # Company model

│ ├── views.py # Company CRUD views

│ ├── serializers.py # Company serializers

│ └── urls.py # Company API endpoints

├── jobs/ # Job management app

│ ├── models.py # Job model

│ ├── views.py # Job CRUD views

│ ├── serializers.py # Job serializers

│ └── urls.py # Job API endpoints

├── applications/ # Job applications app

│ ├── models.py # Application model

│ ├── views.py # Application views

│ ├── serializers.py # Application serializers

│ └── urls.py # Application API endpoints

├── db.sqlite3  

├── manage.py # Django management script

└── README.md # Project documentation

7. API Endpoints

Authentication
POST /api/users/register/ - Register

POST /api/users/login/ - Login (get token)

POST /api/users/logout/ - Logout

Companies
GET /api/companies/ - List companies

POST /api/companies/ - Create company

Jobs
GET /api/jobs/ - List jobs

POST /api/jobs/ - Post job

Applications
POST /api/applications/ - Apply for job

GET /api/applications/ - View applications
