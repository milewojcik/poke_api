import tkinter
import requests

#Cree la clase Pokemon
class Pokemon: 

#Cree las etiquetas
    def _init_ (self,nombre,tipo,habilidades,estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades 
        self.estadisticas = estadisticas

#Agregue la API
def datos_poke(): 
    pokemonId = entryId.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonId}" 
    respoonse = requests.get(url)

#Le di valor a las etiquetas
    if respoonse.status_code == 200 : #Verifica si la solucion fue exitosa 

        datos = respoonse.json()
        nombre = datos['name']
        tipo = datos['types']
        habilidades = datos['ability']
        estadisticas = datos ['statistics']

        etiqueta_nombre.config(text = "nombre:{nombre}")
        etiqueta_tipo.config(text = "tipo:{tipo}")
        etiqueta_habilidades.config(text = "habilidades:{habilidades}")
        etiqueta_estadisticas.config(text = "estadisticas:{estadisticas}")
    else:
        etiqueta_nombre.config(text="Error")
         
#Cree ventana
ventana = tkinter.Tk()
ventana.title = (Pokemon)
ventana.geometry = ("400x400") 

#Las etiquetas se muestren
etiqueta_nombre = tkinter.Label(ventana,text="")
etiqueta_nombre.pack()
etiqueta_tipo = tkinter.Label(ventana,text="")
etiqueta_tipo.pack()
etiqueta_habilidades = tkinter.Label(ventana,text="")
etiqueta_habilidades.pack()
etiqueta_estadisticas = tkinter.Label(ventana,text="")
etiqueta_estadisticas.pack()

#Cree el boton
boton_info = tkinter.Button (ventana, text= "obtener_info" , command= datos_poke)
boton_info.pack()

#Defini Entry
entryId = tkinter.Entry(ventana)
entryId.pack()
