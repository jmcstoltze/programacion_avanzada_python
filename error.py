class Error(Exception):
    """
    Clase base para excepciones personalizadas en este módulo.
    """
    pass

class LargoExcedidoError(Error):
    """
    Excepción lanzada cuando la longitud excede un cierto límite.

    Atributos:
        Ninguno
    """
    pass

class SubTipoInvalidoError(Error):
    """
    Excepción lanzada cuando se encuentra un subtipo no válido.

    Atributos:
        Ninguno
    """
    pass
