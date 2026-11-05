import pytest
from descuentos import calcular_precio_final


def test_cliente_vip_con_cupon():
    # Arrange & Act
    resultado = calcular_precio_final(100.0, es_vip=True, cupon="DESCUENTO10")
    # Assert
    assert resultado == 70.0


def test_precio_invalido_lanza_excepcion():
    with pytest.raises(ValueError):
        calcular_precio_final(-10, es_vip=False)


def test_cliente_regular_sin_cupon():
    resultado = calcular_precio_final(100.0, es_vip=False)
    assert resultado == 100.0


def test_cupon_superpromo():
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="SUPERPROMO")
    assert resultado == 50.0


def test_cupon_oro():
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="ORO")
    assert resultado == 70.0
