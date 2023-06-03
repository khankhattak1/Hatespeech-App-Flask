from flask import Blueprint, render_template, request

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def home():
    return render_template('home.html')
    
@app_blueprint.route('/model_output')
def model_ouput():
    return render_template('model_output.html')

@app_blueprint.route('/create_file', methods=['POST', 'GET'])
def create_file():
    url_scraper = request.form['input']

    file = open("scrap_data.txt","w", encoding="utf-8")
    file.write(url_scraper)
    file.flush()
    file.close
    return render_template('model_output.html')