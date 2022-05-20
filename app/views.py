from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros, Lanches, AuthUser
from django.contrib.auth import authenticate, login

from django.core.paginator import Paginator
# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Lanches.objects.filter(nome__icontains=search)

    else:
        #data['db'] = Lanches.objects.all()[:5]
        data['db'] = Lanches.objects.filter(nome='marcos', data_pedido='2022-02-18')[:5]
        #data['db'] = Lanches.objects.all()

        #data['db'] = Lanches.objects.filter(data_pedido='2022-02-18')

        #all = Lanches.objects.all()
        #paginator = Paginator(all, 10)
        #pages = request.GET.get('page')
        #data['db'] = paginator.get_page(pages)



    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def login2(request):

     return render(request, 'login.html')

def loginForm(request):

    return render(request, 'loginForm.html')

def dashboard(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Lanches.objects.filter(nome__icontains=search)

    else:
        # data['db'] = Lanches.objects.all()[:5]
        data['db'] = Lanches.objects.filter(nome='marcos', data_pedido='2022-02-18')[:5]
        #data['db'] = Lanches.objects.all()

        # data['db'] = Lanches.objects.filter(data_pedido='2022-02-18')

        # all = Lanches.objects.all()
        # paginator = Paginator(all, 10)
        # pages = request.GET.get('page')
        # data['db'] = paginator.get_page(pages)

    return render(request, 'dashboard/index.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def cadastrar_usuario(request):
    if request.method == "POST":
            form_usuario = UserCreationForm(request.POST)
            if form_usuario.is_valid():
                form_usuario.save()
                return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'loginForm.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        user1 = request.POST["username"]
        senha = request.POST["password"]
        usuario1 = authenticate(request, username=user1, password=senha)
        if usuario1 is not None:
            login(request, usuario1)
            return redirect('dashboard')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})


def view(request, pk):
    data = {}
    data['db'] = Lanches.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')