# Phishing Project - Bottle Web Application

A simple web application built with Python Bottle framework that serves XHTML pages.

## Project Structure

```
Phishing Project/
├── app.py              # Main Bottle application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/         # XHTML template files
│   ├── index.xhtml    # Home page
│   └── page2.xhtml    # Second page
└── static/           # Static assets (CSS, JS, images)
```

## Setup Instructions

1. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```powershell
   python app.py
   ```

3. **Access the application:**
   - Home page: http://localhost:8080/
   - Second page: http://localhost:8080/page2

## Features

- Serves two XHTML pages with proper DOCTYPE declarations
- Static file serving for CSS, JavaScript, and images
- Development server with auto-reload functionality
- Clean, responsive design with navigation between pages

## Development

- The application runs on `localhost:8080` by default
- Debug mode is enabled for development
- Auto-reload is enabled - the server will restart when you make changes to the code
- Press `Ctrl+C` to stop the server

## Adding New Pages

To add a new page:

1. Create a new XHTML file in the `templates/` directory
2. Add a new route in `app.py`:
   ```python
   @app.route('/newpage')
   def newpage():
       return static_file('newpage.xhtml', root=TEMPLATE_DIR)
   ```

## Static Assets

Place CSS, JavaScript, images, and other static files in the `static/` directory. They will be accessible at `/static/filename`.
