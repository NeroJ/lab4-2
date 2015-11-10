from django.shortcuts import render_to_response,get_object_or_404
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Book
from models import Author
from forms import AddForm
from forms import AddForm_Author
from django.core.urlresolvers import reverse




 
global Gname
List_Au = ['0']
lst=['0']
def index(request):
    if request.POST:
       name=request.POST
       if not Author.objects.filter(Name=name['Name']):
           return HttpResponseRedirect(reverse("BookDB_none"))
       else:
           p=Author.objects.filter(Name=name['Name'])
           lst[0] = [p.all().values().get()]
           return HttpResponseRedirect(reverse("BookDB_search"))
    address=Book.objects.all()
    author = Author.objects.all()    
#    address=Book(Name = name["Name"],IDnumber = name["IDnumber"],
#                            Phone = name["Phone"],Email = name["Email"],
#                            QQ = name["QQ"],Birth = name["Birth"],
#                            Address = name["Address"],
#                            )       
    return render_to_response('list.html', {'address': address,'author':author})

def beforeadd(request):
    if request.GET:
       name=request.GET
       if not Author.objects.filter(Name=name['Name']):
           global Gname
           Gname = name['Name']
           return HttpResponseRedirect(reverse('BookDB_addauth'))
       else:
           p = Author.objects.filter(Name=name['Name'])
           p = [p.all().values().get()]
           List_Au[0] = p[0]['AuthorID']
           return HttpResponseRedirect(reverse("BookDB_add"))
    
    return render_to_response('beforeadd.html')
        


def add(request):
#    return render_to_response('add.html',)  
     if request.POST:
        name = request.POST
        form= Book(   ISBN = name["ISBN"],
                      Title = name["Title"],
                      AuthorID = List_Au[0],
                      Publisher = name["Publisher"],
                      PublishDate = name["PublishDate"],
                      Price = name["Price"],
                                )       
        form.save()
        return HttpResponseRedirect(reverse("BookDB_list"))
     return render_to_response('add.html', {'form': AddForm()})

def addauth(request):
#    return render_to_response('add.html',)
     if request.POST:
        name = request.POST
        
        form= Author( AuthorID = name["AuthorID"],
                      Name = Gname,
                      Age = name["Age"],
                      Country = name["Country"],
                                )
        form.save()
        List_Au[0] = name["AuthorID"]
        return HttpResponseRedirect(reverse('BookDB_add'))
     return render_to_response('addauth.html', {'form': AddForm_Author()})

def Search(request):
       iterms=lst[0]
       p = iterms[0]['AuthorID']
       Book_Au = Book.objects.filter(AuthorID = p)
#       iterms = [
#            {'Name':'nero','IDnumber':'1130310727','Phone':'15398096133','Email':'735422760@qq.com','QQ':'735422760','Birth':'1995.05.13' ,'Address':'ad1'},
#            {'Name':'cherry','IDnumber':'1130310720','Phone':'1565197760','Email':'232322323@qq.com','QQ':'234566543','Birth':'1995.05.03' ,'Address':'ad2'},
#            {'Name':'ben','IDnumber':'1130310720','Phone':'1565197760','Email':'232322323@qq.com','QQ':'234566543','Birth':'1995.05.03' ,'Address':'ad2'}
#            ]
       
       return render_to_response('search.html',{'Book_Au':Book_Au,'iterms':iterms})

def none(request):
    return render_to_response('none.html')
    
def bookauthor(request):
    auid = request.GET.get('auid')
    bid = request.GET.get('bid')
    iterms=Author.objects.filter(AuthorID=auid)   
    Book_Au = Book.objects.filter(id = bid)
    return render_to_response('bookauthor.html',{'Book_Au':Book_Au,'iterms':iterms})
      
def delete(request,id):

    BookDB=get_object_or_404(Book,pk=int(id))    

    BookDB.delete()

    return HttpResponseRedirect(reverse("BookDB_list"))    

def update(request,id):

    BookDB=get_object_or_404(Book,pk=int(id)) 
    if request.method=="POST":

        form=AddForm(request.POST,instance=BookDB)

        if form.is_valid():

            BookDB=form.save()

            

            return HttpResponseRedirect(reverse("BookDB_list"))

    return render_to_response('update.html', {'form': AddForm(instance=BookDB)})    
    
 
    
    
    
