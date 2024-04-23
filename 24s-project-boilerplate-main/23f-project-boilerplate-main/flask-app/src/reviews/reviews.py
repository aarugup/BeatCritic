from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


reviews = Blueprint('reviews', __name__)

# Get all the reviews from the database
@reviews.route('/reviews', methods=['GET'])
def get_reviews():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of reviews
    cursor.execute('SELECT reviewID, userID FROM Reviews')

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

@reviews.route('/reviews/<reviewID>', methods=['GET'])
def get_review_detail (reviewID):

    query = 'SELECT * FROM Reviews WHERE reviewId = ' + str(reviewID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# get the comments on a specific review
@reviews.route('/reviews/<reviewID>/comments')
def get_review_comments():
    cursor = db.get_db().cursor()
    query = '''
        SELECT review_txt, songDescription, comments_txt
        FROM comments, songs, Reviews
        WHERE Reviews.commentID = comment.commentID AND Reviews.songID = songs.songID
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

@reviews.route('/reviews', methods=['POST'])
def add_new_review():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    songID = the_data['songID']
    modID = the_data['modID']
    userID = the_data['userID']
    review_txt = the_data['review_txt']

    # Constructing the query
    query = 'insert into Reviews (songID, modID, userID, review_txt) values ('
    query += songID + ', '
    query += modID + ', '
    query += userID + ', "'
    query += review_txt + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Review Added!'

@reviews.route('/reviews/<userID>', methods=['PUT'])
def update_review(reviewID):
    # Collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variable
    songID = the_data['songID']
    modID = the_data['modID']
    userID = the_data['userID']
    review_txt = the_data['review_txt']
    reviewID = the_data['reviewID']

    # Constructing the query
    query = 'UPDATE Reviews SET songID = '
    + songID + ', modID = ' + modID + ', userID = ' 
    + userID + ', review_txt = "' + review_txt + '", reviewID = ' + reviewID
    + ' WHERE reviewID = ' + str(reviewID)
    current_app.logger.info(query)

    # Executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Review updated!'

@reviews.route('/reviews/<reviewID>', methods=['DELETE'])
def delete_review(reviewID):
    # Constructing the query
    query = 'DELETE FROM Reviews WHERE reviewID = ' + str(reviewID)
    current_app.logger.info(query)

    # Executing and committing the delete statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Review deleted!'