
from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_news,get_new, get_category

from ..models import Articles


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news()
    print(popular_news)
    title = 'Home - Welcome to The Best news broadcast Online'
    return render_template('index.html', title = title,popular = popular_news)

@main.route('/news/<source_id>')
def news(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news=get_new(source_id)
    name= f'{news.name}'
    return render_template('news.html' ,name=name, news=news )

@main.route('/news/<id>')
def news_articles(id):

    """
    View articles function
    """
    articles=get_article(id)
    
    return render_template('articles.html',articles=articles)


@main.route('/general')
def show_articles():
    """
    Show articles function
    """
    category=get_category('general')
    return render_template('general.html',category=category)


@main.route('/business')
def show_business():
    """
    Show articles function
    """
    category=get_category('business')
    return render_template('business.html',category=category)    

@main.route('/entertainment')
def show_entertainment():
    """
    Show articles function
    """
    category=get_category('entertainment')
    return render_template('entertainment.html',category=category)        


@main.route('/health')
def show_health():
    """
    Show articles function
    """
    category=get_category('health')
    return render_template('health.html',category=category)  

@main.route('/sports')
def show_sports():
    """
    Show articles function
    """
    category=get_category('sports')
    return render_template('sports.html',category=category)         