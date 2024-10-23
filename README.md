# Flask Application

## Structure
```bash
├── app.py                   # Flask app that takes user input and displays a welcome message.
├── test_app                 # Unit tests for the Flask application.
├── requirements.txt         # Python dependencies
├── Dockerfile               # Instructions to build the Docker image
├── 
├── .github
│   └── workflows
│       └── ci.yml           # GitHub Actions CI pipeline for building and testing.
└── README.md                # Project overview and instructions

```
## How to Build and Run

### Local Development
1. Clone the repository.
```bash
https://github.com/darshanrw/CICD_midterm.git
```
2. Install the dependencies:
```bash
   pip install -r requirements.txt
```
3. Run the Flask application:
```bash
    python app.py
```
4. Open your browser and navigate to http://localhost:5000.

Docker:

1. Build the Docker image:
```bash
   docker build -t flask-app .
```

2. Run the Docker container:
```bash
   docker run -p 5000:5000 flask-app
```

3. Open your browser and navigate to `http://localhost:5000`.

### Steps to Test the CI Pipeline
GitHub Actions:
The CI pipeline runs automatically on every push or pull request to the main branch.

Build Phase: Installs dependencies and sets up the environment.
Test Phase: Runs unit tests using pytest. The pipeline fails if any test does not pass.

This will execute the tests defined in test_app.py, which includes:

test_homepage: Checks if the homepage loads and contains the input field.
test_welcome_message: Verifies that the welcome message is correctly displayed when a name is submitted.

### Pulling the Docker Image from the Registry
The Docker image is published to Docker Hub.

To pull the Docker image:
```bash
docker pull darshanrw/flask-app:latest
```

Run the pulled Docker image:
```bash
docker run -p 5000:5000 darshanrw/flask-app:latest
```

Navigate to http://localhost:5000 to access the application.




