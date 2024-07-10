def isempty(string:str):
    return string=='_'

def isValidNumber(string:str):
    valid=False
    try:
        float(string)
        valid=True
    except ValueError:
        valid=False
    return valid

def isNumber(value,value2) -> bool:
    if isinstance(value,value2, int):  # Verifica se o valor recebido é do tipo int
        return True  # Se for, considera como um número inteiro válido
    else:
        return False  # Caso contrário, considera como inválido

