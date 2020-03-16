# retrieves app from app dir
from app import create_app

app = create_app()

# runs our application
if __name__ == '__main__':
    app.run()
