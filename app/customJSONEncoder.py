from bson import json_util
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict):
            return dict((k, self.default(v)) for k, v in obj.items() if v is not None)
        if isinstance(obj, list):
            return list((self.default(x) )for x in obj if x is not None)
        if isinstance(obj, object):
            return str(obj)
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return json_util.default(obj)