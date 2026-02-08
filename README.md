# Python Flask API

A simple REST API built with Flask demonstrating Docker containerization.

## Features

- Health check endpoints
- Sample data API endpoint
- CORS support for cross-origin requests
- Environment variable configuration
- Docker containerization with health checks

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Health check with version info
- `GET /api/health` - Detailed health status
- `GET /api/data` - Sample data endpoint

## Docker

### Build

```bash
docker build -t python-api:latest .
```

### Run

```bash
docker run -p 5000:5000 python-api:latest
```

### Environment Variables

- `PORT` - Port to run on (default: 5000)
- `DEBUG` - Debug mode (default: False)
- `ENVIRONMENT` - Environment name (default: development)

## Testing

```bash
curl http://localhost:5000/
curl http://localhost:5000/api/health
curl http://localhost:5000/api/data
```
