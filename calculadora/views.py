from django.shortcuts import render
from .utils import obtener_metricas_consumo, calcular_emisiones_carbono

def vista_panel_sustentabilidad(request):
    historial_consumos = [
        {"nombre_planta": "Planta Norte", "consumo_kwh": 450.5},
        {"nombre_planta": "Planta Sur", "consumo_kwh": 820.0},
        {"nombre_planta": "Planta Este", "consumo_kwh": 310.2}
    ]
    
    metricas = obtener_metricas_consumo(historial_consumos)
    
    contexto = {
        "emisiones_totales": metricas["total_emisiones"],
        "planta_destacada": metricas["planta_mayor_consumo"],
        "registros": historial_consumos
    }
    
    return render(request, "sustentabilidad/panel.html", contexto) 
