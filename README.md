# Penny America

## Overview
Penny America is a robust financial management application designed to help users manage and track their personal finances. The application integrates with the **Plaid API** (in the sandbox environment) to securely retrieve and categorize user expense transactions from linked financial institutions. The backend is built using **Django**, with RESTful APIs managed via **Django Ninja**. The app also features JWT authentication and admin-level security.

The project is designed to run on **AWS RDS** and **EC2** for production, with **PostgreSQL** used locally for development. 

## Table of Contents
- [Penny America](#penny-america)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [System Architecture](#system-architecture)
  - [Setup](#setup)
    - [Local Development](#local-development)
      - [Prerequisites:](#prerequisites)
      - [Steps:](#steps)
  - [Environment Variables](#environment-variables)
  - [API Documentation](#api-documentation)
    - [Main API Endpoints:](#main-api-endpoints)
  - [Security](#security)
  - [License](#license)
  - [Contributors License Agreement (CLA)](#contributors-license-agreement-cla)

## Features
- **User Authentication**: Implements JWT-based authentication for secure login and access to user-specific data.
- **Transaction Management**: Retrieves user transactions through the Plaid API and filters them to display only relevant expense transactions.
- **Admin Privileges**: Admin users can manage other users and view or edit sensitive data.
- **PostgreSQL Database**: Uses AWS RDS in production and PostgreSQL in local development.
- **Plaid Integration**: Plaid API is integrated for fetching and categorizing financial transactions (Sandbox only).

## Tech Stack
- **Backend**: Django, Django Ninja (for API management), Python
- **Database**: PostgreSQL (AWS RDS in production)
- **Authentication**: JWT (JSON Web Tokens)
- **API Integration**: Plaid (Sandbox environment)
- **Hosting**: AWS EC2

## System Architecture
The architecture is divided into the following components:
1. **Django Application**: Handles all backend logic, including routing, database operations, and authentication.
2. **PostgreSQL Database**: Local PostgreSQL for development; AWS RDS for production.
3. **Plaid Integration**: Manages communication with Plaid’s API to fetch user transactions securely.
4. **Admin Module**: Provides privileged access for admins to manage users and data.
5. **Security Layer**: JWT-based authentication and role-based access control for secure access to resources.

## Setup

### Local Development
#### Prerequisites:
- Python 3.9+
- PostgreSQL
- Plaid account (Sandbox)

#### Steps:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up local PostgreSQL:
   - Create a PostgreSQL database and user:
     ```sql
     CREATE DATABASE your_database;
     CREATE USER your_user WITH PASSWORD 'your_password';
     GRANT ALL PRIVILEGES ON DATABASE your_database TO your_user;
     ```

5. Configure environment variables (see [Environment Variables](#environment-variables)).

6. Apply migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables
The following environment variables need to be configured for both local development and production environments:

- `PLAID_ENV`: Set to `Sandbox` for local development.
- `PLAID_CLIENT_ID`: Your Plaid client ID.
- `PLAID_SECRET`: Your Plaid secret.
- `DB_NAME`: PostgreSQL database name.
- `DB_USER`: PostgreSQL user.
- `DB_PASSWORD`: PostgreSQL password.
- `DB_HOST`: Database host (`localhost` for development).
- `DB_PORT`: PostgreSQL port (default is `5432`).
- `SECRET_KEY`: Django’s secret key for encryption.
- `ALLOWED_HOSTS`: Allowed hosts (set this to your domain).
- `DEBUG`: Set to `True` in development, `False` in production.

## API Documentation
API documentation is available via **Swagger** (powered by Django Ninja) at:

- **Local**: `http://127.0.0.1:8000/api/v0/docs/`
- **Production**: `https://production-domain/api/v0/docs/`

### Main API Endpoints:
- **/accounts/login/**: User login, returns a JWT token.
- **/plaid/transactions/**: Fetch user expense transactions from Plaid.
- **/admin/**: Admin-level operations for managing users and data.

## Security
- **JWT Authentication**: All user-specific routes require a valid JWT token for access.
- **Admin Role**: Certain routes (e.g., user management) are restricted to admin users only. Admin routes are protected by the `require_admin` decorator in `security.py`.

## License
This application is the property of Victor Bondaruk. As the owner, [Victor Bondaruk](https://github.com/SylverVB) retains all rights to the application.

## Contributors License Agreement (CLA)
By making a contribution to this project, you agree to the following terms and conditions for your contributions:

1. You grant the owner, Victor Bondaruk, a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable license to use, distribute, and modify your contributions as part of this project.
2. You represent that you are legally entitled to grant the above license.
3. You agree to promptly notify the owner of any facts or circumstances of which you become aware that would make these representations inaccurate in any respect.