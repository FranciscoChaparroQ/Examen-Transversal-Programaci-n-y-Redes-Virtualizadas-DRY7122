import geopy.distance

# Definición de las ciudades y sus coordenadas (latitud y longitud)
ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Buenos Aires": (-34.6037, -58.3816),
    "Mendoza": (-32.8895, -68.8458),
    "Córdoba": (-31.4201, -64.1888),
    "Rosario": (-32.9442, -60.6505)
}

# Función para obtener la distancia entre dos ciudades
def obtener_distancia(ciudad_origen, ciudad_destino):
    coords_origen = ciudades[ciudad_origen]
    coords_destino = ciudades[ciudad_destino]
    distancia_km = geopy.distance.distance(coords_origen, coords_destino).km
    distancia_millas = geopy.distance.distance(coords_origen, coords_destino).miles
    return distancia_km, distancia_millas

# Función para calcular la duración del viaje
def calcular_duracion(distancia_km, medio_transporte):
    velocidades = {
        "auto": 80,  # km/h
        "bus": 60,   # km/h
        "avión": 800  # km/h
    }
    velocidad = velocidades.get(medio_transporte, 80)  # Valor por defecto: auto
    duracion_horas = distancia_km / velocidad
    return duracion_horas

# Función principal
def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ")
        if ciudad_destino.lower() == 's':
            break

        if ciudad_origen in ciudades and ciudad_destino in ciudades:
            distancia_km, distancia_millas = obtener_distancia(ciudad_origen, ciudad_destino)
            medio_transporte = input("Ingrese el medio de transporte (auto, bus, avión): ").lower()
            duracion_horas = calcular_duracion(distancia_km, medio_transporte)

            print(f"\nNarrativa del viaje:")
            print(f"Desde {ciudad_origen} hasta {ciudad_destino}")
            print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
            print(f"Duración estimada del viaje: {duracion_horas:.2f} horas en {medio_transporte}\n")
        else:
            print("Una de las ciudades ingresadas no está en la lista. Por favor, intente nuevamente.\n")

if __name__ == "__main__":
    main()
