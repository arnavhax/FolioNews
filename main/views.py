
from django.http import HttpResponse
from django.template import loader
from .models import Stock
from django.contrib.auth.models import User
from bs4 import BeautifulSoup as bs
from django.contrib.auth import get_user_model
import requests 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def update(request):
    User = get_user_model()
    logged_in_user = request.user
    stock_list = User.objects.filter(pk=logged_in_user.pk).values_list('stock__name', flat=True)
    html="https://www.moneycontrol.com/news/stocksinnews-142.html"#get webpage
    homepage=requests.get(html)
    soup = bs(homepage.content,"html.parser")
    pagination=soup.find("div",class_="pagenation")
    pages=pagination.find_all("a")
    linklist=[]
    portfolio=stock_list#your portfolio
    try:
        for stock in portfolio:# remove whitespaces
                    if stock is None:
                        portfolio.remove(stock)
                    else:
                        stock.replace(" ","")
        for page in pages:
            pagelink=page['href']
            if(pagelink[0]=="/"):
                html_page="https://www.moneycontrol.com"+pagelink
                homepage_page=requests.get(html_page)
                soup = bs(homepage_page.content,"html.parser")
                headings = soup.find_all("li", class_="clearfix")#get all headings
                for head in headings:#iterate articles
                    news=head.find("h2")#get all anchor tags with news links
                    para=news.find("a")
                    text=para.text
                    text=text.replace(" ","")
                    for k in portfolio:
                        if(k.casefold() in text.casefold()):#ignore case and find keyword
                            link=para['href']
                            name=para.text
                            linklist.append((link,name))  #get link to article
    except:
         pass
    template = loader.get_template("main/main.html")
    context = {
        "stock_list": stock_list,
        "news_list": linklist,
    }
    # news_list = "pass after getting links of news"
    return HttpResponse(template.render(context, request))

def main(request):
    User = get_user_model()
    logged_in_user = request.user
    stock_list = User.objects.filter(pk=logged_in_user.pk).values_list('stock__name', flat=True)
    template = loader.get_template("main/main.html")
    context = {
        "stock_list": stock_list,
    }
    return HttpResponse(template.render(context, request))
def saveStock(request):
    if request.method =='POST':
        name=request.POST.get('stock_name')
        if(name==''):
             pass
        else:
            form=Stock(name=name,user_name = User.objects.get(pk=request.user.id))
            form.save()
    return redirect('/main')
     
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class MyLoginView(LoginView):
    template_name = 'registration/login.html'

def logout_view(request):
    logout(request)
    return redirect('/') 

def about(request):
     pass