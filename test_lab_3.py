from solution import validate_date


def test_dates():
    inputs = [
        "6 7 531",
        "18 1 1784",
        "22 1 4336",
        "4 13 4668",
        "10 5 2390",
        "41 8 3080",
        "42 18 3539",
        "35 5 1165",
        "12 1 612",
        "21 10 3502",
        "32 18 3248",
        "14 5 3148",
        "50 8 4049",
        "35 11 1393",
        "4 2 4717",
        "45 14 1697",
        "26 16 74",
        "14 12 250",
        "31 13 510",
        "42 15 3820",
    ]
    
    outputs = [
        "Fecha correcta",
        "Fecha correcta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha incorrecta",
        "Fecha incorrecta",
        "Fecha correcta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha incorrecta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha incorrecta",
        "Fecha correcta",
        "Fecha incorrecta",
        "Fecha incorrecta",
    ]
    
    for inp, out in zip(inputs, outputs):
        assert validate_date(inp) == out
