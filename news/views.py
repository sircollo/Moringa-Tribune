from ast import Not
from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404
import datetime as dt

from news.models import Article
# Create your views here.

# def welcome(request):
#   return render(request,'all-news/todays-news.html')

def news_of_day(request):
  date = dt.date.today()
  day = convert_dates(date)
  news = Article.today_news()
  return render(request,'all-news/todays-news.html',{'date':date,'news':news})
  
def convert_dates(dates):
  day_number = dt.date.weekday(dates)
  
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  
  day = days[day_number]
  return day

def past_days_news(request,past_date):
  date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
  day = convert_dates(date)
  try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

  except ValueError:
      # Raise 404 error when ValueError is thrown
      raise Http404()
    
  if date == dt.date.today():
    return redirect(news_of_day)
  title = 'Archives'
  news = Article.days_news(date)
  return render(request,'all-news/past-news.html',{"date": date,"news":news})

def search_results(request):
  if 'article' in request.GET and request.GET["article"]:
      search_term = request.GET.get("article")
      searched_articles = Article.search_by_title(search_term)
      message = f"{search_term}"

      return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

  else:
      message = "You haven't searched for any term"
      return render(request, 'all-news/search.html',{"message":message})
DoesNotExist = Http404   


def article(request,articles_id):
  try:
    article = Article.objects.get(id=articles_id)
  except DoesNotExist:
    raise Http404
  return render(request, 'all-news/article.html',{'article':article})


