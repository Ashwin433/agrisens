# AgriSens - Smart Agriculture Recommendation System

AgriSens is a Django-based web application that provides intelligent crop recommendations and weather forecasting for farmers. The system uses machine learning models to suggest the best crops based on soil conditions and provides weather forecasts to aid in agricultural planning.

## Live Demo
Check out the live application here: [https://agrisens-1-z158.onrender.com/](https://agrisens-1-z158.onrender.com/)

## Features

- **Crop Recommendation**: Get AI-powered crop suggestions based on soil parameters
- **Weather Forecast**: Access accurate weather predictions for better farming decisions
- **User Authentication**: Secure user accounts with role-based access
- **Responsive Design**: Works on both desktop and mobile devices

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**:
   ```bash
   git clone [your-repository-url]
   cd agrisens
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install psycopg2-binary scikit-learn pandas numpy
   ```

4. **Set up the database**:
   - Create a PostgreSQL database named `agri_db`
   - Update database settings in `agrisens/settings.py` if needed

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

```
agrisens/
├── agrisens/             # Project configuration
├── recommendation/       # Crop recommendation app
├── users/                # User authentication app
├── weather_forecast/     # Weather forecasting app
├── static/               # Static files (CSS, JS, images)
└── templates/            # HTML templates
```

## Configuration

Copy `.env.example` to `.env` and update the environment variables as needed.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [scikit-learn](https://scikit-learn.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Support

For support, please open an issue in the repository or contact the maintainers.
