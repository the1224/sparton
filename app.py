from flask import Flask, render_template, jsonify
from vote import *

app = Flask(__name__)

from db import *

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/vote-poll')
def vote_poll():
  return render_template('vote-poll.html')

@app.route('/vote')
def vote():
  return render_template('vote.html', id = request.args.get('id'))

#각 링크별 결과창 생성
@app.route('/vote-result')
def vote_result():
  return render_template('vote-result.html', id = request.args.get('id'))

@app.route('/shared-vote-links')
def shared_vote_links():
  return render_template('shared-vote-links.html', id = request.args.get('id'))

@app.route('/api/vote-poll', methods=["POST"])
def create_vote_poll():
  doc = {}
  for key, value in request.form.items():
    if key == "title_give":
      doc['title'] = value
    else:
      doc[value] = 0
  new_id = len(list(db.vote_polls.find({}, {'_id': False})))
  doc['id'] = new_id
  db.vote_polls.insert_one(doc)

  return jsonify({'error': False, 'id': new_id})

# 투표 GET API
@app.route('/api/vote', methods=["GET"])
def vote_get_data():
  id = request.args.get('idGive', "0")
  return vote_get(id)

# 투표 POST API
@app.route('/api/vote', methods=["POST"])
def vote_post_api():
  return "post"

# 투표 DELETE API
@app.route('/api/vote', methods=["DELETE"])
def vote_delete_api():
  return "delete"

# 투표 PUT API
@app.route('/api/vote', methods=["PUT"])
def vote_put_api():
  return vote_put()


@app.route('/api/vote-result', methods=["GET"])
def get_vote_result():
  id_give = int(request.args.get('id'))
  found_vote_result = db.vote_polls.find_one({'id': id_give}, {'_id': False})
  if found_vote_result is None:
    return jsonify({'error': True, 'msg': '해당 id를 가진 투표장이 없습니다'})

  doc = {}
  doc['error'] = False
  for key, value in found_vote_result.items():
    if key != 'id' and key != 'msg':
      doc[key] = value
  return doc



@app.route('/api/vote-results', methods=["GET"])
def get_all_vote_results():
  all_vote_results = list(db.vote_polls.find({}, {'_id': False}))
  return all_vote_results


# 각 링크별 결과 받아오기
@app.route("/api/vote", methods=["GET"])
def vote_result_get():
  vote_result = list(db.vote_polls.find({}, {'_id': False}))
  return jsonify({'results': vote_result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)