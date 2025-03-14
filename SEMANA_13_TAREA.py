# Garcia Arreaga Jeison Teobaldo
# Función para calcular el promedio de temperatura por ciudad

def calcular_promedio_temperaturas(temperaturas, nombres_ciudades):
    print("------PROMEDIO DE TEMPERATURAS POR CIUDAD------")

    for ciudad_idx, ciudad in enumerate(temperaturas):
        total_temperaturas = 0
        total_dias = 0

        print(f"Promedio de temperaturas en {nombres_ciudades[ciudad_idx]}:")

        for semana_idx, semana in enumerate(ciudad):
            suma_temperaturas = sum(dia["temp"] for dia in semana)
            promedio_semana = suma_temperaturas / len(semana)

            print(f"  Semana {semana_idx + 1}: {promedio_semana:.2f}°C")

            total_temperaturas += suma_temperaturas
            total_dias += len(semana)

        promedio_ciudad = total_temperaturas / total_dias
        print(f"  Promedio total de la ciudad: {promedio_ciudad:.2f}°C\n")

# Datos de ejemplo
nombres_ciudades = ["Quito", "Guayaquil", "Ambato"]

temperaturas = [
    [  # Ciudad 1: Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [  # Ciudad 2: Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [  # Ciudad 3: Ambato
        [  # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 24}
        ]
    ]
]

calcular_promedio_temperaturas(temperaturas, nombres_ciudades)
