from flask import Flask
from common import mongo
from routes import meeting_bp
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/mycalendar"
app.register_blueprint(meeting_bp, url_prefix='/api/meetings')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)