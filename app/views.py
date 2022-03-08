from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros, Lanches, users_Login
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

def login(request):

    return render(request, 'login.html')

def loginForm(request):

    return render(request, 'loginForm.html')

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request,pk):
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