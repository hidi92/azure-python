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
	global user
	global password
	global vmname
	global ventana

	resource_group_list = """az group  list --query "[].{Nombre_Grupo:name,Localizacion:location}" --output table"""
	run_command = Popen(resource_group_list,  shell=True ,stdout=subprocess.PIPE)
	output_command = run_command.stdout.read().decode("ascii") 
	#print(output_command)   

	sg.theme('Material1')
	layout = [[sg.Text("Introduce el grupo de recursos al que vas a asociar la VM")],
            [sg.Text('Grupo de Recursos', size=(15, 1)), sg.InputText(key='resourcegroup')],
			[sg.Text('Nombre de la VM', size=(15, 1)), sg.InputText(key='vmname')],
			[sg.Text('Nombre de usuario', size=(15, 1)), sg.InputText(key='user')],
			[sg.Text('Password de usuario', size=(15, 1)), sg.InputText(key='password')],
            [sg.Frame(layout=[
            [sg.Multiline(output_command, size=(50,10), disabled=True,key='output_command')]], title='Grupos en tu Suscripcion',title_color='red')],
            [sg.Button("Crear VM"), sg.Button("Salir")],
			[sg.Output(size=(110,30), background_color='black', text_color='white')]]

	ventana = sg.Window('Crear Maquina Virtual',layout)

	while True:  # Event Loop
		event, values = ventana.read()
		#print(event, values)
		if event == sg.WIN_CLOSED or event == 'Salir':
			print ("adios")
			break
		if event == 'Crear VM':
			resourcegroup = values['resourcegroup']
			vmname = values['vmname']
			user = values['user']
			password = values['password']
			createvm(ventana=ventana)
			print ("Operacion realizada")
			#Volvemos a cargar los grupos de la suscripcion
			ventana.Normal()
			run_command = Popen(resource_group_list,  shell=True ,stdout=subprocess.PIPE)
			output_command = run_command.stdout.read().decode("ascii")
			ventana['output_command'].update(output_command)
	ventana.close()




def createvm(timeout=None, ventana=None):

	create_vm = """az vm create \
        --resource-group """ +resourcegroup+ """ \
        --name """ +vmname+ """ \
        --image RedHat:RHEL:7-RAW:7.4.2018010506 \
        --vnet-name """ +vmname+ """ \
        --subnet """ +vmname+ """ \
        --admin-username """ +user+ """ \
        --admin-password """ +password+ """ \
        --size Standard_B1s"""

	print ("Comando lanzado: "+ create_vm)
	ventana.Minimize()
	sg.popup("Esta operacion tardara unos minutos, se minimazara la ventana mientras tanto")

	nop = None
	p = subprocess.Popen(create_vm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = ''
	for line in p.stdout:
		line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
		output += line
		print(line)
		ventana.refresh() if ventana else nop        # yes, a 1-line if, so shoot me

	retval = p.wait(timeout)
	return (retval, output)
