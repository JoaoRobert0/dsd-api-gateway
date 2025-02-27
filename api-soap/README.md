# Servidor SOAP em Java

Este é um simples servidor SOAP em Java que oferece operações de cálculo, como adição e subtração.

## Estrutura do Projeto

- **src/**: Contém o código-fonte Java.
- **bin/**: Contém os arquivos `.class` compilados.

## Pré-requisitos

- Java JDK 8 instalado.
- Variáveis de ambiente `JAVA_HOME` e `PATH` configuradas.

Verifique a instalação com:
```sh
java -version
javac -version
```

## Compilação

1 - Abra o terminal e navegue até o diretório src:
```sh
cd src
```
2 - Crie uma pasta bin/ irmã a src/

3 - Compile os arquivos .java para a pasta bin:
```sh
javac -d ../bin soap/*.java
```

## Execução

1 - Navegue até o diretório bin:
```sh
cd ../bin
```

2 - Inicie o servidor SOAP:
```sh
java soap.SoapServer
```

O servidor será iniciado em:
```sh
http://localhost:8080/calculator
```

## Testando o servidor

Use o SOAP UI ou faça uma requisição manual com o cURL ou Postman. Exemplo de requisição para adicionar dois números:
```sh
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://soap/">
   <soapenv:Header/>
   <soapenv:Body>
      <soap:add>
         <arg0>5</arg0>
         <arg1>3</arg1>
      </soap:add>
   </soapenv:Body>
</soapenv:Envelope>
```

Envie esta requisição para:
```sh
http://localhost:8080/calculator
```