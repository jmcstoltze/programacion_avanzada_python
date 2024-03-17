
# Importa la clase ABC y la función abstractmethod del módulo abc
from abc import ABC, abstractmethod

# Importa la clase SubTipoInvalidaError desde el archivo error.py
from error import SubTipoInvalidoError

# Definición de la clase Anuncio como clase abstracta
class Anuncio(ABC):
    
    # Método constructor con parámetros
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        
        # Inicializa los atributos del anuncio
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, nuevo_ancho: int) -> None:
        self.__ancho = nuevo_ancho if nuevo_ancho > 0 else 1

    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter
    def alto(self, nuevo_alto: int) -> None:
        self.__alto = nuevo_alto if nuevo_alto > 0 else 1

    # Método de propiedad para acceder a la url_archivo
    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    # Método setter para la url_archivo
    @url_archivo.setter
    def url_archivo(self, nueva_url_archivo: str) -> None:
        self.__url_archivo = nueva_url_archivo

    # Método de propiedad para acceder a la url_clic
    @property
    def url_clic(self) -> str:
        return self.__url_clic

    # Método setter para la url_clic
    @url_clic.setter
    def url_clic(self, nueva_url_clic: str) -> None:
        self.__url_clic = nueva_url_clic

    # Método de propiedad para acceder al sub tipo
    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    # Método setter para el subtipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    # Método estático para mostrar los formatos disponibles
    @staticmethod
    def mostrar_formatos() -> None:
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    # Método abstracto para comprimir los anuncios
    @abstractmethod
    def comprimir_anuncios(self) -> None:
        pass
    
    # Método abstracto para redimensionar los anuncios
    @abstractmethod
    def redimensionar_anuncio(self) -> None:
        pass

# Se define la clase Video que hereda de Anuncio
class Video(Anuncio):

    # Tupla de subtipos de la clase en string
    SUB_TIPOS = ("instream", "outstream")

    # Método constructor de la clase
    def __init__(self, duracion: int, url_archivo: str, url_clic: str, sub_tipo: str ) -> None:

        # Invoca al método constructor de la clase de la cual hereda
        super().__init__(ancho = 1, alto = 1, url_archivo = url_archivo.lower(), url_clic  = url_clic.lower(), sub_tipo = sub_tipo.lower())
        
        # Atributo de la instancia
        self.__duracion = duracion if duracion > 0 else 5

    # Método getter del atributo duración
    @property
    def duracion(self) -> int:
        return self.__duracion

    # Método setter del atributo duración 
    @duracion.setter
    def duracion(self, nueva_duracion: int) -> None:

        # Establece la nueva duracion siempre y cuando sea mayor que cero de lo contrario establece valor cinco
        self.duracion = nueva_duracion if nueva_duracion > 0 else 5

    # Método para comprimir el video no implementado aún
    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    # Método para redimensionar el video no implementado aún
    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

# Se define la clase Display que hereda de la clase Anuncio
class Display(Anuncio):

    # Tupla de subtipos de la clase en string
    SUB_TIPOS = ("tradicional", "native")

    # Método constructor de la clase
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:

        # Invoca al método constructor de la clase de la cual hereda
        super().__init__(ancho = ancho, alto = alto, url_archivo = url_archivo.lower(), url_clic = url_clic.lower(), sub_tipo = sub_tipo.lower())

    # Método para comprimir el anuncio display no implementado aún
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    # Método para redimensionar el anuncio display no implementado aún
    def redimensionar_anuncio():
        print("RECORTE DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

# Se define la clase Social que hereda de la clase Anuncio
class Social(Anuncio):

    # Tupla de subtipos de la clase en string
    SUB_TIPOS = ("facebook", "linkedin")

    # Método constructor de la clase
    def __init__(self, ancho:int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:

        # Invoca al método constructor de la clase de la cual hereda
        super().__init__(ancho = ancho, alto = alto, url_archivo = url_archivo.lower(), url_clic = url_clic.lower(), sub_tipo = sub_tipo.lower())

    # Método para comprimir el anuncio de redes sociales no implementado aún
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    # Método para redimensionar el anuncio de redes sociales no implementado aún
    def redimensionar_anuncio():
        print("RECORTE DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
