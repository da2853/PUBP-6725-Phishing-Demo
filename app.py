from bottle import Bottle, static_file, abort
import os

app = Bottle()

@app.route('/')
def index():
    """Root route - can redirect to a default page or show a landing page"""
    return "<h1>Phishing Project</h1><p>Available routes:</p><ul><li><a href='/edstem/'>/edstem/</a></li><li><a href='/outlook/'>/outlook/</a></li></ul>"

@app.route('/edstem/')
@app.route('/edstem/index.html')
def edstem_page():
    """Serve the EdStem phishing page"""
    print("Serving EdStem HTML page")
    try:
        return static_file('index.html', root='./edstem/')
    except:
        abort(404, "EdStem page not found")

@app.route('/outlook/')
@app.route('/outlook/index.html') 
def outlook_page():
    """Serve the Outlook phishing page"""
    print("Serving Outlook HTML page")
    try:
        return static_file('index.html', root='./outlook/')
    except:
        abort(404, "Outlook page not found")

@app.route('/edstem/<filename>')
def edstem_static(filename):
    """Serve static files from the edstem directory (like logo.svg)"""
    return static_file(filename, root='./edstem/')

@app.route('/outlook/<filename>')
def outlook_static(filename):
    """Serve static files from the outlook directory"""
    return static_file(filename, root='./outlook/')

@app.route('/static/<filename>')
def server_static(filename):
    """Serve static files from the static directory"""
    return static_file(filename, root='./static/')

# Handle subdirectories in static folders if needed
@app.route('/edstem/<filepath:path>')
def edstem_deep_static(filepath):
    """Serve nested files from edstem directory"""
    return static_file(filepath, root='./edstem/')

@app.route('/outlook/<filepath:path>')
def outlook_deep_static(filepath):
    """Serve nested files from outlook directory"""
    return static_file(filepath, root='./outlook/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting server on port {port}")
    print("Available routes:")
    print("  http://localhost:{}/edstem/".format(port))
    print("  http://localhost:{}/outlook/".format(port))
    app.run(host='0.0.0.0', port=port, debug=True)