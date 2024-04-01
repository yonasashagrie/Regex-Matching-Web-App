# Regex-Matching-Web-App
## Flask Regex Web App

This is a simple Flask web application that allows users to input a test string and a regular expression pattern. It then finds and displays all matches of the regular expression pattern within the test string.

Additionally, the application provides a basic email validation feature, where users can input an email address, and it checks if the email contains both '@' and '.' characters.

## File Structure
app.py: Contains the Flask application code with routes for rendering templates and processing form submissions.

templates/: Directory containing HTML templates used by the application.

index.html: Template for the homepage.

results.html: Template for displaying regex pattern matching results.

validate_email.html: Template for displaying email validation results.

requirements.txt: File listing the Python dependencies required by the application.

## Dependencies
### The application requires the following Python packages:

Flask: A lightweight WSGI web application framework.

Jinja2: A modern and designer-friendly templating engine for Python.

Werkzeug: A comprehensive WSGI web application library.

These dependencies are listed in the requirements.txt file.