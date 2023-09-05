def validate_date(date: str) -> str:
    # Parsear la fecha en día, mes y año
    d, m, a = list(map(int, date.split()))

    # Función auxiliar para determinar si un año es bisiesto
    def es_bisiesto(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Validar el mes
    if m < 1 or m > 12:
        return "Fecha incorrecta"

    # Validar el día según el mes
    if m == 2:  # Febrero
        if es_bisiesto(a):
            if d < 1 or d > 29:
                return "Fecha incorrecta"
        else:
            if d < 1 or d > 28:
                return "Fecha incorrecta"
    elif m in [4, 6, 9, 11]:  # Meses con 30 días
        if d < 1 or d > 30:
            return "Fecha incorrecta"
    else:  # Meses con 31 días
        if d < 1 or d > 31:
            return "Fecha incorrecta"

    return "Fecha correcta"