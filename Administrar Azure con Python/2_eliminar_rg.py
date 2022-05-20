#importamos los mudulos externos necesarios para el funcionamiento de las diferentes utilidades
import sys
import os
import importlib
import PySimpleGUI as sg
import subprocess
from subprocess import Popen
from subprocess import PIPE

def ejecutar():
    global resourcegroup
    global ventana

    resource_group_list = """az group  list --query "[].{Nombre_Grupo:name,Localizacion:location}" --output table"""
    run_command = Popen(resource_group_list,  shell=True ,stdout=subprocess.PIPE)
    output_command = run_command.stdout.read().decode("ascii") 
    #print(output_command)   

    sg.theme('Material1')
    layout = [[sg.Text("Introduce el grupo que quieres eliminar")],
            [sg.Text('Nombre del Grupo', size=(13, 1)), sg.InputText(key='resourcegroup')],
            [sg.Frame(layout=[
            [sg.Multiline(output_command, size=(50,10), disabled=True,key='output_command')]], title='Grupos en tu Suscripcion',title_color='red')],
            [sg.Button("Borrar Grupo"), sg.Button("Salir")],
            [sg.Output(size=(110,30), background_color='black', text_color='white')]]

    ventana = sg.Window('Eliminar Grupo de recursos',layout)

    while True:  # Event Loop
        event, values = ventana.read()
        #print(event, values)
        if event == sg.WIN_CLOSED or event == 'Salir':
            print ("adios")
            break
        if event == 'Borrar Grupo':
            resourcegroup = values['resourcegroup']
            deleteresourcegroup(ventana=ventana)
            print ("Operacion realizada")
            #Volvemos a cargar los grupos de la suscripcion
            ventana.Normal()
            run_command = Popen(resource_group_list,  shell=True ,stdout=subprocess.PIPE)
            output_command = run_command.stdout.read().decode("ascii")
            ventana['output_command'].update(output_command)
    ventana.close()


def deleteresourcegroup(timeout=None, ventana=None):

    eliminiar_rg = ("az group delete -n " + resourcegroup + " -y")
    print ("Comando lanzado: "+ eliminiar_rg)
    ventana.Minimize()
    sg.popup("Esta operacion tardara unos minutos, se minimazara la ventana mientras tanto")
    nop = None
    p = subprocess.Popen(eliminiar_rg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        ventana.refresh() if ventana else nop        # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)
