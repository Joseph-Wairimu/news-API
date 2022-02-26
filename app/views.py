from flask import render_template
from app import app

# Views
from .request import get_news, get_new

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news()
    print(popular_news)
    title = 'Home - Welcome to The Best news broadcast Online'
    return render_template('index.html', title = title,popular = popular_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)

