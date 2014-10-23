from flask import render_template
from app import app

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	user = {'nickname': 'Miguel', 'name':'MM'}  # fake user
	posts = [  # fake array of posts
	    { 
	        'author': {'nickname': 'John'}, 
	        'body': 'Beautiful day in Portland!' 
	    },
	    { 
	        'author': {'nickname': 'Susan'}, 
	        'body': 'The Avengers movie was so cool!' 
	    }
	]
	return render_template("index.html",
	                       title='Home',
	                       user=user,
	                       posts=posts)


@app.route('/user/<username>')
def user(username):
	user = {'nickname': 'Miguel', 'name':'MM'}
	if len(username) >0:
		user['nickname']  = username
	posts = [  # fake array of posts
	    { 
	        'author': {'nickname': 'John'}, 
	        'body': 'Beautiful day in Portland!' 
	    },
	    { 
	        'author': {'nickname': 'Susan'}, 
	        'body': 'The Avengers movie was so cool!' 
	    }
	]
	return render_template("index.html", user=user, posts = posts)