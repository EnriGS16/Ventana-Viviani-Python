import math

# --- Funciones matemáticas ---
def longitud_viviani(R, n):
    a = 0
    b = 2 * math.pi
    delta_t = (b - a) / n
    suma = 0
    for i in range(n):
        t = a + (i+0.5) * delta_t
        integrando= (R / 2) * math.sqrt(1 + math.cos(t / 2) ** 2)
        suma += integrando
    return suma * delta_t

# --- Validación numérica ---
def es_numero_valido(texto):
    texto = texto.replace(",", ".")
    partes = texto.split(".")
    if len(partes) > 2:
        return False
    for p in partes:
        if not p.isdigit():
            return False
    return True

# --- Inicio del programa ---
print("Cálculo del perímetro de la Ventana de Viviani usando Suma de Riemann")

# Radio de la esfera
R_input = input("Ingrese el radio de la esfera (cm): ")
while not (es_numero_valido(R_input) and float(R_input.replace(",", ".")) > 0):
    print("¡Radio incorrecto! Ingrese un número válido y positivo.")
    R_input = input("Ingrese el radio de la esfera (cm): ")
R = float(R_input.replace(",", "."))

# Número de subintervalos
n_input = input("Ingrese la cantidad de subintervalos: ")
while not n_input.isdigit() or int(n_input) <= 0:
    print("¡Valor incorrecto! Debe ser un entero positivo.")
    n_input = input("Ingrese la cantidad de subintervalos: ")
n = int(n_input)

# Cantidad de decimales a mostrar
d_input = input("Ingrese la cantidad de decimales para mostrar el resultado: ")
while not d_input.isdigit() or int(d_input) < 0:
    print("¡Valor incorrecto! Debe ser un número entero no negativo.")
    d_input = input("Ingrese la cantidad de decimales para mostrar el resultado: ")
decimales = int(d_input)

# Cálculo
print("\nCalculando perímetro...")
perimetro_aprox = longitud_viviani(R, n)
print(f"\nPerímetro aproximado: {perimetro_aprox:.{decimales}f} cm")
