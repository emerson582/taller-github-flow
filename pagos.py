IMPUESTOS = {"CO": 0.19, "MX": 0.16, "CL": 0.19}


def calcular_descuento(monto, es_vip):
    if not es_vip:
        return monto
    if monto > 1000:
        return monto * 0.80
    return monto * 0.90


def aplicar_impuesto(monto, pais):
    return monto + monto * IMPUESTOS.get(pais, 0)


def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    if usuario is None:
        return False
    if not usuario['activo']:
        print("Usuario inactivo")
        return False
    if tarjeta['saldo'] < monto:
        print("Saldo insuficiente")
        return False

    monto_final = calcular_descuento(monto, es_vip)
    monto_final = aplicar_impuesto(monto_final, pais)
    tarjeta['saldo'] -= monto_final
    return True
