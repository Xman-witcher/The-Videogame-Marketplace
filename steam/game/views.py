from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from game.models import Games


# Create your views here.

def mygames(request):
    username = request.user.username
    game = Games.objects.filter(name=username).first()
    dicts={}
    if game.gta==True:
            dicts['gta']=1

    if game.nfs==True:
            dicts['nfs']=1

    if game.ac==True:
            dicts['ac']=1

    if game.spiderman==True:
            dicts['spiderman']=1

    if game.uncharted==True:
            dicts['uncharted']=1

    if game.tombraider==True:
            dicts['tombraider']=1

    if game.dmc==True:
            dicts['dmc']=1

    if game.cod==True:
            dicts['cod']=1

    if game.sam==True:
            dicts['sam']=1

    if game.division==True:
            dicts['division']=1
    if len(dicts)==0:
        dicts['nogame']=1

    return render(request, 'mygames.html', dicts)

def home(request):

    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        if len(username)>25:
            newname = username[0:25]+'....'+username[-1]
            dicts['username']=newname
        else:
            dicts['username']=username
        

        game = Games.objects.filter(name=username).first()
        if not game:
            game = Games(name=username, gta=False, nfs=False, ac=False, spiderman=False, uncharted=False, tombraider=False, dmc=False, cod=False, sam=False, division=False)
            game.save()
        
        if game.gta==True:
            dicts['gta']=1

        if game.nfs==True:
            dicts['nfs']=1

        if game.ac==True:
            dicts['ac']=1

        if game.spiderman==True:
            dicts['spiderman']=1

        if game.uncharted==True:
            dicts['uncharted']=1

        if game.tombraider==True:
            dicts['tombraider']=1

        if game.dmc==True:
            dicts['dmc']=1

        if game.cod==True:
            dicts['cod']=1

        if game.sam==True:
            dicts['sam']=1

        if game.division==True:
            dicts['division']=1

    return render(request, 'home.html', dicts)

def gta(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.gta:
          dicts['paid']=1
    return render(request, 'gtav.html',dicts)
def nfs(request):
    return render(request, 'nfs.html')

def ac(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.ac:
          dicts['paid']=1
    return render(request, 'ac.html',dicts)


def spiderman(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.spiderman:
          dicts['paid']=1
    return render(request, 'spiderman.html',dicts)

def uncharted(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.uncharted:
          dicts['paid']=1
    return render(request, 'uncharted.html',dicts)

def tombraider(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.tombraider:
          dicts['paid']=1
    return render(request, 'tombraider.html',dicts)

def dmc(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.dmc:
          dicts['paid']=1
    return render(request, 'dmc.html',dicts)

def cod(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.cod:
          dicts['paid']=1
    return render(request, 'cod.html',dicts)

def sam(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.sam:
          dicts['paid']=1
    return render(request, 'sam.html',dicts)

def nfs(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.nfs:
          dicts['paid']=1
    return render(request, 'nfs.html',dicts)

def division(request):
    dicts={}
    if request.user.is_authenticated:
        username = request.user.username
        game = Games.objects.filter(name=username).first()    
        if game.division:
          dicts['paid']=1
    return render(request, 'division.html',dicts)



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            dicts={'error':1}
            return render(request, 'login.html',dicts )
               
    return render(request, 'login.html', {})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors.as_text()
            count=0
            lists=[]
            s=''
            for i in errors:
                if i=='*':
                    if s!='':
                        lists.append(s)
                        s=''
                    count+=1
                    continue
                if count%2==0:
                    s+=i
            lists.append(s)                
            return render(request, 'signup.html', {'form': form, 'errors': lists})
    
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')



@login_required
def payment_gta5(request):
    name= 'Grand Theft Auto V'
    price = 'Rs. 2499/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.gta = True
        game.save()

    return render(request, 'payment.html', dicts)



@login_required
def payment_nfs(request):
    name= 'Need for Speed'
    price = 'Rs. 4499/-'
    dicts={'game_name':name, 'price':price}
       
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.nfs = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_ac(request):
    name= "Assassin's Creed: Mirage"
    price = 'Rs. 4999/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.ac = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_spiderman(request):
    name= 'Spider-Man'
    price = 'Rs. 3999/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.spiderman = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_uncharted(request):
    name= "Uncharted 4: A Thief's End"
    price = 'Rs. 4999/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.uncharted = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_tombraider(request):
    name= 'Tomb Raider'
    price = 'Rs. 4499/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.tombraider = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_dmc(request):
    name= 'Devil May Cry 4'
    price = 'Rs. 3199/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.dmc = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_cod(request):
    name= 'Call of Duty: Modern Warfare'
    price = 'Rs. 4999/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.cod = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_sam(request):
    name= 'Serious Sam 4'
    price = 'Rs. 4499/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.sam = True
        game.save()
    
    return render(request, 'payment.html', dicts)



@login_required
def payment_division(request):
    name= 'The Division'
    price = 'Rs. 1999/-'
    dicts={'game_name':name, 'price':price}
    if request.method == 'POST':
        dicts['paid']=1 
        username = request.user.username
        game = Games.objects.filter(name=username).first()
        game.division = True
        game.save()
    
    return render(request, 'payment.html', dicts)


def paid(request):
        return redirect('/')