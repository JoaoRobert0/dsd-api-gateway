from fastapi import FastAPI
import requests
import xml.etree.ElementTree as ET
from pydantic import BaseModel

app = FastAPI()

# URL do serviço de produtos
PRODUCTS_SERVICE_URL = "http://localhost:3000/produtos"  # Supondo que o serviço de produtos esteja rodando na porta 3000

# Endpoint para redirecionar requisições GET para o serviço de produtos
@app.get("/produtos")
def get_produtos():
    # Realiza uma requisição GET para o serviço de produtos
    response = requests.get(PRODUCTS_SERVICE_URL)

    # Monta a resposta com HATEOAS
    produtos = response.json()
    hateoas_response = {
        "produtos": produtos,
        "links": [
            {"rel": "self", "href": "/produtos", "method": "GET"},
            {"rel": "create", "href": "/produtos", "method": "POST"},
            {"rel": "soma", "href": "/soma", "method": "POST"},
            {"rel": "subtracao", "href": "/subtracao", "method": "POST"}
        ]
    }
    return hateoas_response

# Modelo Pydantic para o Produto
class Produto(BaseModel):
    nome: str
    preco: float

# Endpoint para criar um novo produto
@app.post("/produtos")
def create_produto(produto: Produto):
    # Converte o produto para dicionário (dict) antes de enviar
    response = requests.post(PRODUCTS_SERVICE_URL, json=produto.dict())

    # Monta a resposta com HATEOAS
    novo_produto = response.json()
    hateoas_response = {
        "produto": novo_produto,
        "links": [
            {"rel": "self", "href": "/produtos", "method": "POST"},
            {"rel": "list", "href": "/produtos", "method": "GET"},
            {"rel": "soma", "href": "/soma", "method": "POST"},
            {"rel": "subtracao", "href": "/subtracao", "method": "POST"}
        ]
    }
    return hateoas_response

# Endpoint para operação de soma
@app.post("/soma")
def soap_add(arg0: int, arg1: int):
   soap_url =  "http://localhost:8080/calculator"
   
   soap_request = f"""
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://soap/">
      <soapenv:Header/>
      <soapenv:Body>
         <soap:add>
            <arg0>{arg0}</arg0>
            <arg1>{arg1}</arg1>
         </soap:add>
      </soapenv:Body>
   </soapenv:Envelope>
   """

   response = requests.post(soap_url, data=soap_request, headers={'Content-Type': 'text/xml'})

   root = ET.fromstring(response.text)
   return_value = root.find('.//return').text

   # Monta a resposta com HATEOAS
   hateoas_response = {
       "resultado": return_value,
       "links": [
           {"rel": "self", "href": "/soma", "method": "POST"},
           {"rel": "subtracao", "href": "/subtracao", "method": "POST"},
           {"rel": "list", "href": "/produtos", "method": "GET"},
           {"rel": "create", "href": "/produtos", "method": "POST"}
       ]
   }

   return hateoas_response

# Endpoint para operação de subtração
@app.post("/subtracao")
def soap_subtract(arg0: int, arg1: int):
   soap_url =  "http://localhost:8080/calculator"
   
   soap_request = f"""
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://soap/">
      <soapenv:Header/>
      <soapenv:Body>
         <soap:subtract>
            <arg0>{arg0}</arg0>
            <arg1>{arg1}</arg1>
         </soap:subtract>
      </soapenv:Body>
   </soapenv:Envelope>
   """

   response = requests.post(soap_url, data=soap_request, headers={'Content-Type': 'text/xml'})

   root = ET.fromstring(response.text)
   return_value = root.find('.//return').text

   # Monta a resposta com HATEOAS
   hateoas_response = {
       "resultado": return_value,
       "links": [
           {"rel": "self", "href": "/subtracao", "method": "POST"},
           {"rel": "soma", "href": "/soma", "method": "POST"},
           {"rel": "list", "href": "/produtos", "method": "GET"},
           {"rel": "create", "href": "/produtos", "method": "POST"}
       ]
   }

   return hateoas_response
