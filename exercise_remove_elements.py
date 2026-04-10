# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    # Reemplazar con tu implementación
    if len(lista) >= 6:   # Es mayor o igual a 6 elementos
        del lista[5]      # Saca el sexto
    if len(lista) >= 5:   # Es mayor o igual a 5 elementos
        del lista[4]      # Saca el quinto
    try:
        del lista[0]
    except IndexError:
        return lista
    return lista