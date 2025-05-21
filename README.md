# README.md

# Streamlit Hello World App

This project is a simple Streamlit application that displays "Hello World". It is designed to demonstrate the use of Streamlit along with Docker and Gunicorn for deployment.

## Project Structure

```
streamlit-app
├── src
│   ├── app.py                # Main application file
│   └── tests
│       ├── __init__.py       # Test package initialization
│       └── test_app.py       # Unit tests for the application
├── Dockerfile                 # Dockerfile for building the application image
├── pyproject.toml            # Poetry configuration file
├── poetry.lock               # Locked dependencies for consistent installations
├── gunicorn.conf.py          # Gunicorn configuration settings
└── README.md                 # Project documentation
```

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd streamlit-app
   ```

2. **Install dependencies:**
   This project uses Poetry for dependency management. Install Poetry if you haven't already, then run:
   ```bash
   poetry install
   ```

3. **Build the Docker image:**
   ```bash
   docker build -t streamlit-app .
   ```

4. **Run the application:**
   You can run the application using Docker:
   ```bash
   docker run -p 8501:8501 streamlit-app
   ```

5. **Access the application:**
   Open your web browser and go to `http://localhost:8501` to see the "Hello World" message.

## Running Tests

To run the tests for this application, use the following command:
```bash
poetry run pytest src/tests
```

## License

This project is licensed under the MIT License.