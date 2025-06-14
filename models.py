from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Get the database credentials
with open('sensitive.json', 'r') as f:
    pg_info = json.load(f)['postgres']

# Create the link to the database for this app
database_uri_string = f'postgresql://{pg_info['username']}:{pg_info['password']}@localhost:{pg_info['port']}/{pg_info['database']}'

# Configure the app database_uri_string
app.confi['SQLALCHEMY_DATABASE_URI'] = database_uri_string

# Create an instance of the SQLAlchemy database
db = SQLAlchemy(app)

# User table
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    # todo: At some point do some validation to enforce a minimum length 
    username = db.Column(db.String(64), nullable=False, unique=True)
    # todo: At some point do some validation to enforce a minimum length
    password = db.Column(db.String(64), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    
    # def __init__(self, username, password, created_at, updated_at):
    #     super().__init__()
    #     self._username = username
    #     self._password = password
    #     self._created_at = created_at
    #     self._updated_at = updated_at
        
    def __repr__(self):
        return f'The account with username "{self._username}" was created at {self._created_at}'


# Songs table
class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    artist = db.Column(db.String(64), nullable=False)
    # Since there are singles, this must be nullable
    album = db.Column(db.String(64), nullable=True)
    # We might not know the release date
    release_date = db.Column(db.DateTime, nullable=True)
    # These refer to the actual record in the database
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    # todo: Do we want to track the actual user who updated, or added this record?
    # These should reference their id's
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Album table
class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    artist = db.Column(db.String(64), nullable=False)
    # We might not know the release date
    release_date = db.Column(db.DateTime, nullable=True)
    # These refer to the actual record in the database
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    # todo: Do we want to track the actual user who updated, or added this record?
    # These should reference their id's
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Artist table
class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    # These refer to the actual record in the database
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    # todo: Do we want to track the actual user who updated, or added this record?
    # These should reference their id's
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
# Each user will have their library
class Library(db.Model):
    __tablename__ = 'library'
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    
    # todo: create a composite primary key

# Each user can have a series of libraries
class Playlist(db.Model):
    __tablename__ = 'playlist'
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(64), nullable=False, unique=True)
    song = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    
    # todo: create a composite primary key
    