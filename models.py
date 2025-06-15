from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
import json
from werkzeug.security import generate_password_hash, check_password_hash

# Get the database credentials
with open('sensitive.json', 'r') as f:
    pg_info = json.load(f)['postgres']

# Create the link to the database for this app
database_uri_string = f'postgresql://{pg_info['username']}:{pg_info['password']}@localhost:{pg_info['port']}/{pg_info['database']}'

# Configure the app database_uri_string
app.confi['SQLALCHEMY_DATABASE_URI'] = database_uri_string

# Create an instance of the SQLAlchemy database
db = SQLAlchemy(app)

# ! Commenting out for right now, so I can run the app without worrying about backend errors

# User table
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     # todo: At some point do some validation to enforce a minimum length 
#     username = db.Column(db.String(64), nullable=False, unique=True)
#     # todo: At some point do some validation to enforce a minimum length
#     password_hash = db.Column(db.String(128), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
    
    
#     # * Password operations
    
#     @property
#     def password(self):
#         raise AttributeError('"password" is not a readable attribute')
    
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
        
#     # Check if the password entered actually matches
#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)
    
    
#     # * Creating the various back references to the tables across the database
    
#     # * song
#     # User can have added/created many songs
#     songs_added = db.relationship('Song', backref='song_creator', foreign_keys='Song.created_by')
#     # User can have updated many songs
#     songs_updated = db.relationship('Song', backref='song_updator', foreign_keys='Song.updated_by')
    
#     # * album
#     # User can have added/created many albums
#     albums_added = db.relationship('Album', backref='album_creator', foreign_keys='Album.created_by')
#     # User can have updated many albums
#     albums_updated = db.relationship('Album', backref='album_updator', foreign_keys='Album.updated_by')
    
#     # * artist
#     # User can have added/created many albums
#     artists_added = db.relationship('Artist', backref='artist_creator', foreign_keys='Artist.created_by')
#     # User can have updated many albums
#     artists_updated = db.relationship('Artist', backref='artist_updator', foreign_keys='Artist.updated_by')
    
#     # * library
#     # User can have 1 library
#     library = db.relationship('Library', backref='owner', uselist=False)
    
#     # * playlist
#     # User can have added/created many playlists
#     playlists_created = db.relationship('Playlist', backref='playlist_creator', foreign_keys='Playlist.created_by')
#     # User can have updated many albums
#     playlists_updated = db.relationship('Playlist', backref='playlist_updator', foreign_keys='Playlist.updated_by')
        
#     def __repr__(self):
#         return f'The account with username "{self._username}" was created at {self._created_at}'


# # Songs table
# class Song(db.Model):
#     __tablename__ = 'song'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64), nullable=False)
#     artist = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
#     # Since there are singles, this must be nullable
#     album = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=True)
#     # We might not know the release date
#     release_date = db.Column(db.DateTime, nullable=True)
#     # These refer to the actual record in the database
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
#     # todo: Do we want to track the actual user who updated, or added this record?
#     # These should reference their id's
#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    

# # Album table
# class Album(db.Model):
#     __tablename__ = 'album'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64), nullable=False)
#     artist = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
#     # We might not know the release date
#     release_date = db.Column(db.DateTime, nullable=True)
#     # These refer to the actual record in the database
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
#     # These should reference their id's
#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
#     # * one-to-many w/song
#     songs = db.relationship('Song', backref='album')

# # Artist table
# class Artist(db.Model):
#     __tablename__ = 'artist'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     # These refer to the actual record in the database
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
#     # todo: Do we want to track the actual user who updated, or added this record?
#     # These should reference their id's
#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
#     # * one-to-many w/song
#     songs = db.relationship('Song', backref='artist')
    
#     # * one-to-many w/album
#     albums = db.relationship('Album', backref='artist')
    
# # Each user will have their library
# class Library(db.Model):
#     __tablename__ = 'library'
#     id = db.Column(db.integer, unique=True)
#     user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     song = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
#     # These refer to the actual record in the database
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
    
#     # todo: create a composite primary key
#     __table_args__ = (
#         PrimaryKeyConstraint('user', 'song')
#     )
    
#     # * many-to-one w/user
#     users = db.relationship('User', backref='library')    
    
#     # * many-to-one w/library
#     songs = db.relationship('Song', backref='library')

# # Each user can have a series of libraries
# class Playlist(db.Model):
#     __tablename__ = 'playlist'
#     user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     # This shouldn't be a unique column for two reasons: two users can use the same name, and there will be multiple records per playlist (one for every song within a user's playlist)
#     title = db.Column(db.String(64), nullable=False)
#     song = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
#     # These refer to the actual record in the database
#     created_at = db.Column(db.DateTime, nullable=False)
#     updated_at = db.Column(db.DateTime, nullable=False)
    
#     # todo: create a composite primary key
#     __table_args__ = (
#         PrimaryKeyConstraint('user', 'title', 'song')
#     )
    
#     # * many-to-one w/user
#     users = db.relationship('User', backref='playlist')  
    
#     # * many-to-one w/playlist
#     playlists = db.relationship('Playlist', backref='song')


# with app.app_context():
#     db.create_all()
    