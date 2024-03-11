# meetingmangementmongo/tests/test_routes.py
from flask import Flask,Blueprint
from flask_pymongo import PyMongo
from bson import ObjectId
import pytest

# import sys
# print(sys.path)

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_db'  # Use a test database
    mongo = PyMongo(app)
    # meeting_bp = Blueprint('meeting_bp', __name__)
    # app.register_blueprint(meeting_bp, url_prefix='/api/meetings')

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_meeting(client):
    # Implement test for creating a meeting
    response = client.post('/api/meetings/create_meeting', json={
        "mail": "test@example.com",
        "color": "red",
        "title": "Test Meeting",
        "start_time": "2024-03-08T12:00:00",
        "end_time": "2024-03-08T13:00:00",
        "id_meet": "test-meeting",
        "description": "This is a test meeting"
    })
    assert response.status_code == 201  # Check if the meeting was created successfully

def test_get_meeting(client):
    # Implement test for getting a meeting
    response = client.get('/api/meetings/3')
    assert response.status_code == 200  # Check if the meeting was retrieved successfully
    data = response.get_json()
    assert data["id_meet"] == "test-meeting"

def test_get_all_meetings(client):
    # Implement test for getting all meetings
    response = client.get('/api/meetings/get_all_meetings')
    assert response.status_code == 200  # Check if the request was successful
    data = response.get_json()
    assert isinstance(data["meetings"], list)

def test_update_meeting(client):
    # Implement test for updating a meeting
    response = client.put('/api/meetings/test-meeting', json={
        "mail": "updated-test@example.com",
        "color": "blue",
        "title": "Updated Test Meeting",
        "start_time": "2024-03-08T14:00:00",
        "end_time": "2024-03-08T15:00:00",
        "description": "This is an updated test meeting"
    })
    assert response.status_code == 200  # Check if the meeting was updated successfully

def test_delete_meeting(client):
    # Implement test for deleting a meeting
    response = client.delete('/api/meetings/test-meeting')
    assert response.status_code == 200  # Check if the meeting was deleted successfully
