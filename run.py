from app import create_app

# Create instance of flask app
app = create_app()

# create_app() is the factory function in app/__init__.py that initializes and configures the app. It allows for better flexibility and scalability, especially in larger applications.
if __name__ == "__main__":
    app.run(debug=True)