# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import json

# Load data from the JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

file_path = r'D:\ict300001 flask final\flask-sb-admin-master reworked\apps\static\assets\demo\pie-chart.txt'

@blueprint.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text']
        found = False
        for item in data['data']:
            if item['product_name'] == text:
                print(f"Product Name: {text}")
                print(f"Average Positive: {item['average_positive']}")
                print(f"Average Negative: {item['average_negative']}")
                print(f"Average Neutral: {item['average_neutral']}")
                
                # Write positive, negative, and neutral values to piechart.txt
                with open(file_path, 'w') as pie_file:
                    pie_file.write(f"{item['average_negative'] * 100}, {item['average_neutral'] * 100}, {item['average_positive'] * 100}")
                
                found = True
                break
        if not found:
            print("Product not found.")
    return '', 204

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
