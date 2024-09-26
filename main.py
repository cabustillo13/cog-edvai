from PIL import Image


def rotar_imagen(imagen_path, angulo):
    """
    Rota una imagen por un ángulo dado.

    :param imagen_path: Ruta a la imagen que se desea rotar.
    :param angulo: Ángulo en grados para rotar la imagen (entero).
    :return: Imagen rotada.
    """
    # Abre la imagen
    imagen = Image.open(imagen_path)
    
    # Rota la imagen
    imagen_rotada = imagen.rotate(angulo, expand=True)
    
    # Devuelve la imagen rotada
    return imagen_rotada
