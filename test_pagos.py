import unittest
from pagos import procesar_pago_usuario


class TestProcesarPagoUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario_activo = {"id": 1, "nombre": "Juan", "activo": True}
        self.usuario_inactivo = {"id": 2, "nombre": "Pedro", "activo": False}

    def test_usuario_none(self):
        tarjeta = {"saldo": 1000}
        resultado = procesar_pago_usuario(None, tarjeta, 500, "CO", False)
        self.assertFalse(resultado)
        self.assertEqual(tarjeta["saldo"], 1000)

    def test_usuario_inactivo(self):
        tarjeta = {"saldo": 1000}
        resultado = procesar_pago_usuario(self.usuario_inactivo, tarjeta, 500, "CO", False)
        self.assertFalse(resultado)
        self.assertEqual(tarjeta["saldo"], 1000)

    def test_saldo_insuficiente(self):
        tarjeta = {"saldo": 100}
        resultado = procesar_pago_usuario(self.usuario_activo, tarjeta, 500, "CO", False)
        self.assertFalse(resultado)
        self.assertEqual(tarjeta["saldo"], 100)

    def test_pago_regular_colombia(self):
        # Monto 1000, no VIP -> 0% desc, IVA CO (19%) -> 1190
        tarjeta = {"saldo": 2000}
        resultado = procesar_pago_usuario(self.usuario_activo, tarjeta, 1000, "CO", False)
        self.assertTrue(resultado)
        self.assertAlmostEqual(tarjeta["saldo"], 2000 - 1190)

    def test_pago_vip_monto_bajo_mexico(self):
        # Monto 500 <= 1000, VIP -> 10% desc = 450. IVA MX (16%) -> 450 * 1.16 = 522
        tarjeta = {"saldo": 1000}
        resultado = procesar_pago_usuario(self.usuario_activo, tarjeta, 500, "MX", True)
        self.assertTrue(resultado)
        self.assertAlmostEqual(tarjeta["saldo"], 1000 - 522)

    def test_pago_vip_monto_alto_chile(self):
        # Monto 2000 > 1000, VIP -> 20% desc = 1600. IVA CL (19%) -> 1600 * 1.19 = 1904
        tarjeta = {"saldo": 3000}
        resultado = procesar_pago_usuario(self.usuario_activo, tarjeta, 2000, "CL", True)
        self.assertTrue(resultado)
        self.assertAlmostEqual(tarjeta["saldo"], 3000 - 1904)


if __name__ == "__main__":
    unittest.main()
