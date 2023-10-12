from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap

import forms
from forms import AboutMeForm
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions', methods=['POST', 'GET'])
def questions():
    return render_template('questions.html')

@app.route('/mystory', methods=['POST'])
def mystory():
    if request.method == 'POST':
        food = request.form['food']
        job = request.form['job']
        adj = request.form['adj']
        phrase = request.form['phrase']
        animal = request.form['animal']
        place = request.form['place']
        verb = request.form['verb']
        celebrity = request.form['celebrity']
        buy = request.form['buy']
        things = request.form['things']
        return render_template('mystory.html',f=food, j=job, adj=adj, place=place, prhase=phrase,animal=animal,celeb=celebrity, buy=buy, verb=verb,things=things)
    return render_template('questions.html')

@app.route('/colorballoon', methods=['POST'])
def colorballoon():
    if request.method == 'POST':
        color = request.form['color']
        things2 = request.form['things2']
        adj = request.form['adj2']
        phrase = request.form['phrase2']
        word = request.form['word']
        verb = request.form['verb2']
        place = request.form['place2']
        person = request.form['person']
        animal = request.form['animal2']
        things3=request.form['things3']

        return render_template('color_balloon.html',c=color,t=things2,adj=adj,ph=phrase, word=word,verb=verb,place=place,person=person,animal=animal,things=things3)
    return render_template('questions.html')
@app.route('/halloween', methods=['POST'])
def halloween():
    if request.method == 'POST':
        scary_thing = request.form['noun']
        adj1 = request.form['adj1']
        person=request.form['person']
        number = request.form['num']
        verb1 = request.form['verb1']
        foods=request.form['foods']
        adj2 = request.form['adj2']
        monster=request.form['monster']
        animal1=request.form['animal1']
        thing=request.form['thing']

        return render_template('halloween.html', noun=scary_thing, adj1=adj1,
                               person=person, verb1=verb1,
                               foods=foods, adj2=adj2, monster=monster,
                               animal1=animal1,thing=thing, number=number)
    return render_template('questions.html')

@app.route('/aliens', methods=['POST'])
def aliens():
    if request.method == 'POST':
        adj = request.form['adj']
        silly = request.form['silly']
        verb = request.form['verb']
        thing = request.form['thing']
        game = request.form['game']
        food = request.form['food']
        person1 = request.form['person1']
        animals = request.form['animals']
        person2 = request.form['person2']
        return render_template('aliens.html', adj=adj,silly=silly,verb=verb,thing=thing,game=game,
                               food=food,person1=person1,animals=animals,person2=person2)
    return render_template('questions.html')


if __name__ == '__main__':
    app.run(debug=True)





