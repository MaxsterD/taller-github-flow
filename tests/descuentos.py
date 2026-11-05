def calcular_precio_final(precio_base: float, es_vip: bool, cupon: str = None) -> float:
       if precio_base <= 0:
           raise ValueError("El precio debe ser mayor a cero")
       
       descuento = 0.20 if es_vip else 0.0
       if cupon == "DESCUENTO10":
           descuento += 0.10
       # Agrega esto en descuentos.py
       if cupon == "SUPERPROMO":
           descuento += 0.50
       # Agrega esto en descuentos.py
       if cupon == "ORO":
           descuento += 0.30        
       return precio_base * (1 - descuento)