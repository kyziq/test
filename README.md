# MindHive

## Virtual Environment Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setting Up Virtual Environment

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt)

2. Navigate to the fastapi-backend directory:

```bash
cd fastapi-backend
```

3. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` and data files will be created for the ZUS Coffee API at /data directory.

### Deactivating Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

## Note

- Always activate the virtual environment before running the application or installing new packages
- If you install new packages, update requirements.txt:

```bash
pip freeze > requirements.txt
```
