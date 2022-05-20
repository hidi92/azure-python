#importamos los mudulos externos necesarios para el funcionamiento de las diferentes utilidades
import sys
import os
import importlib
from importlib import reload
import subprocess
from subprocess import Popen
from subprocess import PIPE
import PySimpleGUI as sg

#importamos los mudulos de nuestros diferentes Menus y Scripts
global window
global crearRG
global eliminarRG
global crearVM

crearRG = importlib.import_module("1_crear_rg")
eliminarRG = importlib.import_module("2_eliminar_rg")
crearVM = importlib.import_module("3_crear_vm")


#Funcion para borrar la pantalla
def limpiar_pantalla():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
	


#Funcion para elegir las opciones del menu
def menuopc():
	sg.theme('Material1')
	layout = [[sg.Text("Elige una opcion")],
            [sg.Radio('Crear un grupo de recursos', "opcion", default=False,key="createRG")],
			[sg.Radio('Eliminar un grupo de recursos', "opcion", default=False,key="deleteRG")],
			[sg.Radio('Crear una maquina virtual', "opcion", default=False,key="createVM")],
			[sg.Text('Otras opciones', size=(17, 1))],
			[sg.Radio('Limpiar Pantalla', "opcion", default=False,key="clearscreen")],
			[sg.Button("Seleccionar"), sg.Button("Salir")]]

	ventana = sg.Window('Menu Principal',layout)

	while True:
		event, values = ventana.read()
		#print(event, values)
		if event == sg.WIN_CLOSED or event == 'Salir':
			print ("Ok adios")
			break
		if event == 'Seleccionar':
			if values["createRG"] == True:
				ventana.Minimize()
				crearRG.ejecutar()
				ventana.Normal()
			elif values["deleteRG"] == True:
				ventana.Minimize()
				eliminarRG.ejecutar()
				ventana.Normal()
			elif values["createVM"] == True:
				ventana.Minimize()
				crearVM.ejecutar()
				ventana.Normal()
			elif values["clearscreen"] == True:
				limpiar_pantalla()
			else:
				print ("No has seleccionado ninguna opcion")
			#crearresourcegroup(ventana=ventana)
			print ("Operacion realizada")

menuopc()
