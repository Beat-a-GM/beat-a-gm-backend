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
@app.route("/puzzles/")
def puzzles():
    data = supabase.table("Puzzles").select("*").execute().data
    print("data "+str(data))
    return jsonify(data)
@app.route("/puzzles/get/<int:id>")
def puzzles_id(id):
    data = supabase.table("Puzzles").select("*").eq("id", int(id)).execute().data[0]
    return jsonify(data)
@app.route("/puzzles/get/category/<string:category>")
def puzzles_cat(category):
    data = supabase.table("Puzzles").select("*").eq("category", (category)).execute().data
    return jsonify(data)
@app.route("/categories")
def get_categories():
    data = supabase.table("Categories").select("*").execute().data
    res = []
    for dict in data:
        res.append(dict["name"])
    return jsonify(res)
if (__name__ == "__main__"):
    app.run(debug=True)