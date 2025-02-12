# Backend setup

This project is a simple web application built with Flask that generates QR codes from user-provided text. It provides a user-friendly interface to input text and download the generated QR code as an image.  This README includes detailed instructions on setting up the database, including creating a user, database, and running migrations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This Flask application allows users to quickly and easily generate QR codes. You simply enter the text you want to encode, and the application will generate the corresponding QR code, which you can then download. This is a useful tool for encoding URLs, contact information, or any other text-based data.

## Features

- Generates QR codes from user-provided text.
- Downloads the generated QR code as a PNG image.
- Simple and intuitive user interface.
- Database storage of QR code generation history (example - you can customize).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd YOUR_REPOSITORY_NAME
    ```

3.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```

4.  **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate    # For Windows
    ```

5.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file yet, create one:

    ```bash
    pip freeze > requirements.txt
    ```

## Database Setup (PostgreSQL Example)

These instructions use PostgreSQL as an example. Adapt as needed for your chosen database.

1.  **Install PostgreSQL:** If you don't have PostgreSQL installed, download and install it from the official website: [https://www.postgresql.org/](https://www.postgresql.org/)

2.  **Create a database user and database:**

    ```sql
    -- Connect to the postgres user (or a user with sufficient privileges)
    psql -U postgres

    -- Create a new user (replace 'your_username' and 'your_password')
    CREATE USER your_username WITH PASSWORD 'your_password';

    -- Create a new database (replace 'your_database_name')
    CREATE DATABASE your_database_name;

    -- Grant privileges to the user on the database
    GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;

    -- Connect to the newly created database
    \c your_database_name

    -- Create the necessary tables (run migrations - see below)
    ```

3.  **Configure Database URI:** Set the `DATABASE_URL` environment variable.  The format for PostgreSQL is:

    ```
    postgresql://your_username:your_password@host:port/your_database_name
    ```

    -   **.env file (Recommended):** Create a `.env` file in your project root and add:

    ```
    DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database_name
    SECRET_KEY=your_secret_key  # Generate a strong secret key
    ```

    Install `python-dotenv`:

    ```bash
    pip install python-dotenv
    ```

    In your `app.py`:

    ```python
    from dotenv import load_dotenv
    load_dotenv()
    ```

4.  **Migrations (Alembic Example):**

    ```bash
    Run `migrate.sh` file on the backend root directory
    ```

## How to Run

1.  **Activate the virtual environment:** (If not already activated)

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

3.  **Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in the terminal).**



## Frontend Setup (Example using npm and Vue.js)

1.  **Navigate to the frontend directory:**

    ```bash
    cd frontend  # Or the name of your frontend directory
    ```

2.  **Install frontend dependencies:**

    ```bash
    npm install  # Or yarn install if you use Yarn
    ```

3.  **Development Server (Optional):** If your frontend framework has a development server (like `npm run serve` for Vue.js or `npm start` for React), you can start it:

    ```bash
    npm run dev # Or the appropriate command for your framework
    ```

    This will usually run the frontend on a separate port (e.g., `http://localhost:8080`).

5.  **Integrating with Flask:**  Copy the contents of the `dist` or `build` directory (the output of the build command) into the `static` folder of your Flask project.  This is how Flask will serve your static files (including your built frontend application).

## How to Run

1.  **Activate the virtual environment:** (If not already activated)

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

3.  **Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in the terminal).**  Flask will serve your built frontend application from the `static` directory.

## Usage

(Same as before)

## Technologies Used

-   Flask
-   qrcode
-   PostgreSQL (Example)
-   Flask Migrate (Example)
-   [Frontend Framework/Library, e.g., Vue.js, React, or plain HTML/CSS/JS]
-   npm (or yarn)

## Project Structure
