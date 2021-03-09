from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    dados = [("0", "Sorvete de cocô"), ("1" ,"Pudim de Barbeiro"), ("2", "Bolo de barata")]

    receitas = {
        "nome_das_receitas" : dados
    }

    return render(request, "index.html", receitas)

def receita(request):
    return  render(request, "receita.html")