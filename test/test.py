from src.main import *
from unittest.mock import patch
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', retrun_value=123456):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 123456}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Divaldo", curso="ADS", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def teste_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def teste_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def teste_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def teste_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result