# Student Management System

This is a Django-based Student Management System that allows administrators, teachers, and students to manage courses, results, and announcements.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/K-Ananthamoorthy/student_management_system.git
    cd student_management_system
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/admin` to access the admin interface.

## Usage

- Admins can manage users, courses, results, and announcements through the Django admin interface.
- Teachers can add and edit students, create announcements, and manage results.
- Students can view their courses, results, and recent announcements.

## Features

- **User Management**: Custom user model with different user types (Admin, Teacher, Student).
- **Course Management**: Admins and teachers can create and manage courses.
- **Result Management**: Teachers can add and edit results for students.
- **Announcements**: Teachers can create announcements for their courses.
- **Dashboards**: Separate dashboards for students and teachers.

## Project Structure

- `communication/`: Handles communication-related models and views.
- `core/`: Core functionality including user authentication and dashboards.
- `courses/`: Manages courses, results, and announcements.
- `student_management_system/`: Project settings and configurations.
- `templates/`: HTML templates for rendering views.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.