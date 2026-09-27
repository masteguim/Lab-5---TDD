from TDD import Calculadora

def test_soma():
    calc = Calculadora()

    resultado = calc.somar(2, 3)

    assert resultado == 5