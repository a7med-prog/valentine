from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    session.clear()
    return redirect(url_for('question1'))

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        session['question1'] = request.form.get('question1')
        return redirect(url_for('question2'))
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        session['question2'] = request.form.get('question2')
        return redirect(url_for('question3'))
    return render_template('question2.html')

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        session['question3'] = request.form.get('question3')
        return redirect(url_for('question4'))
    return render_template('question3.html')

@app.route('/question4', methods=['GET', 'POST'])
def question4():
    if request.method == 'POST':
        session['birthday'] = request.form.get('birthday')
        return redirect(url_for('question5'))
    return render_template('question4.html')

@app.route('/question5', methods=['GET', 'POST'])
def question5():
    if request.method == 'POST':
        session['question5'] = request.form.get('question5')
        return redirect(url_for('question6'))
    return render_template('question5.html')

@app.route('/question6', methods=['GET', 'POST'])
def question6():
    if request.method == 'POST':
        session['question6'] = request.form.get('question6')
        return redirect(url_for('result'))
    return render_template('question6.html')

@app.route('/result')
def result():
    question1 = session.get('question1')
    question2 = session.get('question2')
    question3 = session.get('question3')
    birthday = session.get('birthday')
    question5 = session.get('question5')
    question6 = session.get('question6')
    
    # Calculate age
    birthdate = datetime.strptime(birthday, '%Y-%m-%d')
    age = datetime.now().year - birthdate.year - ((datetime.now().month, datetime.now().day) < (birthdate.month, birthdate.day))
    
    if question1 == 'yes' and question2 == 'yes' and question3 == 'no' and question5 == 'yes' and question6 == 'yes':
        match = "We look like a perfect match!"
    else:
        match = "Maybe we can still be friends!"
    
    return render_template('result.html', match=match, age=age)

if __name__ == '__main__':
    app.run(debug=True)
