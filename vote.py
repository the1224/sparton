from flask import jsonify, request
from db import db

def vote_get(id):
    vote_id = int(id)
    print(vote_id)
    vote_list = list(db.vote_polls.find({'id': vote_id}, {'_id': False, 'id':False}))
    return jsonify({'vote_data': vote_list})

def vote_post():

    vote_name = request.form['vote_select_name']
    vote_id = int(request.form['vote_id'])

    select_add_num = vote_now_num(vote_id,vote_name) + 1

    try:
        db.vote_polls.update_one({'id':int(vote_id)},{"$set":{vote_name:int(select_add_num)}})
        return "ok"
    except Exception as e:
        return "error"

def vote_put():
    return "vote_put"

def vote_delete():
    return "vote_delete"

def vote_now_num(id, vote_name):
    vote_data = list(db.vote_polls.find({'id':id}, {'_id': False}))

    now_num = vote_data[0][vote_name]

    if(vote_data == []):
        return 0
    else:
        return int(now_num)









