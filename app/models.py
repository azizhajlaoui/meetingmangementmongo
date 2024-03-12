from flask import current_app

class Meeting:
    def __init__(self, _id, id_meet, start_hour, end_hour, description, mail, title, color, collection=None):
        self._id = _id
        self.id_meet = id_meet
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.description = description
        self.mail = mail
        self.title = title
        self.color = color
        self.collection = collection

    def to_dict(self):
        return {
            '_id': self._id, 
            'id_meet': self.id_meet,
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'description': self.description,
            'mail': self.mail,
            'title': self.title,
            'color': self.color
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data.get('_id'),
            id_meet=data.get('id_meet'),
            start_hour=data.get('start_hour'),
            end_hour=data.get('end_hour'),
            description=data.get('description'),
            mail=data.get('mail'),
            title=data.get('title'),
            color=data.get('color')
        )

    def save_to_db(self):
        # Get the MongoDB collection from the current app context
        meetings_collection = current_app.mongo.db.meetings
        # Save the meeting to the MongoDB collection
        meetings_collection.insert_one(self.to_dict())
