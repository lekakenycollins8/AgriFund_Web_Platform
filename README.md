# AgriFund_Web_Platform
# AgriFund

AgriFund is a web platform designed to connect farmers with potential investors and provide a means for farmers to apply for loans to support their agribusiness projects. The platform allows farmers to list their projects, investors to express interest in projects, and facilitates loan applications.

## Features

- **Project Listings Page**: View all agribusiness projects listed on the platform.
- **Project Details Page**: Detailed view of a specific project, including descriptions, funding goals, current status, and investor interests.
- **Loan Application Form**: Farmers can apply for loans for their projects.
- **Express Interest Form**: Investors can express interest in projects.
- **Notification System**: Email notifications for farmers when an investor expresses interest in their project.

## Project Structure

- `models.py`: Contains the database models for Project, LoanApplication, InvestorInterest, and Notification.
- `forms.py`: Contains form classes for Project, LoanApplication, and InvestorInterest.
- `views.py`: Contains view functions for handling requests and rendering templates.
- `urls.py`: URL mappings for the app.
- `email_utils.py`: Utility functions for sending emails.
- `serializers.py`: contains model serializers for the API viewsets
- `api_views.py`: contains Class Based viewsets for handling API CRUD operations

## Models
- **BaseModel**: Holds the creation and update time for class instances
- **Project**: Holds details of agribusiness projects.
- **LoanApplication**: Holds details of loan applications by farmers.
- **InvestorInterest**: Holds details of investors interested in a project.
- **Notification**: Handles notifications sent to farmers.

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/lekakenycollins8/AgriFund_Web_Platform.git
    cd Agrifund_Web_Platform/Agrifund
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure email settings** in `Agrifund/settings.py`:
    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    EMAIL_USE_TLS = True
    ```

5. **Run database migrations**:
    ```sh
    python3 manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

8. **Access the application** at `http://127.0.0.1:8000/`.

## Usage

- **Landing Page**: Provides an overview and introduction to the platform.
- **Project Listings**: Displays all projects with an option to view details.
- **Project Details**: Shows detailed information about a project and forms for loan application and investor interest.
- **Loan Application**: Farmers can apply for loans by filling out the loan application form.
- **Express Interest**: Investors can express interest in a project by filling out the investor interest form.

## Example Project

Here's an example of a project you can submit via the form:

- **Project Name**: Sustainable Spinach Farming
- **Description**: This project aims to establish a sustainable spinach farming operation that utilizes eco-friendly farming practices. The goal is to produce high-quality spinach for local markets while minimizing environmental impact. Funding is required to purchase seeds, organic fertilizers, and irrigation equipment. The project will also invest in training local farmers on sustainable agriculture techniques.
- **Funding Goal**: $10,000
- **Current Status**: Open
- **Farmer Name**: John Doe
- **Farmer Email**: johndoe@example.com

## Contributing

We welcome contributions to improve AgriFund. Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Acknowledgements

Special thanks to ALX SE school and the Django community for their support and resources.

## Contact

For any inquiries or feedback, please contact [lekakenycollins8@gmail.com].
