# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
    # Reemplazar con tu implementación
    maxi = float("-infinity")
    if len(lista) > 0:
        for num in lista:
            if maxi < num:
                maxi = num
        return maxi
    else:
        return None
