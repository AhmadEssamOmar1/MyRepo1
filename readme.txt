Automated Testing Script for MCIT Careers Platform
This repository contains a Python script that uses SeleniumBase to perform automated testing on the MCIT Careers website. The script automates user registration, browsing job postings, and applying for a job.

Features
Dynamic Input Generation:
Generates random user data such as names, email addresses, and strong passwords.
Website Interaction:
Tests critical workflows including registration and job application.
Reporting:
Produces detailed HTML reports and logs for debugging and analysis.
Headless Execution:
Runs browser interactions in the background without requiring a GUI.
Requirements
Python: Version 3.7 or later.
SeleniumBase: Install the testing framework via pip:
bash
Copy code
pip install seleniumbase
Script Overview
Random Data Generation:

Functions generate_random_text, generate_email, and generate_password create random inputs for the registration form.
Test Workflow:

Navigates to the website.
Accepts cookies.
Completes the registration form with generated data.
Verifies successful navigation to specific pages using URL assertions.
Simulates applying for a job by interacting with relevant buttons.
Execution:

The script uses pytest for execution and reporting.