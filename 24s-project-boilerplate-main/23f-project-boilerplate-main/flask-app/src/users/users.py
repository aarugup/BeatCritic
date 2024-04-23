from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


users = Blueprint('users', __name__)

# Get all the users from the database
@users.route('/users', methods=['GET'])
def get_users():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT userID, fName, mName, lName FROM Users')

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

@users.route('/users/<userID>', methods=['GET'])
def get_user_detail (userID):

    query = 'SELECT userID, fName, mName, lName, email, phoneNo FROM Users WHERE userId = ' + str(userId)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# get the users reviews from the database
@users.route('/users/<userID>/reviews')
def get_user_reviews():
    cursor = db.get_db().cursor()
    query = '''
        SELECT songDescription, review_txt
        FROM Reviews, Songs, Users
        WHERE Reviews.userID = Users.userID AND Reviews.songID = Songs.songID
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

@users.route('/users', methods=['POST'])
def add_new_user():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    fName = the_data['fName']
    mName = the_data['mName']
    lName = the_data['lName']
    email = the_data['email']
    phoneNo = the_data['phoneNo']

    # Constructing the query
    query = 'insert into Users (fName, mName, lName, email, phoneNo) values ("'
    query += fName + '", "'
    query += mName + '", "'
    query += lName + '", "'
    query += email + '", '
    query += phoneNo + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'User Added!'

@users.route('/users/<userID>', methods=['PUT'])
def update_user(userID):
    # Collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variable
    fName = the_data['fName']
    mName = the_data['mName']
    lName = the_data['lName']
    email = the_data['email']
    phoneNo = the_data['phoneNo']
    userID = the_data['userID']

    # Constructing the query
    query = 'UPDATE Users SET fName = "'
    + fName + '", mName = "' + mName + '", lName = "' 
    + lName + '", email = "' + email + '", phoneNo = ' 
    + str(phoneNo) + ', userID = ' + userID + ' WHERE userID = ' + str(userID)
    current_app.logger.info(query)

    # Executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'User updated!'

@users.route('/users/<userID>', methods=['DELETE'])
def delete_user(userID):
    # Constructing the query
    query = 'DELETE FROM Users WHERE userID = ' + str(userID)
    current_app.logger.info(query)

    # Executing and committing the delete statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'User deleted!'