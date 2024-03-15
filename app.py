from flask import Flask, jsonify
import os
from supabase import create_client
from flask_cors import CORS

app = Flask(__name__)
app = Flask(__name__)
CORS(app)

# Create a Supabase client
database_url = os.environ.get('FLASK_DATABASE_URL')
database_key = os.environ.get('FLASK_DATABASE_KEY')

supabase = create_client(
    database_url,
    database_key
)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/puzzles")
def puzzles():
    data = supabase.table("Puzzles").select("*").execute().data
    print("data "+str(data))
    return jsonify(data)
@app.route("/puzzles/<int:id>")
def puzzles(id):
    
    data = supabase.table("Puzzles").select("id").eq(int(id)).execute().data
    return jsonify(data)

if (__name__ == "__main__"):
    app.run(debug=True)