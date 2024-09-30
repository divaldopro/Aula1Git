from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', retrun_value=123456):
        result = funcaoteste()
        yield result
    assert result == {"teste": True, "num_aleatorio": 123456}

def test_create_estudante():
    estudante_teste = Estudante(name="Divaldo", curso="ADS", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

def teste_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def teste_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result

def teste_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result

def teste_delete_estudante_positivo():
    result = delete_estudante(5)
    yield result
    assert result