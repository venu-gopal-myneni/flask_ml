from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.config import Config

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from api.gets.routes import gets
    from api.posts.routes import posts

    app.register_blueprint(gets)
    app.register_blueprint(posts)


    return app
