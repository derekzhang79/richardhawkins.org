"""
RichardHawkins.org (My Website)
Copyright (C) 2013 Richard Hawkins

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from flask import Flask, Response, url_for, render_template


app = Flask(__name__, static_url_path='', static_folder='./static')


@app.route('/404error.html')
def page_not_found():
    return render_template('404error.html')


@app.route('/')
def page_root():
    return render_template('root.html')

@app.route('/credits/')
def page_credits():
    return render_template('credits.html')
