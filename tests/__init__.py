# # tests/__init__.py
# import sys
# sys.path.append('/home/mahajlaoui/meetingmangementmongo')
# from ..common import create_mongo_connection

# import pytest

# @pytest.fixture
# def app():
#     app=create_mongo_connection()
#     yield app

# @pytest.fixture
# def client(app):
#     return app.test_client()