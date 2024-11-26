from app import create_app  # Import the create_app function from __init__.py

# Create the Flask application instance
app = create_app()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  #debug for development, False for production