from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """A musician & app user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
    

def connect_to_db(flask_app, db_uri="postgresql:///mpp", echo=False): 
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    ###can change "echo" to True if you want to see a much more verbose readout
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets  annoying
    # this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app)