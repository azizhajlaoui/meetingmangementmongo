import requests
import pytest

BASE_URL = "http://localhost:5000/api/meetings"

def test_create_meeting():
    data = {
        "mail": "test@example.com",
        "color": "red",
        "title": "Test Meeting",
        "start_time": "2024-03-08T12:00:00",
        "end_time": "2024-03-08T13:00:00",
        "id_meet": "test-meeting",
        "description": "This is a test meeting"
    }

    response = requests.post(f"{BASE_URL}/create_meeting", json=data)
    assert response.status_code == 201
    assert response.json()['message'] == 'Meeting created successfully'

def test_get_meeting():
    response = requests.get(f"{BASE_URL}/10")
    assert response.status_code == 200
    data = response.json()
    assert data["id_meet"] == "10"

def test_get_all_meetings():
    response = requests.get(f"{BASE_URL}/get_all_meetings")
    assert response.status_code == 200
    # data = response.json()
    # assert isinstance(data["meetings"], list)

def test_update_meeting():
    data = {
        "mail": "updated-test@example.com",
        "color": "aaa0aaa",
        "title": "Updated Meeting..",
        "start_time": "2024-03-08T14:00:00",
        "end_time": "2024-03-08T15:00:00",
        "description": "This is updated test meeting"
    }

    response = requests.put(f"{BASE_URL}/10", json=data)
    assert response.status_code == 200
    assert response.json()['message'] == 'Meeting updated successfully'

def test_delete_meeting():
    response = requests.delete(f"{BASE_URL}/test-meeting")
    assert response.status_code == 200
    assert response.json()['message'] == 'Meeting deleted successfully'
