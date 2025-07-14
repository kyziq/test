# MindHive Assessment Zus Coffee Assistant

## Getting Started

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

2. Start the FastAPI backend server:

```bash
cd fastapi-backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

3. In a new terminal, start the Streamlit app:

```bash
streamlit run app.py
```

The chat interface will open in your browser at `http://localhost:8501`

### Using the Assistant

Once both servers are running, you can:

1. Open the Streamlit app in your browser
2. Start chatting with the assistant
3. Try sample questions like:
   - "Is there any outlets in Petaling Jaya?"
   - "I want to know more about Zus Mug?"
   - "What time does Zus Coffee SS2 open?"
   - "Calculate 2 + 3"

### Development Notes

- Always activate the virtual environment before running the application or installing new packages
- If you install new packages, update requirements.txt:
