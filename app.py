from flask import Flask, request, url_for, session, redirect
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

app.secret_key = ""
app.config['SESSION_COOKIE_NAME'] = 'Cookie Monster'

the_remote_app = oauth.remote_app(
    'remote_application',
    base_url='',
    request_token_url='',
    access_token_url='',
    authorize_url='',
    consumer_key='',
    consumer_secret=''
)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/login')
def login():
    return app.authorize(callback=url_for('oauth_authorized',
    next=request.args.get('next') or request.referrer or None
    ))

@app.route('/redirect')
def redirect():
    return 'redirect'
@app.route('/play_something')
def play():
    return "Playing something"
@app.tokengetter
def get_app_token(token=None):
    return session.get('app_token')