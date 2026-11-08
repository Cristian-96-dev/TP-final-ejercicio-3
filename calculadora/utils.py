def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    
    emision = consumo_kwh * factor_emision  
    return emision



def obtener_metricas_consumo(registros_plantas: list) -> dict:
    
    total_emisiones = 0.0
    consumo_maximo = 0.0
    planta_mayor_consumo = "Sin registros"

    for planta in registros_plantas:
        consumo_actual = planta.get("consumo_kwh", 0.0)
        emision_planta = calcular_emisiones_carbono(consumo_actual)
        
        total_emisiones += emision_planta

        if consumo_actual > consumo_maximo:
            consumo_maximo = consumo_actual
            planta_mayor_consumo = planta.get("nombre_planta", "Desconocida")

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo
    }



