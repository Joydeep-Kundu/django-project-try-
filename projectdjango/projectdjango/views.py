"""
to render html web page
"""
from django.http import HttpResponse
from articles.models import Article
from random import randint
def home_view(request):
    """
    take in a request (Django sends request)
    Return HTM as a response (we pic to return the response)
    """
    name='rn'
    number=randint(1,3)
    article_obj=Article.objects.get(id=number)
    h1_string=f"""
    <h1>{article_obj.title} ({article_obj.id})</h1>
    """
    p_string=f"""
    <p>{article_obj.content}
    """
    HTML_STRING=h1_string+p_string
    return HttpResponse(HTML_STRING)