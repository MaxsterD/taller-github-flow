"""Módulo de procesamiento de pagos."""

# Constantes de negocio (0 valores mágicos)
IMPUESTOS_POR_PAIS = {
    "CO": 0.19,
    "MX": 0.16,
    "CL": 0.19,
}

UMBRAL_VIP = 1000
DESCUENTO_VIP_ALTO = 0.20       # 20% descuento
DESCUENTO_VIP_ESTANDAR = 0.10   # 10% descuento


def calcular_descuento_vip(monto):
    """Calcula el descuento aplicable para clientes VIP."""
    return DESCUENTO_VIP_ALTO if monto > UMBRAL_VIP else DESCUENTO_VIP_ESTANDAR


def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    """
    Procesa el pago de un usuario aplicando descuentos e impuestos según reglas de negocio.
    Complejidad Ciclomática: V(G) = 5
    """
    # 1. Guard Clauses: validación del estado del usuario
    if usuario is None:
        return False

    if not usuario.get("activo", False):
        print("Usuario inactivo")
        return False

    # 2. Cálculo de descuento
    descuento = calcular_descuento_vip(monto) if es_vip else 0.0
    monto_final = monto * (1 - descuento)

    # 3. Impuestos por país (Principio Open/Closed)
    tasa_impuesto = IMPUESTOS_POR_PAIS.get(pais, 0.0)
    monto_final += monto_final * tasa_impuesto

    # 4. Guard Clause: validación de saldo sobre el monto final real
    if tarjeta.get("saldo", 0) < monto_final:
        print("Saldo insuficiente")
        return False

    # 5. Débito y confirmación
    tarjeta["saldo"] -= monto_final
    return True