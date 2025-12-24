from ejercicio1.notificaciones import SistemaNotificaciones, Canal
from ejercicio2.estacionamiento import Estacionamiento, Vehiculo
from ejercicio3.pagos import Tienda, MedioPago
from ejercicio4.sensores import Sensor

def ejecutar_pruebas():
    print("--- PRUEBA EJERCICIO 1: NOTIFICACIONES ---")
    sn = SistemaNotificaciones()
    email = Canal("Email", 10)
    sms = Canal("SMS", 50, limite_caracteres=20)
    sn.registrar_destino(email, "user@test.com")
    sn.registrar_destino(sms, "+56912345678")
    print(sn.enviar_alerta("Alerta de Seguridad"))
    print(sn.enviar_alerta("Este mensaje es demasiado largo para el canal SMS")) # Simula fallo en SMS

    print("\n--- PRUEBA EJERCICIO 2: ESTACIONAMIENTO (12 estadías) ---")
    est = Estacionamiento()
    auto = Vehiculo("ABCD12", "Auto", 20)
    moto = Vehiculo("XYZ12", "Moto", 10)
    for i in range(6):
        est.registrar_estadia(auto, 45 + (i*10), es_hora_punta=(i%2==0))
        est.registrar_estadia(moto, 30 + (i*5))
    total, top, conteo = est.generar_reporte()
    print(f"Total Recaudado: {total}, Vehículos: {conteo}")

    print("\n--- PRUEBA EJERCICIO 3: TIENDA ---")
    tienda = Tienda()
    visa = MedioPago("Tarjeta", 0.05)
    efectivo = MedioPago("Efectivo", 0)
    print(tienda.realizar_venta(101, 5000, visa))
    print(tienda.realizar_venta(102, 3000, efectivo))

    print("\n--- PRUEBA EJERCICIO 4: SENSORES ---")
    s_temp = Sensor("Temperatura", "C", -10, 50)
    s_temp.registrar_lectura(30, "C")
    s_temp.registrar_lectura(100, "F")
    print(f"Estadísticas Sensor: {s_temp.obtener_estadisticas()}")

if __name__ == "__main__":
    ejecutar_pruebas()2
    ---------------------------fin------------------------------