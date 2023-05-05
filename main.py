from flask import Flask, render_template, redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_proj_key'


@app.route('/')
@app.route('/index')
def index():
    user = "owner"
    return render_template('index.html', title='Универсальный сайт для художников')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/users')
def users():
    return render_template("users_list.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
