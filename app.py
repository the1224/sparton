from flask import Flask, render_template, jsonify, request
from vote import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/vote-poll')
def vote_poll():
  return render_template('vote-poll.html')

@app.route('/vote/<id>')
def vote(id):
  return render_template('vote.html', id = id)

@app.route('/vote-result')
def vote_result():
  return render_template('vote-result.html')

@app.route('/shared-vote-links')
def shared_vote_links():
  return render_template('shared-vote-links.html')

# 투표 GET API
@app.route('/api/vote', methods=["GET"])
def vote_get_data():
  id = request.args.get('idGive', "0")
  return vote_get(id)

# 투표 POST API
@app.route('/api/vote', methods=["POST"])
def vote_post_api():
  return vote_post()

# 투표 DELETE API
@app.route('/api/vote', methods=["DELETE"])
def vote_delete_api():
  return vote_delete()

# 투표 PUT API
@app.route('/api/vote', methods=["PUT"])
def vote_put_api():
  return vote_put()

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)