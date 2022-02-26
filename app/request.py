
from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
       get_news_data = url.read()
       get_news_response = json.loads(get_news_data)

       news_results = None

       if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        news_results = process_results(news_results_list)


        return news_results



def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        language= news_item.get('language')
        country = news_item.get('country')
        category = news_item.get('category')

        if url:
            news_object = News(id,name,description,url,language,country,category)
            news_results.append(news_object)

    return news_results

def get_new(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads( new_details_data)

        new_object = None
        if new_details_response:
            id =  new_details_response.get('id')
            name =  new_details_response.get('name')
            description =  new_details_response.get('description')
            url =  new_details_response.get('url')
            language= new_details_response.get('language')
            country =  new_details_response.get('country')
            category =  new_details_response.get('category')


            new_object = News(id,name,description,url,language,country,category)

    return new_object


