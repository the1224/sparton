from flask import jsonify, request
from db import db

def vote_get(id):
    vote_id = int(id)
    vote_list = list(db.vote_polls.find({'id': vote_id}, {'_id': False, 'id':False}))
    return jsonify({'vote_data': vote_list})

def vote_put():
    #선택한 것의 이름과 투표의 아이디 가져오기
    vote_name = request.form['vote_select_name']
    vote_id = int(request.form['vote_id'])

    #선택한것의 현재 투표갯수를 가져와 +1 하기
    select_add_num = vote_now_num(vote_id,vote_name) + 1

    try:
        #업데이트 해주기
        db.vote_polls.update_one({'id':int(vote_id)},{"$set":{vote_name:int(select_add_num)}})
        return "ok"
    except Exception as e:
        return "error"


def vote_now_num(id, vote_name):
    vote_data = list(db.vote_polls.find({'id':id}, {'_id': False}))

    now_num = vote_data[0][vote_name]

    if(vote_data == []):
        return 0
    else:
        return int(now_num)









