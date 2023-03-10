"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def comparar_impuestos(impuesto_1, impuesto_2):
    if compare(impuesto_1[0], impuesto_2[0])==1:
        return True
    elif compare(impuesto_1[0], impuesto_2[0])==-1:
        return False
    else:
        comparar_impuestos(impuesto_1[0], impuesto_2[0])
        if comparar_impuestos(impuesto_1[0], impuesto_2[0])==0:
            return False

def new_data_structs_arraylist():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=compare)

    return data_structs

def new_data_structs_linkedlist():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure="SINGLE_LINKED",
                                     cmpfunction=compare)

    return data_structs

# Funciones para agregar informacion al modelo
def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None
    }
    
    data_structs["data"] = lt.newList(datastructure="SINGLE_LINKED", cmpfunction=compare)

    return data_structs

def cambio(data_structs, tipo):
    
    if tipo == 1:
        data_structs["data"] = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compare)
    
    elif tipo == 2:
        data_structs = data_structs
    
    return data_structs
    

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], d)

    pass
    """ return data_structs """


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
def Insertion(list):
    lista=ins(list)
    return(lista)
def Selection(list):
    lista=se(list)
    return(lista)
def Shell(list):
    lista=sa(list)
    return(lista)
def Merge(list):
    lista=merg(list)
    return(lista)
def Quick(list):
    lista=quk(list)
    return(lista)


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["Año"] > data_2["Año"]:
        return 1
    elif data_1["Año"] < data_2["Año"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["Año"] > data_2["Año"]


def sort(data_structs, tipo):
    """
    Función encargada de ordenar la lista con los datos
    """
    #sa.sort(data_structs["data"], sort_criteria)
    if tipo == 1:
        lista = sa.sort(data_structs["data"], sort_criteria)
    elif tipo == 2:
        lista = ins.sort(data_structs["data"], sort_criteria)
    elif tipo == 3:
        lista = se.sort(data_structs["data"], sort_criteria)
    elif tipo == 4:
        lista =merg.sort(data_structs["data"], sort_criteria)
    elif tipo == 5:
        lista = quk.sort(data_structs["data"], sort_criteria)
    else:
        lista = print("No existe este ordenamiento")
    return lista

def cmp_impuestos_by_anio_CAE(empresas, filename):
   """
   Devuelve verdadero (True) si el año de impuesto 1 es menor que el de impuesto 2,
   en caso de que sean iguales tenga en cuenta el código de la actividad económica,
   de lo contrario devuelva falso (False).
   Args:
        impuesto 1: información del primer registro de impuestos que incluye el "Año" y el
        "Código actividad económica"
        impuesto 2: información del segundo registro de impuestos que incluye el "Año" y el
        "Código actividad económica"
   """ 
   
def cmp_id(va1, va2):
    id_key = "lista"
    if (va1[id_key] == va2[id_key]):
        return 0
    elif (va1[id_key] > va2[id_key]):
        return 1
    elif (va1[id_key] < va2[id_key]):
        return -1
    else:
        raise Exception

def load_data(struct, folder_name, file_name):
    if struct == 1:
        list = lt.newList("ARRAY_LIST",cmpfunction=cmp_id)

    if struct == 2:
        list = lt.newList("SINGLE_LINKED",cmpfunction=cmp_id)
    
    try:
        list_fpath = cf.os.path.join(cf.data_dir,
                                    folder_name,
                                    file_name,)
        print("Archivo ubicado en:", list_fpath)
        list_file = open(list_fpath, "r", encoding="utf-8")
        list_register = csv.DictReader(list_file, delimeter=",")
        for list in list_register:
            list_lt = add_data(list_lt, list)
        list_file.close()
        return list_lt
    except Exception as e:
        print(e)
        raise Exception 
