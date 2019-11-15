from flask import Flask,redirect,url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecrectkey'

#twitter_blueprint = make_twitter_blueprint(api_key='',api_secret='')
#github_blueprint = make_github_blueprint(client_id='',client_secret='')
google_blueprint = make_google_blueprint(client_id='ENTER YOUR GOOGLE CLIENT ID', client_secret='ENTER YOUR CLIENT SECRET')

app.register_blueprint(google_blueprint, url_prifix='/google_login')

@app.route('/')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v1/userinfo')
    assert resp.ok, resp.text
    #return "You are {email} on Google".format(email=resp.json()["email"])
    return "<marquee>You are successfully loggged in/marquee>"
if __name__ == '__main__':
    app.run(ssl_context="adhoc")


