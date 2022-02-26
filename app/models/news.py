class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,urlToImage,language,country,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.language = language
        self.country = country
        self.category = category


class Article:
    '''
    Class to define news article
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
