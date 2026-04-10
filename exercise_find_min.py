# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor mínimo de la lista o None si está vacía
    """
    # Reemplazar con tu implementación
    mini = float("infinity")
    if len(lista) > 0:
        for num in lista:
            if mini > num:
                mini = num
        return mini
    else:
        return None