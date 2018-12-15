# config=utf-8
import sys
import os
from app import app
from app.api.user_api import Token
from app.api.mine_api import Mine
from app.api.activities_api import Activity
from app.api.join_api import Join
from flask_cors import CORS
from flask_script import Manager, Server
from flask_restful import Api
sys.path.append(os.getcwd())

if __name__ == '__main__':
    CORS(app)
    api = Api(app)
    api.add_resource(Token, "/api/token")
    api.add_resource(Mine, "/api/mine")
    api.add_resource(Activity, "/api/activity")
    api.add_resource(Join, "/api/join")
    manager = Manager(app)
    manager.add_command("runserver", Server(use_debugger=True))
    manager.run()
