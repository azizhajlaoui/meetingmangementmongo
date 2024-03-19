from bson import ObjectId,json_util
from models import Meeting
from flask import Blueprint, request, jsonify
from common import mongo 
meeting_bp = Blueprint('meeting_bp', __name__)

 
@meeting_bp.route('/create_meeting', methods=['POST'])
def create_meeting():
    try:
    # Use the mongo object to interact with the database
        meetings_collection = mongo.db.meetings
        meeting = {
            'mail': request.json['mail'],
            'color': request.json['color'],
            'title': request.json['title'],
            'start_time': request.json['start_time'],
            'end_time': request.json['end_time'],
            'id_meet': request.json['id_meet'],
            'description': request.json['description'],
        }
        result = meetings_collection.insert_one(meeting)

        return jsonify({'message': 'Meeting created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

 
@meeting_bp.route('/<string:id_meet>', methods=['PUT'])
def update(id_meet):
    if request.method == 'PUT':
        try:
            # Get data from the request
            meeting_data = request.json  # Get data from the request JSON

            # Assuming 'meetings' is the name of your MongoDB collection
            meetings_collection = mongo.db.meetings
            existing_meeting = meetings_collection.find_one({'id_meet': id_meet})

            if existing_meeting:
                # Extract data using correct syntax
                mail = meeting_data.get('mail', existing_meeting['mail'])
                color = meeting_data.get('color', existing_meeting['color'])
                title = meeting_data.get('title', existing_meeting['title'])
                start_time = meeting_data.get('start_time', existing_meeting['start_time'])
                end_time = meeting_data.get('end_time', existing_meeting['end_time'])
                description = meeting_data.get('description', existing_meeting['description'])

                # Update the meeting document in the MongoDB collection
                result = meetings_collection.update_one(
                    {'id_meet': id_meet},  # Use id_meet as the identifier
                    {'$set': {
                        'start_time': start_time,
                        'end_time': end_time,
                        'description': description,
                        'mail': mail,
                        'title': title,
                        'color': color,
                        'id_meet': id_meet
                    }}
                )

                if result.modified_count > 0:
                    return jsonify({"message": "Meeting updated successfully"}), 200
                else:
                    return jsonify({"error": "Meeting not found"}), 404
            else:
                return jsonify({"error": "Meeting not found"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 400

 
@meeting_bp.route('/<string:id_meet>', methods=['GET'])
def get_meeting(id_meet):
    try:
        # Assuming 'meetings' is the name of your MongoDB collection
        meetings_collection = mongo.db.meetings
        meeting = meetings_collection.find_one({'id_meet': id_meet})

        if meeting:
            return jsonify({
                "id_meet": meeting['id_meet'],
                "start_time": meeting['start_time'],
                "end_time": meeting['end_time'],
                "description": meeting['description'],
                "mail": meeting['mail'],
                "title": meeting['title'],
                "color": meeting['color']
            }), 200
        else:
            return jsonify({"error": "Meeting not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 404


 
@meeting_bp.route('/get_all_meetings', methods=['GET'])
def get_all_meetings():
    try:
        meetings_collection = mongo.db.meetings

        meetings = meetings_collection.find()

        meetings_list = json_util.dumps(list(meetings))

        return meetings_list, 200, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

 
@meeting_bp.route('/<string:id_meet>', methods=['DELETE'])
def delete_meeting(id_meet):
    try:
        # Assuming 'meetings' is the name of your MongoDB collection
        result = mongo.db.meetings.delete_one({'id_meet': id_meet})

        if result.deleted_count > 0:
            return jsonify({"message": "Meeting deleted successfully"}), 200
        else:
            return jsonify({"error": "Meeting not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400    