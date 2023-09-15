from flask import Flask, url_for, session, request
from flask import render_template, redirect
import pdb, requests


app = Flask(__name__)
app.config.from_object('config')


@app.route('/index/')
@app.route('/')
def login():
  body = '<h1> LinkedIn GTM+CAPI Access Token Generation </h1> <br> <h3>Click <a href="' + app.config['LINKEDIN_AUTHORIZE_URL'] + '?response_type=code&client_id=' + app.config['LINKEDIN_CLIENT_ID'] + '&redirect_uri=' + app.config['LINKEDIN_REDIRECT_URI_1'] + '&state=foobar&scope=' + app.config['LINKEDIN_SCOPE'] + '">here</a> to begin the OAuth flow and generate an access token</h1>'
  #pdb.set_trace()
  return body


@app.route('/authcode/')
def authcode():
  #need to make a call for the access token (with the autho code, client id, client secret)
  #once that call is returned, display the access token 
  
  auth_code = request.args.get('code')
  
  post_data = {'grant_type':'authorization_code', 'code':auth_code, 'client_id':app.config['LINKEDIN_CLIENT_ID'], 'client_secret':app.config['LINKEDIN_CLIENT_SECRET'], 'redirect_uri':app.config['LINKEDIN_REDIRECT_URI_1']}

  post_headers = {'Content-Type': 'application/x-www-form-urlencoded' }
  
  r = requests.post(app.config['LINKEDIN_ACCESS_TOKEN_URL'], data = post_data, headers=post_headers)
  access_token = r.json()['access_token']
  body = 'I hear you would like an access token...<br><br> ' + access_token
  return body


@app.route('/accessToken/')
def accessToken():
  return 'sounds like we did it in a few hours. whats the big deal people'


