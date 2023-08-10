# Rock Paper Scissors Game in Python
from flask import Flask,render_template,request
import random

app = Flask(__name__)


def opponent():
    options = ['rock','paper','scissors']
    ans = options[random.randint(0, 2)]
    return ans

def player(i):
    opp = opponent()
    if i==opp:
        result = "It's a Tie"
    elif (i == 'rock' and opp == 'scissors') or (i == 'paper' and opp == 'rock') or (i == 'scissors' and opp == 'paper'):
        result = 'You Win'
    else:
        result = 'You Lost'
    return [result,opp]


@app.route('/', methods=['GET', 'POST'])
def rpsgame():
    answer = ''
    final = ['','']
    if request.method == 'POST' and 'option' in request.form:
        answer = request.form.get('option')
        final = player(answer)
    return render_template('index.html',fin=final[0],a=final[1])


if __name__ == '__main__':
    app.run(debug=True)
