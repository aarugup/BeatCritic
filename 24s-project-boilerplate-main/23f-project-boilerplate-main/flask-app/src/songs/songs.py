from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


songs = Blueprint('songs', __name__)

# Get all the songs from the database
@songs.route('/songs', methods=['GET'])
def get_songs():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of songs
    cursor.execute('SELECT songID, songDescription FROM Songs')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@songs.route('/songs/<songID>', methods=['GET'])
def get_song_detail (songID):

    query = 'SELECT * FROM Songs WHERE songId = ' + str(songID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# get the avg rating on a specific song
@songs.route('/songs/<songID>/avg_rating')
def get_song_avg_rating():
    cursor = db.get_db().cursor()
    query = '''
        SELECT AVG(rating)
        FROM Songs, ratings
        WHERE Songs.songID = ratings.songID
    '''
    cursor.execute(query)
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@songs.route('/songs', methods=['POST'])
def add_new_song():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    genreID = the_data['genreID']
    artistID = the_data['artistID']
    rating = the_data['rating']

    # Constructing the query
    query = 'insert into Songs (genreID, artistID, rating) values ('
    query += genreID + ', '
    query += artistID + ', '
    query += rating + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Song Added!'

@songs.route('/songs/<songID>', methods=['PUT'])
def update_song(songID):
    # Collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variable
    genreID = the_data['genreID']
    artistID = the_data['artistID']
    rating = the_data['rating']
    songID = the_data['songID']

    # Constructing the query
    query = 'UPDATE Songs SET genreID = '
    + genreID + ', artistID = ' + artistID + ', rating = ' 
    + rating + ', songID = ' + songID
    + ' WHERE songID = ' + str(songID)
    current_app.logger.info(query)

    # Executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Song updated!'

@songs.route('/songs/<songID>', methods=['DELETE'])
def delete_song(songID):
    # Constructing the query
    query = 'DELETE FROM Songs WHERE songID = ' + str(songID)
    current_app.logger.info(query)

    # Executing and committing the delete statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Song deleted!'