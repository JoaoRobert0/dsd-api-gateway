import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

# URL do seu gateway FastAPI
GATEWAY_URL = "http://localhost:8000"  # Alterar se necessário

# View para obter produtos
def get_produtos(request):
    response = requests.get(f"{GATEWAY_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json()
        return render(request, 'produtos_list.html', {'produtos': produtos})
    return JsonResponse({"error": "Falha ao obter produtos"}, status=500)

# View para criar um produto
def create_produto(request):
    if request.method == "GET":
        # Renderiza o formulário para criar um novo produto
        return render(request, 'produtos_form.html')
    
    elif request.method == "POST":
        # Obtém os dados do formulário
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        # Verifica se os campos foram preenchidos
        if not nome or not preco:
            return JsonResponse({"error": "Nome e preço são obrigatórios"}, status=400)

        produto_data = {
            "nome": nome,
            "preco": preco
        }

        # Envia os dados para o serviço de gateway
        response = requests.post(f"{GATEWAY_URL}/produtos", json=produto_data)

        # Verifica a resposta do gateway
        if response.status_code == 200:
            return redirect("get_produtos")
        else:
            return JsonResponse({"error": "Falha ao criar produto no Gateway"}, status=500)
    
    else:
        return JsonResponse({"error": "Método inválido"}, status=405)

# View para operação de soma
def soma(request):
    if request.method == "POST":
        # Pega os valores do formulário usando request.POST.get()
        arg0 = request.POST.get('arg0')
        arg1 = request.POST.get('arg1')

        # Converte os valores para inteiros (se necessário)
        try:
            arg0 = int(arg0)
            arg1 = int(arg1)
        except ValueError:
            return render(request, 'soma.html', {'error': "Por favor, insira valores válidos."})

        # Faz a requisição para o gateway
        response = requests.post(f"{GATEWAY_URL}/soma?arg0={arg0}&arg1={arg1}")

        if response.status_code == 200:
            resultado = response.json()
            return render(request, 'soma.html', {'resultado': resultado['resultado']})
        else:
            return render(request, 'soma.html', {'error': "Falha ao realizar a soma."})

    return render(request, 'soma.html')

# View para operação de subtração
def subtracao(request):
    if request.method == "POST":
        # Pega os valores do formulário usando request.POST.get()
        arg0 = request.POST.get('arg0')
        arg1 = request.POST.get('arg1')

        # Converte os valores para inteiros (se necessário)
        try:
            arg0 = int(arg0)
            arg1 = int(arg1)
        except ValueError:
            return render(request, 'subtracao.html', {'error': "Por favor, insira valores válidos."})

        # Faz a requisição para o gateway
        response = requests.post(f"{GATEWAY_URL}/subtracao?arg0={arg0}&arg1={arg1}")

        if response.status_code == 200:
            resultado = response.json()
            return render(request, 'subtracao.html', {'resultado': resultado['resultado']})
        else:
            return render(request, 'subtracao.html', {'error': "Falha ao realizar a subtração."})

    return render(request, 'subtracao.html')
