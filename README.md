# Rule Engine API

This project implements a Rule Engine API using FastAPI, allowing users to create, combine, evaluate, and modify rules. The API is designed to work with a MongoDB database and includes a custom rule engine for processing complex logical expressions.

## API Documentation: [Postman](https://documenter.getpostman.com/view/31555061/2sAXxWZ9JG)

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create complex rules using logical expressions
- Combine multiple rules
- Evaluate rules against provided data
- Modify existing rules
- Attribute validation using a predefined catalog

## Tech Stack

- Python 3.9
- FastAPI
- MongoDB 
- Pydantic for data validation
- Pytest for testing


## Getting Started

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Satyam2192/rule-engine-api.git
   cd rule-engine-api
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv .venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your MongoDB connection:
   - Update the MongoDB connection string in `app/database.py` if needed.

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

6. Run the tests:
```
pytest tests/test_rule_engine.py
```
Output:
=========== test session starts ===========
platform linux -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/sk/Desktop/Zeotap/server
plugins: anyio-4.6.2.post1
collected 7 items                         

tests/test_rule_engine.py .......   [100%]

============ 7 passed in 0.12s ============

## Usage

The Rule Engine API allows you to create, combine, evaluate, and modify rules. Rules are represented as logical expressions and can be used to evaluate data against predefined criteria.

## API Endpoints

- `POST /rules`: Create a new rule
- `POST /combine_rules`: Combine multiple rules
- `POST /evaluate_rule`: Evaluate a rule against provided data
- `POST /modify_rule`: Modify an existing rule

For detailed API documentation, visit `http://localhost:8000/docs` after starting the server.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

