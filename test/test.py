from src.main import *
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', retrun_value=123456):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 123456}

def test_create_estudante():
    estudante_teste = Estudante(name="Divaldo", curso="ADS", ativo=False)
    assert estudante_teste == create_estudante()

def teste_update_estudante_negativo():
    assert not update_estudante(-5)

def teste_update_estudante_positivo():
    assert update_estudante(10)

def teste_delete_estudante_negativo():
    assert not delete_estudante(-5)

def teste_delete_estudante_positivo():
    assert delete_estudante(5)