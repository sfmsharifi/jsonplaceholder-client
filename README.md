# JSONPlaceholder API Client

A Python application that interacts with the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) to fetch and display data about users, albums, and posts. The project includes a test suite to ensure the reliability of API interactions.

## Features
- Fetch user data
- Retrieve albums
- Access posts
- Includes unit tests using `pytest` and `requests-mock`
- Continuous Integration (CI) setup with GitHub Actions

## Technologies Used
- Python 3.10+
- Requests library
- Pytest for testing
- Requests-mock for mocking API responses
- GitHub Actions for CI/CD

## Getting Started

To set up the project locally, follow these instructions:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sfmsharifi/jsonplaceholder-client.git
   cd jsonplaceholder-client
   
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Runing the application**:
   ```bash
   python app.py
   
5. **Type checking**:
   ```bash
   mypy app.py
   
6. **Running tests**:
   ```bash
   pytest test_app.py
   
6. **Checking test coverage**:
   ```bash
   pytest --cov=app test_app.py
