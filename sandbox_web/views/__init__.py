
import os
from pprint import pprint as pp

import api, conf
from sandbox_web import app

from flask import g, session, redirect, render_template, abort, \
                    request, flash, url_for, send_from_directory

from blog_view import *


@app.route("/")
def home():
    """This function peforms the home page view"""
    pp(api.blog.get_blog())
    #return render_template("show_entries.html", 
    #                        entries=api.blog.get_blog())
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != conf.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != conf.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries.html'))

@app.route("/file/<path:filename>")
def get_file(filename):
    """This function serves file from the file_store directory;
    Returns the file provided by the path:filename argument"""

    print filename
    return send_from_directory(app.root_path+"/file_store/", 
                               filename, as_attachment=True)

@app.route("/file/")
@app.route("/files/")
def list_files():
    """Lists all files available in the filestore"""
    return render_template("files.html", 
                            file_list=sorted(os.listdir(os.path.join(app.root_path, "file_store"))))


from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
