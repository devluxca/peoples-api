import os
base_project_dir = os.path.abspath(os.path.dirname(__file__))

class Database(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_project_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False