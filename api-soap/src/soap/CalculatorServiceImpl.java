package soap;

import javax.jws.WebService;

@WebService(endpointInterface = "soap.CalculatorService")
public class CalculatorServiceImpl implements CalculatorService {
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    public int subtract(int num1, int num2) {
        return num1 - num2;
    }
}
