import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@myfirstcluster.iravb.mongodb.net/recipe_database?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", courses=mongo.db.courses.find(), cuisines=mongo.db.cuisines.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/get_cuisines')
def get_cuisines():
    return render_template("cuisines.html", cuisines=mongo.db.cuisines.find())


@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine_doc = {'cuisine_name': request.form.get('cuisine_name')}
    mongo.db.cuisines.insert_one(cuisine_doc)
    return redirect(url_for('get_cuisines'))


@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html')
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)