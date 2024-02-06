# Contract Testing with Pact and pact-python

This project demonstrates how to perform contract testing using Pact and the pact-python library for a scenario involving a Dashboard service and an Employee service.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Running Tests](#running-tests)

## Introduction

Contract testing is a method to ensure that interactions between different services are consistent and do not break when changes occur. This project uses the Pact framework and the pact-python library to create, manage, and verify contracts between a Dashboard service (consumer) and an Employee service (provider).

## Getting Started

### Prerequisites

Make sure you have Python and pip installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/contract-testing-pact-python.git
    cd contract-testing-pact-python
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

- `contracts`
  - `consumer`
    - `test_dashboard.json`: Consumer contract storage for the Dashboard service.
  - `provider`
    - `test_employee.json`: Provider contract test conditions for the Employee service.

- `tests`
  - `consumer`
    - `test_dashboard.py`: Consumer contract test cases for the Dashboard service.
  - `provider`
    - `test_employee.py`: Provider contract test cases for the Employee service.

## Running Tests

To run the contract tests, use the following commands:

```bash
python tests/consumer/test_dashboard.py
python tests/provider/test_employee.py
