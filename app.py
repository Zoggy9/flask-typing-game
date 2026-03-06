from flask import Flask, request, render_template_string
import random
app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Test Web-App</title>
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
    .url-form {
        display: inline-block;
        margin-top: 20px;
        padding: 10px 15px;
        background-color: black;
        color: green;
        border-radius: 5px;
    }
    .message {
        display: block;
        background-color: black;
        border-radius: 5px;
        border: 2px solid white;
        color: green;
        margin: 10px 500px;
        padding: 10px 0px;
        font-size: 30px;
    }
    h3 {
        color: black;
    }

    button {
        background-color: gray;
        color: blue;
    }

    input {
        border: 1px solid white;
        color: green;
        background-color: black;
        padding: 5px;
    }
    
    .coin-num {
        color: gold;
    }
    </style>
    <link rel="icon" href="https://png.pngtree.com/png-vector/20240816/ourlarge/pngtree-empty-laboratory-conical-flask-on-a-transparent-background-free-and-clipart-png-image_13503663.png">
</head>

<body>
<header><h2 class="lives">Lives: {{ lives_hearts }}</h2><h2 class="coins">Coins: <div class="coin-num">{{ coins }}</div></h2></header>
<h1>Test flask api</h1>
<h2>Enter the word "{{ random_word }}", please</h2>
    <form method="POST" action="/" class="url-form">
        <input 
            type="text" 
            name="inp-box" 
            placeholder="enter the word..."
            value="{{ box }}"
            required
            >
            <input type="hidden" name="random-word" value="{{ random_word }}">
            <input type="hidden" name="lives" value="{{ lives }}">
            <input type="hidden" name="coins" value="{{ coins }}">
                <button type="submit" class="btn" name="reset" value="dont-reset">Enter</button>
                <button type="submit" class="btn" name="reset" value="reset">Reset</button>
            </form>
<h2 class="message">{{ message }}</h2>
</body>
</html>
'''


@app.route('/', methods=['GET','POST'])
def render():
    word_list = ['something', 'nothing', 'anything', "cupboard", "pillow", "coffee maker", "bed", "spoon", "blanket", "knife", "stove", "sink", "washing machine", "pot", "dish", "fridge", "sofa", "stool", "cup", "fork", "glass"]
    box = ''
    message = ''
    correct_messages = ['correct!!!', 'nice one!', 'well done!', 'on fire!!!', 'spectacular!!!', 'keep it up!']
    incorrect_messages = ['oops, try again!!!', 'not quite...', 'better luck next time!', 'close, but no cigar!', 'almost there...', 'keep trying!']
    lives = 5
    coins = 0

    if request.method == 'POST':
        random_word = request.form.get('random-word')
        box = request.form.get('inp-box').lower()
        lives = int(request.form.get('lives'))
        coins = int(request.form.get('coins'))
        if box == random_word:
            message = random.choice(correct_messages)
            coins += 10
        else:
            message = random.choice(incorrect_messages)
            coins -= 10
            lives -= 1
            if lives <= 0:
                message = 'Game Over!!!'
                random_word = random.choice(word_list)
                lives = 5
                coins = 0

    else:
        random_word = random.choice(word_list)
        lives = 5
        coins = 0

    reset = request.form.get('reset')
    if reset == 'reset':
        box = ''
        random_word = random.choice(word_list)
        lives = int(request.form.get('lives'))
        coins = int(request.form.get('coins'))
        

    lives_hearts = '❤️' * lives
    rendered_html = render_template_string(html_template, box=box, message=message, random_word=random_word, lives_hearts=lives_hearts, lives=lives, coins=coins)
    return rendered_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
