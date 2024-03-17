
# Importación de las clases necesarias
from error import LargoExcedidoError
from anuncio import Video, Social, Display
from datetime import date

# Definir la clase Campania
class Campania():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        # Inicializa la campania con nombre, fechas de inicio y termino, y una lista de anuncios
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []

        # Itera la lista anuncios para obtener instancias que se almacenan en el atributo anuncios
        for a in anuncios:
            instancia_anuncio = self.__obtener_instancia_anuncio(a)
            self.__anuncios.append(instancia_anuncio)
        
    # Método privado para obtener la instancia del anuncio obteniendo los datos desde un diccionario
    def __obtener_instancia_anuncio(self, anuncio: dict):
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        # Crea la instancia de acuerdo con el tipo de anuncio
        # NOTA: para video no se agrega alto y ancho ya que el requerimiento señala que tiene valores predefinidos e inmodificables, según lo muestra el constructor de la clase en anuncio.py
        if tipo_anuncio == "video":
            return Video(duracion, url_archivo, url_clic, sub_tipo)
        elif tipo_anuncio == "display":
            return Display(ancho, alto, url_archivo, url_clic, sub_tipo)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_archivo, url_clic, sub_tipo)
            
    # Método de propiedad para acceder al nombre de la campaña
    @property
    def nombre(self) -> str:
        return self.__nombre

    # Método setter para el nombre de la campaña
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        
        # Verificar que el nombre ingresado no exceda los 250 caracteres
        if len(nombre) > 250:
            raise LargoExcedidoError("El largo del nombre excede los 250 caracteres")
        else:
            self.__nombre = nombre

    # Método de propiedad para acceder a la fecha de inicio
    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    # Método setter para la fecha de inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date) -> None:
        self.__fecha_inicio = fecha_inicio

    # Método de propiedad para la fecha de término
    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino

    # Método setter para la fecha de término
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date) -> None:
        self.__fecha_termino = fecha_termino

    # Método de propiedad para acceder a la lista de anuncios
    @property
    def anuncios(self) -> list:
        return self.__anuncios

    # Método para obtener una representación en cadena de la campaña
    def __str__(self):
        cant_video = len(list(filter(
            lambda x: isinstance(x, Video), self.anuncios
        )))
        cant_display = len(list(filter(
            lambda x: isinstance(x, Display), self.anuncios
        )))
        cant_social = len(list(filter(
            lambda x: isinstance(x, Social), self.anuncios
        )))

        # Devuelve un string con el conteo de cada tipo de anuncio en la lista
        return (f"Nombre de la Campaña: {self.__nombre}\n"
                f"Anuncios: {cant_video} Video, "
                f"{cant_display} Display, "
                f"{cant_social} Social")
    