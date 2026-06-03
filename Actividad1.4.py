def nombre_de_la_funcion(parametro1, parametro2):
    """
    Documentación de la función (opcional pero recomendado)
    Explica qué hace la función y qué parámetros espera
    """
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado  # Opcional: devuelve un valor
def saludar(nombre):
    """
    Muestra un saludo personalizado
    
    Args:
        nombre (str): El nombre de la persona a saludar
        
    Returns:
        str: Un mensaje de saludo
    """
    mensaje = f"¡Hola, {nombre}! Veo que tienes 28 y vives en Madrid ¡Bienvenida!."
    return mensaje

# Llamando a la función
print(saludar("Ana"))  # Muestra: ¡Hola, Ana! Bienvenido al curso de Python.