
from django.test import TestCase
from .models import *

# Create your tests here.
class EditorTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    
  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.james,Editor))
    
  def test_save_method(self):
    self.james.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors)>0)

class ArticleTestClass(TestCase):
  
  def setUp(self):
    self.james = Editor(first_name = 'James', last_name = 'Muriuki', email ='james@moringas.com')
    self.james.save_editor()
    
    #new tag and save
    self.new_tag = tags(name = 'testing')
    self.new_tag.save()
    
    self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
    self.new_article.save()
    
  def tearDown(self):
      Editor.objects.all().delete()
      tags.objects.all().delete()
      Article.objects.all().delete()
      
  def test_get_news_today(self):
    today_news = Article.today_news()
    self.assertTrue(len(today_news)>0)
    
  def test_get_news_by_date(self):
    test_date = '2018-07-16'
    date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    news_by_date = Article.days_news(date)
    self.assertTrue(len(news_by_date)==0)
    
    
  