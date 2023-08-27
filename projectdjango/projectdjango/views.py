"""
to render html web page
"""
from django.http import HttpResponse
from django.template.loader import render_to_string,get_template
from articles.models import Article
from random import randint

def home_view(request):
    """
    take in a request (Django sends request)
    Return HTM as a response (we pic to return the response)
    """
    number=randint(1,3)
    article_obj=Article.objects.get(id=number)
    article_queryset=Article.objects.all()
    context={
        "object_list":article_queryset,
        "title": article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }

    #django templates
    HTML_STRING=render_to_string("home-view.html",
    context=context)
    # HTML_STRING="""
    # <h1>{title} ({id})</h1>
    # <p>{content}</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)