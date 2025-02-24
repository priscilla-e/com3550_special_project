# Server

A Flask-based web server that provides an AI opponent for Tic-Tac-Toe using OpenAI's GPT models. This server is designed to demonstrate API development and AI integration.

## Project Structure
```
server/
├── app/
│   ├── gpt/
│   │   ├── __init__.py    # API Blueprint initialization
│   │   └── routes.py      # API endpoints
│   │   └── utils.py       # API utilities
│   ├── extensions.py      # Flask extensions (CORS, OpenAI)
│   └── __init__.py        # App factory
├── .flaskenv              # Flask environment variables
├── .env.example          # Example environment template
├── requirements.txt      # Project dependencies
├── config.py              # App configuration file
└── run.py               # Server entry point
```

## API Endpoints

- `GET /gpt/` - Health check endpoint
- `POST /gpt/move` - Get AI's next move
  - Request body: `{ "board": [[...]], "model": "gpt-3.5-turbo-1106" }`
  - Response: JSON with row and column indices for the AI's move

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**Unix/MacOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` file with your settings:
```
HOST=0.0.0.0
PORT=2000
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Server

### Development Mode

Development mode includes:
- Debug mode enabled
- Auto-reload on code changes
- Detailed error messages

```bash
python run.py
```

### Production Mode

To run in production mode, set the environment variable:

```bash
export FLASK_ENV=production
python run.py
```

Production mode features:
- Uses Waitress WSGI server
- Optimized for performance
- Disabled debug mode
- Enhanced security

## Technical Details

- **Flask**: Web framework for the API
- **OpenAI**: GPT integration for AI moves
- **CORS**: Enabled for cross-origin requests
- **Waitress**: Production WSGI server
- **Environment Variables**: Configuration management

## Notes for Students

1. The server uses a Blueprint pattern for API organization
2. CORS is configured to allow requests from any origin (*)
3. The AI opponent uses GPT-3.5-Turbo with temperature=0.4 for consistent moves
4. JSON response format is enforced for API consistency
5. Error handling and input validation are implemented

## Common Issues

- Ensure your OpenAI API key is valid and set in `.env`
- Virtual environment must be activated before running the server
- Default port is 2000; ensure it's not in use
- Check CORS settings if connecting from a frontend application