from bson import ObjectId
from models import Meeting
from flask import Blueprint, request, jsonify
from common import mongo 
meeting_bp = Blueprint('meeting_bp', __name__)

 
@meeting_bp.route('/create_meeting', methods=['POST'])
def create_meeting():
    try:
    # Use the mongo object to interact with the database
        meeting = {
            '_id':None,
            'mail': request.json['mail'],
            'color': request.json['color'],
            'title': request.json['title'],
            'start_time': request.json['start_time'],
            'end_time': request.json['end_time'],
            'id_meet': request.json['id_meet'],
            'description': request.json['description'],
        }
        result = mongo.insert_one(meeting)

        return jsonify({'message': 'Meeting created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

 
@meeting_bp.route('/<string:id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        try:
            # Get data from the request
            meeting_data = request.get_json()
            start_hour = meeting_data['start_hour']
            end_hour = meeting_data['end_hour']
            description = meeting_data['description']
            mail = meeting_data['mail']
            title = meeting_data['title']
            color = meeting_data['color']

            # Update the meeting document in the MongoDB collection
            result = mongo.db.update_one(
                {'_id': ObjectId(id)},
                {'$set': {
                    'start_hour': start_hour,
                    'end_hour': end_hour,
                    'description': description,
                    'mail': mail,
                    'title': title,
                    'color': color
                }}
            )

            if result.modified_count > 0:
                return jsonify({"message": "Meeting updated successfully"}), 200
            else:
                return jsonify({"error": "Meeting not found"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
 
@meeting_bp.route('/<string:id>', methods=['GET'])
def get_meeting(id):
    try:
        # Retrieve the meeting document by its ID
        meeting = mongo.db.find_one({'_id': ObjectId(id)})

        if meeting:
            return jsonify({
                "id": str(meeting['_id']),
                "start_hour": meeting['start_hour'],
                "end_hour": meeting['end_hour'],
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
        # Assuming you have a 'meetings' collection in your MongoDB
        meetings_collection = mongo.db.meetings

        # Find all documents in the 'meetings' collection
        meetings = meetings_collection.find()

        # Convert the MongoDB cursor to a list for easier JSON serialization
        meetings_list = list(meetings)

        return jsonify({"meetings": meetings_list})

    except Exception as e:
        return jsonify({"error": str(e)})

 
@meeting_bp.route('/<string:id>', methods=['DELETE'])
def delete_meeting(id):
    try:
        # Delete the meeting document from the MongoDB collection
        result = mongo.db.delete_one({'_id': ObjectId(id)})

        if result.deleted_count > 0:
            return jsonify({"message": "Meeting deleted successfully"}), 200
        else:
            return jsonify({"error": "Meeting not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400





    