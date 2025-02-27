from fastapi import FastAPI
import requests
import xml.etree.ElementTree as ET

app = FastAPI()

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

   return {"resultado": return_value}

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

   return {"resultado": return_value}
