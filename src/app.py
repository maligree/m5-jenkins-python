from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'index': True})

@app.route('/item/<int:item_id>')
def item(item_id):
    return jsonify({'item': {'id': item_id }})

if __name__ == "__main__":
    app.run()
