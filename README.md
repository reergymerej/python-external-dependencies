# API Testing Demo

A minimal Flask API that demonstrates the challenge of testing code with external dependencies.

## The Problem

This Flask app fetches post data from an external API (JSONPlaceholder). The current implementation is "untestable" because:

- Tests require real API calls
- Tests are slow and unreliable
- Tests depend on external service availability
- Network issues break your test suite

## Running the App

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

3. Try it out:
```bash
curl http://localhost:5000/posts/1
```

## Running Tests (The Problem)

```bash
pytest test_app.py -v
```

**Note:** Tests make real API calls to jsonplaceholder.typicode.com making them slow and brittle.## The Solution

This project will be refactored to demonstrate dependency injection patterns that make the code fully testable without external dependencies.

## Project Structure

- `app.py` - Flask application with "untestable" API integration
- `test_app.py` - Tests that demonstrate the testing problem
- `requirements.txt` - Python dependencies