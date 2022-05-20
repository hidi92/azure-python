#importamos los mudulos externos necesarios para el funcionamiento de las diferentes utilidades
import sys
import os
import importlib
import subprocess
from subprocess import Popen
from subprocess import PIPE
import PySimpleGUI as sg

def ejecutar():

	global resourcegroup
	global region
	global ventana

	location_list = """az account list-locations --query "[].{DisplayName:displayName,Nombre_de_Region:name}" --output table"""
	run_command = Popen(location_list,  shell=True ,stdout=subprocess.PIPE)
	output_command = run_command.stdout.read().decode("ascii") 
	#print(output_command)
	
	sg.theme('Material1')
	layout = [[sg.Text("Introduce el nombre del grupo y la region donde la vas a crear")],
            [sg.Text('Nombre del Grupo', size=(17, 1)), sg.InputText(key='resourcegroup')],
			[sg.Text('Localizacion del Grupo', size=(17, 1)), sg.InputText(key='region')],
            [sg.Frame(layout=[
            [sg.Multiline(output_command ,size=(50,10), disabled=True,key='output_command')]], title='Localizaciones disponibles con tu Suscripcion',title_color='red')],
			[sg.Button("Crear Grupo"), sg.Button("Salir")],
			[sg.Output(size=(110,30), background_color='black', text_color='white')]]

	ventana = sg.Window('Crear Grupo de recursos',layout)

	while True:
		event, values = ventana.read()
		#print(event, values)
		if event == sg.WIN_CLOSED or event == 'Salir':
			print ("Ok adios")
			break
		if event == 'Crear Grupo':
			resourcegroup = values['resourcegroup']
			region = values['region']
			crearresourcegroup(ventana=ventana)
			print ("Operacion realizada")
	ventana.close()

def crearresourcegroup(timeout=None, ventana=None):

	crear_rg = ("az group create -n " + resourcegroup + " -l " + region)
	print ("Comando lanzado: "+ crear_rg)
	nop = None
	p = subprocess.Popen(crear_rg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = ''
	for line in p.stdout:
		line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
		output += line
		print(line)
		ventana.refresh() if ventana else nop        # yes, a 1-line if, so shoot me

	retval = p.wait(timeout)
	return (retval, output)
