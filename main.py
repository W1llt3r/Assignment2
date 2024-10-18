from app import flask_app
from dotenv import load_dotenv
load_dotenv()

flask_app.run(host="0.0.0.0", port=5000)
