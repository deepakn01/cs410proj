from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
	return render_template('index.html')
    
#@app.route("/results", methods=['post'])
#def results():
#	search_term = request.form['search']
#	return render_template('results.html',s_t = search_term)
 

@app.route("/results", methods=['post'])
def results():
	results = ['Result 1','Result 2','Result 3']
	sentiments = ['Positive','Neutral','Negetive']
	search_term = request.form['search']
	head1 = '<h1> Search Results for: '+ search_term +'</h1><br>'
	head2 = '<br>'
	for i, result in enumerate(results):
		head2 = head2+'<h2>' +result+ '&nbsp&nbsp&nbsp&nbsp'+ sentiments[i] +'</h2>'
	
	return head1+head2

app.run(debug=True)
