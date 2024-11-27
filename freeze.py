from flask_frozen import Freezer
from flask import Flask, render_template
#from app1 import app1  # Import app1 blueprint (if it exists)
from app import app2_bp  # Import app2 blueprint from app.py

app = Flask(__name__)

# Register blueprints for app1 and app2 (both need to be available for freezing)
#app.register_blueprint(app1, url_prefix='/app1')  # Register app1 blueprint with a prefix
app.register_blueprint(app2_bp, url_prefix='/app2')  # Register app2 blueprint with a prefix

# Initialize Flask-Frozen
freezer = Freezer(app)

# Define any dynamic URL generators here if needed
@freezer.register_generator
def app2_index_generator():
    # If app2 has dynamic routes, add them here (e.g., for a specific ID or query parameter)
    yield '/app2/app2_index'  # Explicitly tell Flask-Frozen about app2_index route

@app.route('/')
def home():
    return render_template('index.html')

# Check if URL generators are working properly
for url in freezer.all_urls():
    print(url)


if __name__ == '__main__':
    freezer.freeze()  # Freeze the app into static files
