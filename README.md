# Studypal

Studypal is an academic app designed for students and elite learners. It provides authentication and user management using Django and Django REST Framework (DRF), with JWT-based authentication powered by `djangorestframework_simplejwt`.

## Features
- User authentication (Signup, Login, Logout)
- JWT-based authentication
- API integration for frontend authentication

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd studypal
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- `POST http://127.0.0.1:8000/login` – Login with credentials and receive a JWT token.
- `POST http://127.0.0.1:8000/register` – Create a new user account.
- `POST http://127.0.0.1:8000/token/refresh` – Refresh an expired JWT token.

## Technologies Used
- **Django**: Backend framework
- **Django REST Framework (DRF)**: API development
- **SimpleJWT**: JWT-based authentication

## Contributing
Feel free to contribute by submitting issues and pull requests.

## Author
**Kehinde Waris Akanmu**  
GitHub: [war-riz](https://github.com/war-riz)  
Currently working at **ACE (African Centre of Excellence)**

## License
This project is licensed under the MIT License.
