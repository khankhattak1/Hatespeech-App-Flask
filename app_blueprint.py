from flask import Blueprint, render_template, request
from Usesavedmodel import score_comment
from bs4 import BeautifulSoup
import urllib.request


app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def home():
    return render_template('home.html')

    
@app_blueprint.route('/model_output')
def model_output():

    file = open(r"E:\Data Science\Web-Practice\Hatespeech-App-Flask\scrapped_file\scrap_data.txt","r", encoding="utf-8")
    data = str(file.read())

    print("\nDATA : ", data)

    if file is None:
        print("\n******FILE EMPTY******\n")
    else:
        new_data = str(score_comment(data)).upper()
        print("\n******NEW DATA******\n", new_data)
    return render_template('model_output.html', data = data, new_data = new_data)

@app_blueprint.route('/create_file', methods=['POST', 'GET'])
def create_file():
    url_scraper = request.form['input']
    
    if not(url_scraper.startswith("http://") or url_scraper.startswith("https://")):   
        #get the textual data only
        r = urllib.request.urlopen(url_scraper).read()
        soup = BeautifulSoup(r, "html.parser")
        if soup.find(class_="site-main"):
            soup.find( class_="site-main").decompose()
        elif soup.find(class_="css-1dbjc4n r-18u37iz r-1h0z5md"):
            soup.find( class_="css-1dbjc4n r-18u37iz r-1h0z5md").decompose()
        elif soup.find(class_="q-inlineFlex qu-mr--small"):
            soup.find( class_="q-inlineFlex qu-mr--small").decompose()
        # create txt file
        file = open("E:\\Data Science\Web-Practice\\Hatespeech-App-Flask\\scrapped_file\\scrap_data.txt","w", encoding="utf-8")
        file.write(soup.get_text())
        file.flush()
        file.close()
    

    # create txt file
    file = open("E:\\Data Science\Web-Practice\\Hatespeech-App-Flask\\scrapped_file\\scrap_data.txt","w", encoding="utf-8")
    file.write(url_scraper)
    file.flush()
    file.close()

    print("\n******File Created******\n")
    return render_template('model_output.html')