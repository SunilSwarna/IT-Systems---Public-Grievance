#from django.shortcuts import render


"""
    html= ''
       url='/music/'+ str(album.id) + '/'
        html += '<a href=" ' + url + ' " >' + album.album_title +'</a><br>'

    return HttpResponse(html)
---------------------------------------
    all_albums=Album.objects.all()
    template1= loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template1.render(context,request))

----------------
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doosn't exist")


from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.template import loader
from .models import Album,song
from .models import song


def index(request):
    all_albums = Album.objects.all()
    context = {   'all_albums': all_albums,}
    return render(request,'music/index.html',context)



def detail(request,album_id):
    # for rasing an error i m using get_object_or_404
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html', { 'album': album})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,song.DoesNotExist):
        return render(request,'music/detail.html', {
        'album': album,
        'error_message': "You did not sleect a valid song",
    })
    else:
         selected_song.is_favourite=True
         selected_song.save()
         return render(request,'music/detail.html', { 'album': album})

         -----------------------
         <!--
<form action="{% url 'music:favorite' album.id %}" method="post">

    {% csrf_token %}
    {% for song in album.song_set.all %}
        <input type="radio" id="song{{forloop.counter}}" name="song" value="{{song.id}}"/>
    <label for="song{{ forloop.counter }}">
        {{song.song_title}}
        {% if song.is_favourite %}
            <img src="http://i.imgur.com/b9b13Rd.png" />
        {% endif %}
    </label><br>

    {% endfor %}
    <input type="submit" value="Favorite" >
</form>
-->
------------------------
def login_view(request):
    title = "Login"
    template_name = 'music/form.html'
    form=UserLoginForm(request.POST or None)
    if form.is_valid():

        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
    return render(request,template_name,{"form":form,"title":title })
    -------------------------


class IndexView(generic.ListView):

    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()
        ------------------------

def login1(request):
   # form=UserForm1(request.POST or None)
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('music:index')

                # request.user.username
            else:

                return render(request,'music/login.html',{'error_message':"Your account has been disabled"})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})

    return render(request, 'music/login.html',context={"form":form,})
-------------
@charset "utf-8";
@import url(http://weloveiconfonts.com/api/?family=fontawesome);

[class*="fontawesome-"]:before {
  font-family: 'FontAwesome', sans-serif;
}

body {
  background: #2c3338;
  color: #606468;
  font: 87.5%/1.5em 'Open Sans', sans-serif;
  margin: 0;
}

input {
  border: none;
  font-family: 'Open Sans', Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5em;
  padding: 0;
  -webkit-appearance: none;
}

p {
  line-height: 1.5em;
}

after { clear: both; }

#login {
  margin: 50px auto;
  width: 320px;
}

#login form {
  margin: auto;
  padding: 22px 22px 22px 22px;
  width: 100%;
  border-radius: 5px;
  background: #282e33;
  border-top: 3px solid #434a52;
  border-bottom: 3px solid #434a52;
}

#login form span {
  background-color: #363b41;
  border-radius: 3px 0px 0px 3px;
  border-right: 3px solid #434a52;
  color: #606468;
  display: block;
  float: left;
  line-height: 50px;
  text-align: center;
  width: 50px;
  height: 50px;
}

#login form input[type="text"] {
  background-color: #3b4148;
  border-radius: 0px 3px 3px 0px;
  color: #a9a9a9;
  margin-bottom: 1em;
  padding: 0 16px;
  width: 235px;
  height: 50px;
}

#login form input[type="password"] {
  background-color: #3b4148;
  border-radius: 0px 3px 3px 0px;
  color: #a9a9a9;
  margin-bottom: 1em;
  padding: 0 16px;
  width: 235px;
  height: 50px;
}

#login form input[type="submit"] {
  background: #b5cd60;
  border: 0;
  width: 100%;
  height: 40px;
  border-radius: 3px;
  color: white;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
}
#login form input[type="submit"]:hover {
  background: #16aa56;
}
"""

from django.views import generic
from .models import Album
from .models  import Transport

from django.views.generic.edit  import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login, logout, get_user_model
from django.views.generic import  View
from .models import Album
from django.contrib.auth.models import User
from .forms import UserForm,UserLoginForm,UserForm1
from .forms import TransportForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):

    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()
#@login_required
def index(request):
    if not request.user.is_authenticated():
        return redirect('music:login1')
    else :

      #  user_id = int(request.POST['username'])
      #  user = User.objects.get(id=user_id)
        current_user = request.user
      # print current_user.id
        idp1 = current_user.id
        all_albums = Transport.objects.filter(idp=idp1)
        contents = {   'all_albums': all_albums,}
        return render(request,'music/index.html',contents)
def display(request):
    current_user = request.user
    # print current_user.id
    idp1 = current_user.id
    all_albums = Transport.objects.filter(idp=idp1)
    contents = {'all_albums': all_albums, }
    return render(request, 'music/display.html', contents)

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'
   #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
  #process the data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            # cleaned (normalized) data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

        # returns User Objects if credentials are correct

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:

                    login(request,user)
                    return redirect('music:index')

                   # request.user.username

        return render(request, self.template_name, {'form': form})


def login1(request):
   # form=UserForm1(request.POST or None)
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('music:index')

                # request.user.username
            else:

                return render(request,'music/login1.html',{'error_message':"Your account has been disabled"})
        else:
            return render(request, 'music/login1.html', {'error_message': 'Invalid login'})

    return render(request, 'music/login1.html')

def logout_user(request):
    logout(request)
    return redirect('music:login1')
def transport_new(request):
   ##return render(request,'music/transport_edit.html',{'form':form})
    if request.method == "POST":
        form = TransportForm(request.POST ,request.FILES or None)
        if form.is_valid():
        #    instance = Transport(file_field=request.FILES['logo'])
         #   instance.save()
            Transport1 = form.save(commit=False)
            current_user = request.user
           # print current_user.id
            Transport1.idp = current_user.id
            Transport1.created_date= timezone.now()
            Transport1.save()
            return redirect('music:index')
    else:
        form = TransportForm()
    return render(request, 'music/transport_edit.html', {'form': form})
def alll(request):
    all_albums = Transport.objects.all()
    current_user = request.user
    # print current_user.id
    k = current_user.id
    return render(request, 'music/alll.html', {'all_albums': all_albums,'k':k})

def delete_album(request, album_id):
    album = Transport.objects.get(pk=album_id)
    album.delete()
    current_user = request.user
    # print current_user.id
    idp1 = current_user.id
    all_albums = Transport.objects.filter(idp=idp1)
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Transport, pk=album_id)
        k=album.idp
        m = User.objects.get(id=k).username
        return render(request, 'music/detail.html', {'album': album,'m':m})


















