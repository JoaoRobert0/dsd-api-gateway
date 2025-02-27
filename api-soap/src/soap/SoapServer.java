package soap;

import javax.xml.ws.Endpoint;

public class SoapServer {
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:8080/calculator", new CalculatorServiceImpl());
        System.out.println("SOAP Server started at http://localhost:8080/calculator?wsdl");
    }
}
