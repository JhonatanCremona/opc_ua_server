import time
import random
from opcua import Server
import socket
import threading
from threading import Thread
import asyncio
import random
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import math

# Obtener la IP local para configurar el endpoint
local_ip = socket.gethostbyname(socket.gethostname())

# Crear una instancia del servidor OPC UA
server = Server()

# Configurar el servidor
server.set_endpoint(f"opc.tcp://{local_ip}:4841")
server.set_server_name("Servidor OPC UA - Datos Dinámicos")

# Registrar un espacio de nombres para las variables
uri = "http://example.org/opcua/server/"
idx = server.register_namespace(uri)

objects = server.nodes.objects
server_interfaces = objects.add_object(idx, "ServerInterfaces")
server_interface_1 = server_interfaces.add_object(idx, "Server interface_1")

datos_complementarios = server_interface_1.add_object(idx, "datosComplementarios")
variables = [
    datos_complementarios.add_variable(idx, "pantalla_receta", True),
]

for var in datos_complementarios.get_variables():  
    var.set_writable()

datos_recetas = server_interface_1.add_object(idx, "RECETARIO")

recetas_info = [
    {"id": "1", "nombre": "Jamon tipo 1", "nroPaso": 1, "tipoFin": "TIEMPO"},
    {"id": "2", "nombre": "Jamon tipo 2", "nroPaso": 2, "tipoFin": "TEMPERATURA"},
    {"id": "3", "nombre": "Jamon tipo 3", "nroPaso": 3, "tipoFin": "TIEMPO"},
    {"id": "4", "nombre": "Jamon tipo 4", "nroPaso": 4, "tipoFin": "TEMPERATURA"},
]

for i, receta in enumerate(recetas_info, start=1):
    receta_node = datos_recetas.add_object(idx, f"{i}")
    variables = [
        receta_node.add_variable(idx, "id", receta["id"]),
        receta_node.add_variable(idx, "nombre", receta["nombre"]),
        receta_node.add_variable(idx, "nroPaso", receta["nroPaso"]),
        receta_node.add_variable(idx, "tipoFin", receta["tipoFin"]),
    ]
    for var in variables:
        var.set_writable()

cocina1_obj = server_interface_1.add_object(idx, "COCINA-1-L1")
variables = [
    cocina1_obj.add_variable(idx, "COCINA_NUMERO", 1),
    cocina1_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina1_obj.add_variable(idx, "RECETA_NOMBRE", "Jamon"),
    cocina1_obj.add_variable(idx, "ESTADO_EQUIPO", "FINALIZADO"),
    cocina1_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina1_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina1_obj.add_variable(idx, "TIEMPO_TRANS", datetime.now()),
    cocina1_obj.add_variable(idx, "TEMP_AGUA", 1),
    cocina1_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina1_obj.add_variable(idx, "TEMP_INGRESO", 1),
    cocina1_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina1_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina1_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    cocina1_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina1_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina1_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina1_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina1_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina1_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina1_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina1_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina1_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina1_obj.add_variable(idx, "CICLO_LOTE", "LOTE C1"),
]

for var in cocina1_obj.get_variables():  
    var.set_writable()

cocina2_obj = server_interface_1.add_object(idx, "COCINA-2-L1")
variables = [
    cocina2_obj.add_variable(idx, "COCINA_NUMERO", 2),
    cocina2_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina2_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    cocina2_obj.add_variable(idx, "ESTADO_EQUIPO", "INACTIVO"),
    cocina2_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina2_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina2_obj.add_variable(idx, "TIEMPO_TRANS", datetime.now()),
    cocina2_obj.add_variable(idx, "TEMP_AGUA", 1),
    cocina2_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina2_obj.add_variable(idx, "TEMP_INGRESO", 2),
    cocina2_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina2_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina2_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    cocina2_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina2_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina2_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina2_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina2_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina2_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina2_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina2_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina2_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina2_obj.add_variable(idx, "CICLO_LOTE", "LOTE C2"),
]

for var in cocina2_obj.get_variables():  
    var.set_writable()

cocina3_obj = server_interface_1.add_object(idx, "COCINA-3-L1")
variables = [
    cocina3_obj.add_variable(idx, "COCINA_NUMERO", 3),
    cocina3_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina3_obj.add_variable(idx, "RECETA_NOMBRE", "Paleta"),
    cocina3_obj.add_variable(idx, "ESTADO_EQUIPO", "FINALIZADO"),
    cocina3_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina3_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina3_obj.add_variable(idx, "TIEMPO_TRANS", datetime.now()),
    cocina3_obj.add_variable(idx, "TEMP_AGUA", 1),
    cocina3_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina3_obj.add_variable(idx, "TEMP_INGRESO", 3),
    cocina3_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina3_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina3_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    cocina3_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina3_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina3_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina3_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina3_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina3_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina3_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina3_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina3_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina3_obj.add_variable(idx, "CICLO_LOTE", "LOTE C3"),
]

for var in cocina3_obj.get_variables():  
    var.set_writable()

enfriador1_obj = server_interface_1.add_object(idx, "ENFRIADOR-1-L1")
variables = [
    enfriador1_obj.add_variable(idx, "ENFRIADOR_NUMERO", 7),
    enfriador1_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador1_obj.add_variable(idx, "RECETA_NOMBRE", "Jamon"),
    enfriador1_obj.add_variable(idx, "ESTADO_EQUIPO", "FALLA"),
    enfriador1_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador1_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador1_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador1_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador1_obj.add_variable(idx, "TEMP_AGUA", 1),
    enfriador1_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador1_obj.add_variable(idx, "TEMP_INGRESO", 1),
    enfriador1_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador1_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador1_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador1_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador1_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador1_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador1_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador1_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador1_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador1_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador1_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador1_obj.add_variable(idx, "CICLO_LOTE", "LOTE E1"),
]

for var in enfriador1_obj.get_variables():  
    var.set_writable()

enfriador2_obj = server_interface_1.add_object(idx, "ENFRIADOR-2-L1")
variables = [
    enfriador2_obj.add_variable(idx, "ENFRIADOR_NUMERO", 8),
    enfriador2_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador2_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    enfriador2_obj.add_variable(idx, "ESTADO_EQUIPO", "OPERATIVO"),
    enfriador2_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador2_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador2_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador2_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador2_obj.add_variable(idx, "TEMP_AGUA", 1),
    enfriador2_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador2_obj.add_variable(idx, "TEMP_INGRESO", 2),
    enfriador2_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador2_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador2_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador2_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador2_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador2_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador2_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador2_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador2_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador2_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador2_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador2_obj.add_variable(idx, "CICLO_LOTE", "LOTE E2"),
]

for var in enfriador2_obj.get_variables():  
    var.set_writable()

enfriador3_obj = server_interface_1.add_object(idx, "ENFRIADOR-3-L1")
variables = [
    enfriador3_obj.add_variable(idx, "ENFRIADOR_NUMERO", 9),
    enfriador3_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador3_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    enfriador3_obj.add_variable(idx, "ESTADO_EQUIPO", "OPERATIVO"),
    enfriador3_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador3_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador3_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador3_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador3_obj.add_variable(idx, "TEMP_AGUA", 1),
    enfriador3_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador3_obj.add_variable(idx, "TEMP_INGRESO", 3),
    enfriador3_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador3_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador3_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador3_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador3_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador3_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador3_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador3_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador3_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador3_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador3_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador3_obj.add_variable(idx, "CICLO_LOTE", "LOTE E3"),
]

for var in enfriador3_obj.get_variables():  
    var.set_writable()

enfriador4_obj = server_interface_1.add_object(idx, "ENFRIADOR-4-L1")
variables = [
    enfriador4_obj.add_variable(idx, "ENFRIADOR_NUMERO", 10),
    enfriador4_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador4_obj.add_variable(idx, "RECETA_NOMBRE", "Paleta"),
    enfriador4_obj.add_variable(idx, "ESTADO_EQUIPO", "INACTIVO"),
    enfriador4_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador4_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador4_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador4_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador4_obj.add_variable(idx, "TEMP_AGUA", 1),
    enfriador4_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador4_obj.add_variable(idx, "TEMP_INGRESO", 4),
    enfriador4_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador4_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador4_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador4_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador4_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador4_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador4_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador4_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador4_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador4_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador4_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador4_obj.add_variable(idx, "CICLO_LOTE", "LOTE E4"),
]

for var in enfriador4_obj.get_variables():  
    var.set_writable()

server_interface_2 = server_interfaces.add_object(idx, "Server interface_2")

cocina4_obj = server_interface_2.add_object(idx, "COCINA-4-L2")
variables = [
    cocina4_obj.add_variable(idx, "COCINA_NUMERO", 4),
    cocina4_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina4_obj.add_variable(idx, "RECETA_NOMBRE", "Paleta"),
    cocina4_obj.add_variable(idx, "ESTADO_EQUIPO", "OPERATIVO"),
    cocina4_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina4_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina4_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    cocina4_obj.add_variable(idx, "TEMP_AGUA", 2),
    cocina4_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina4_obj.add_variable(idx, "TEMP_INGRESO", 4),
    cocina4_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina4_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina4_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    cocina4_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina4_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina4_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina4_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina4_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina4_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina4_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina4_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina4_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina4_obj.add_variable(idx, "CICLO_LOTE", "LOTE C4"),
]

for var in cocina4_obj.get_variables():  
    var.set_writable()

cocina5_obj = server_interface_2.add_object(idx, "COCINA-5-L2")
variables = [
    cocina5_obj.add_variable(idx, "COCINA_NUMERO", 5),
    cocina5_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina5_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    cocina5_obj.add_variable(idx, "ESTADO_EQUIPO", "FINALIZADO"),
    cocina5_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina5_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina5_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    cocina5_obj.add_variable(idx, "TEMP_AGUA", 2),
    cocina5_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina5_obj.add_variable(idx, "TEMP_INGRESO", 5),
    cocina5_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina5_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina5_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    cocina5_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina5_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina5_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina5_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina5_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina5_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina5_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina5_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina5_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina5_obj.add_variable(idx, "CICLO_LOTE", "LOTE C5"),
]

for var in cocina5_obj.get_variables():  
    var.set_writable()

cocina6_obj = server_interface_2.add_object(idx, "COCINA-6-L2")
variables = [
    cocina6_obj.add_variable(idx, "COCINA_NUMERO", 6),
    cocina6_obj.add_variable(idx, "RECETA_NUMERO", 1),
    cocina6_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    cocina6_obj.add_variable(idx, "ESTADO_EQUIPO", "INACTIVO"),
    cocina6_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    cocina6_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    cocina6_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    cocina6_obj.add_variable(idx, "TEMP_AGUA", 2),
    cocina6_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    cocina6_obj.add_variable(idx, "TEMP_INGRESO", 6),
    cocina6_obj.add_variable(idx, "TEMP_CHILLER", 1),
    cocina6_obj.add_variable(idx, "NIVEL_AGUA", 1),
    cocina6_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    
    
    cocina6_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    cocina6_obj.add_variable(idx, "CARGA_AGUA", True),
    cocina6_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    cocina6_obj.add_variable(idx, "VAPOR_SERPENTINA", False),
    cocina6_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    cocina6_obj.add_variable(idx, "VAPOR_VIVO", True),
    cocina6_obj.add_variable(idx, "VAPOR_VIVO_ACC", True),
    cocina6_obj.add_variable(idx, "TAPA_ESTADO", True),
    cocina6_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    cocina6_obj.add_variable(idx, "CICLO_LOTE", "LOTE C6"),
]

for var in cocina6_obj.get_variables():  
    var.set_writable()

enfriador5_obj = server_interface_2.add_object(idx, "ENFRIADOR-5-L2")
variables = [
    enfriador5_obj.add_variable(idx, "ENFRIADOR_NUMERO", 11),
    enfriador5_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador5_obj.add_variable(idx, "RECETA_NOMBRE", "Jamon"),
    enfriador5_obj.add_variable(idx, "ESTADO_EQUIPO", "OPERATIVO"),
    enfriador5_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador5_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador5_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador5_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador5_obj.add_variable(idx, "TEMP_AGUA", 2),
    enfriador5_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador5_obj.add_variable(idx, "TEMP_INGRESO", 5),
    enfriador5_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador5_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador5_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador5_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador5_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador5_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador5_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador5_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador5_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador5_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador5_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador5_obj.add_variable(idx, "CICLO_LOTE", "LOTE E5"),
]

for var in enfriador5_obj.get_variables():  
    var.set_writable()

enfriador6_obj = server_interface_2.add_object(idx, "ENFRIADOR-6-L2")
variables = [
    enfriador6_obj.add_variable(idx, "ENFRIADOR_NUMERO", 12),
    enfriador6_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador6_obj.add_variable(idx, "RECETA_NOMBRE", "Pate"),
    enfriador6_obj.add_variable(idx, "ESTADO_EQUIPO", "INACTIVO"),
    enfriador6_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador6_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador6_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador6_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador6_obj.add_variable(idx, "TEMP_AGUA", 2),
    enfriador6_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador6_obj.add_variable(idx, "TEMP_INGRESO", 6),
    enfriador6_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador6_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador6_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador6_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador6_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador6_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador6_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador6_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador6_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador6_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador6_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador6_obj.add_variable(idx, "CICLO_LOTE", "LOTE E6"),
]

for var in enfriador6_obj.get_variables():  
    var.set_writable()

enfriador7_obj = server_interface_2.add_object(idx, "ENFRIADOR-7-L2")
variables = [
    enfriador7_obj.add_variable(idx, "ENFRIADOR_NUMERO", 13),
    enfriador7_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador7_obj.add_variable(idx, "RECETA_NOMBRE", "Jamon"),
    enfriador7_obj.add_variable(idx, "ESTADO_EQUIPO", "OPERATIVO"),
    enfriador7_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador7_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador7_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador7_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador7_obj.add_variable(idx, "TEMP_AGUA", 2),
    enfriador7_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador7_obj.add_variable(idx, "TEMP_INGRESO", 7),
    enfriador7_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador7_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador7_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador7_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador7_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador7_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador7_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador7_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador7_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador7_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador7_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador7_obj.add_variable(idx, "CICLO_LOTE", "LOTE E7"),
]

for var in enfriador7_obj.get_variables():  
    var.set_writable()

enfriador8_obj = server_interface_2.add_object(idx, "ENFRIADOR-8-L2")
variables = [
    enfriador8_obj.add_variable(idx, "ENFRIADOR_NUMERO", 14),
    enfriador8_obj.add_variable(idx, "RECETA_NUMERO", 1),
    enfriador8_obj.add_variable(idx, "RECETA_NOMBRE", "Paleta"),
    enfriador8_obj.add_variable(idx, "ESTADO_EQUIPO", "FALLA"),
    enfriador8_obj.add_variable(idx, "CANTIDAD_TORRES", 1),
    enfriador8_obj.add_variable(idx, "CICLO_TIPO_FIN", "TIEMPO"),

    enfriador8_obj.add_variable(idx, "RECETA_PASO_ACTUAL", 1),
    enfriador8_obj.add_variable(idx, "TIEMPO_TRANS", 1),
    enfriador8_obj.add_variable(idx, "TEMP_AGUA", 2),
    enfriador8_obj.add_variable(idx, "TEMP_PRODUCTO", 1),
    enfriador8_obj.add_variable(idx, "TEMP_INGRESO", 8),
    enfriador8_obj.add_variable(idx, "TEMP_CHILLER", 1),
    enfriador8_obj.add_variable(idx, "NIVEL_AGUA", 1),

    enfriador8_obj.add_variable(idx, "FILTRO_SUCCION_AGUA", False),
    enfriador8_obj.add_variable(idx, "CARGA_AGUA", False),
    enfriador8_obj.add_variable(idx, "BOMBA_CENTRIFUGA", False),
    enfriador8_obj.add_variable(idx, "VALVULA_AMONIACO", True),
    enfriador8_obj.add_variable(idx, "VAPOR_SERPENTINA_ACC", True),
    enfriador8_obj.add_variable(idx, "VAPOR_VIVO_LIM", True),
    enfriador8_obj.add_variable(idx, "VAPOR_VIVO_LIM_ACC", True),
    enfriador8_obj.add_variable(idx, "TAPA_ESTADO", True),
    enfriador8_obj.add_variable(idx, "TAPA_ESTADO_ACC", "REPOSO"),
    enfriador8_obj.add_variable(idx, "CICLO_LOTE", "LOTE E8"),
]

for var in enfriador8_obj.get_variables():  
    var.set_writable()

def ciclo_coccion(equipo_object, inicio_en_minuto=0):
    maquina_nodos = equipo_object
    while True:
    # Variables de simulación
        nivel_actual = 1600
        temp_producto = 5
        temp_agua = 24
        serpentina_on = True
        on_duracion = random.randint(10, 25)
        off_duracion = random.randint(15, 30)
        ciclo_serpentina = 0

        # Para graficar
        minutos = []
        temperaturas_producto = []
        temperaturas_agua = []
        niveles_agua = []

        step = inicio_en_minuto
        while step <= 180:  # total de minutos simulados (3 horas)
            if step < 30:
                estado = "PRE OPERATIVO"
            elif step < 170:
                estado = "OPERATIVO"
            else:
                estado = "FINALIZADO"
                time.sleep(60)

            for nod in maquina_nodos:
                nombre = nod.get_browse_name().Name

                if nombre == "ESTADO_EQUIPO":
                    nod.set_value(estado)

                elif nombre == "TEMP_AGUA":
                    if estado == "PRE OPERATIVO":
                        temp_agua = 24 + ((85 - 24) / 30) * step
                    elif estado == "OPERATIVO":
                        base_temp = 80 + ((90 - 80) / 140) * (step - 30)
                        temp_agua = base_temp + random.uniform(-1, 1)
                    nod.set_value(round(temp_agua, 2))
                    temperaturas_agua.append(round(temp_agua, 2))

                elif nombre == "TEMP_PRODUCTO":
                    t = step - 30
                    if estado in ["PRE OPERATIVO", "OPERATIVO", "FINALIZADO"]:
                        L = 70
                        k = 0.09
                        x0 = 45
                        temp_producto = 5 + L / (1 + math.exp(-k * (t - x0)))
                        temp_producto = min(temp_producto, 75)
                    nod.set_value(round(temp_producto, 2))
                    temperaturas_producto.append(round(temp_producto, 2))

                elif nombre == "NIVEL_AGUA":
                    if estado == "PRE OPERATIVO":
                        nivel_actual = random.uniform(1560, 1650)
                    elif estado == "OPERATIVO":
                        if step < 40:
                            nivel_actual = 1650 + ((2000 - 1650) / 10) * (step - 30)
                        else:
                            nivel_actual = random.uniform(1900, 2000)
                    else:
                        nivel_actual = max(1800, nivel_actual - random.uniform(1, 3))
                    nod.set_value(round(nivel_actual, 2))
                    niveles_agua.append(round(nivel_actual, 2))

                elif nombre == "VAPOR_VIVO":
                    vapor_activo = step < 30
                    nod.set_value(vapor_activo)

                elif nombre == "VALV_SERPENTINA":
                    ciclo_serpentina += 1
                    if serpentina_on and ciclo_serpentina >= on_duracion:
                        serpentina_on = False
                        ciclo_serpentina = 0
                        off_duracion = random.randint(15, 30)
                    elif not serpentina_on and ciclo_serpentina >= off_duracion:
                        serpentina_on = True
                        ciclo_serpentina = 0
                        on_duracion = random.randint(10, 25)
                    nod.set_value(serpentina_on)

            minutos.append(step)
            step += 1
            time.sleep(60)

            if step > 180:
                step = 0
                nivel_actual = 1600
                temp_producto = 5
                temp_agua = 24
                serpentina_on = True
                on_duracion = random.randint(10, 25)
                off_duracion = random.randint(15, 30)
                ciclo_serpentina = 0

                # 🧼 Limpiar las listas de datos para graficar (opcional)
                minutos.clear()
                temperaturas_producto.clear()
                temperaturas_agua.clear()
                niveles_agua.clear()

"""
def ciclo_coccion(equipo_object):
    maquina_nodos = equipo_object

    while True:
        # Variables de simulación
        nivel_actual = 1600
        temp_producto = 5
        temp_agua = 24
        serpentina_on = True
        on_duracion = random.randint(10, 25)
        off_duracion = random.randint(15, 30)
        ciclo_serpentina = 0

        # Para graficar
        minutos = []
        temperaturas_producto = []
        temperaturas_agua = []
        niveles_agua = []

        step = 0
        while step <= 180:
            if step < 30:
                estado = "PRE CALENTAMIENTO"
            elif step < 170:
                estado = "OPERATIVO"
            else:
                estado = "FINALIZADO"

            for nod in maquina_nodos:
                nombre = nod.get_browse_name().Name

                if nombre == "ESTADO_EQUIPO":
                    nod.set_value(estado)

                elif nombre == "TEMP_AGUA":
                    if estado == "PRE CALENTAMIENTO":
                        temp_agua = 24 + ((85 - 24) / 30) * step
                    elif estado == "OPERATIVO":
                        base_temp = 80 + ((90 - 80) / 140) * (step - 30)
                        temp_agua = base_temp + random.uniform(-1, 1)
                    nod.set_value(round(temp_agua, 2))
                    temperaturas_agua.append(round(temp_agua, 2))

                elif nombre == "TEMP_PRODUCTO":
                    t = step - 30
                    if estado in ["PRE CALENTAMIENTO", "OPERATIVO", "FINALIZADO"]:
                        L = 70
                        k = 0.09
                        x0 = 45
                        temp_producto = 5 + L / (1 + math.exp(-k * (t - x0)))
                        temp_producto = min(temp_producto, 75)
                    nod.set_value(round(temp_producto, 2))
                    temperaturas_producto.append(round(temp_producto, 2))

                elif nombre == "NIVEL_AGUA":
                    if estado == "PRE CALENTAMIENTO":
                        nivel_actual = random.uniform(1560, 1650)
                    elif estado == "OPERATIVO":
                        if step < 40:
                            nivel_actual = 1650 + ((2000 - 1650) / 10) * (step - 30)
                        else:
                            nivel_actual = random.uniform(1900, 2000)
                    else:
                        nivel_actual = max(1800, nivel_actual - random.uniform(1, 3))
                    nod.set_value(round(nivel_actual, 2))
                    niveles_agua.append(round(nivel_actual, 2))

                elif nombre == "VAPOR_VIVO":
                    vapor_activo = step < 30
                    nod.set_value(vapor_activo)

                elif nombre == "VALV_SERPENTINA":
                    ciclo_serpentina += 1
                    if serpentina_on and ciclo_serpentina >= on_duracion:
                        serpentina_on = False
                        ciclo_serpentina = 0
                        off_duracion = random.randint(15, 30)
                    elif not serpentina_on and ciclo_serpentina >= off_duracion:
                        serpentina_on = True
                        ciclo_serpentina = 0
                        on_duracion = random.randint(10, 25)
                    nod.set_value(serpentina_on)

            minutos.append(step)
            step += 1
            time.sleep(0.1)

            if step > 180:
                step = 0
                nivel_actual = 1600
                temp_producto = 5
                temp_agua = 24
                serpentina_on = True
                on_duracion = random.randint(10, 25)
                off_duracion = random.randint(15, 30)
                ciclo_serpentina = 0

                # 🧼 Limpiar las listas de datos para graficar (opcional)
                minutos.clear()
                temperaturas_producto.clear()
                temperaturas_agua.clear()
                niveles_agua.clear()

        # 📊 GRAFICAR al final del ciclo
        plt.figure(figsize=(12, 6))
        plt.plot(minutos, temperaturas_producto, label="TEMP_PRODUCTO (°C)", color="orange", linewidth=2)
        plt.plot(minutos, temperaturas_agua, label="TEMP_AGUA (°C)", color="blue", linewidth=2)
        plt.axvline(30, color='gray', linestyle='--', label='Inicio Operativo')
        plt.axvline(170, color='gray', linestyle='--', label='Inicio Finalizado')
        plt.xlabel("Minutos")
        plt.ylabel("Valores")
        plt.title("Simulación de Cocción - TEMP_PRODUCTO / TEMP_AGUA / NIVEL_AGUA")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

"""


def simular_ciclo_enfriamiento(enfriador_obj, inicio_ciclo_min):
    inicio_simulacion = time.time()
    #inicio_ciclo_s = inicio_ciclo_min * 60
    #duracion_total_s = 4 * 60 * 60  # 4 horas = 14400 segundos
    inicio_ciclo_s = 1 * inicio_ciclo_min
    duracion_total_s = 240
    temp_producto = 0

    nivel_actual = 1600  # Inicializamos fuera del bucle
    while True:
        tiempo_actual_s = time.time() - inicio_simulacion

        if tiempo_actual_s < inicio_ciclo_s:
            time.sleep(1)
            continue

        tiempo_en_ciclo = tiempo_actual_s - inicio_ciclo_s
        if tiempo_en_ciclo > duracion_total_s:
            tiempo_en_ciclo = duracion_total_s

        tiempo_en_min = tiempo_en_ciclo / 60  # tiempo actual del ciclo en minutos

        # Estado del equipo según el momento del ciclo
        if tiempo_en_ciclo < 7200:
            estado = "PRE OPERATIVO"
        elif tiempo_en_ciclo < 14400:
            estado = "OPERATIVO"
        else:
            estado = "FINALIZADO"

        # TEMP_PRODUCTO: de 75°C a 7°C en 4 horas
        

        # TEMP_AGUA: baja de 25°C a 0°C linealmente
        temp_agua = max(25 - (25 * (tiempo_en_ciclo / duracion_total_s)), 0)

        # NIVEL_AGUA según estado
        if estado == "PRE OPERATIVO":
            nivel_actual = random.uniform(1560, 1650)

        elif estado == "OPERATIVO":
            if 120 <= tiempo_en_min < 130:
                # Subida lineal de 1650 a 2000 en 10 minutos
                nivel_actual = 1650 + ((tiempo_en_min - 120) / 10) * (2000 - 1650)
            else:
                nivel_actual = random.uniform(1900, 2000)

        elif estado == "FINALIZADO":
            nivel_actual = max(1800, nivel_actual - random.uniform(1, 3))  # Baja lentamente

        # Válvula de amoníaco activa durante las primeras 2 horas
        valvula_amoniaco = tiempo_en_ciclo < 7200
        if estado == "OPERATIVO":
            temp_producto = max(75 - (68 * (tiempo_en_ciclo / duracion_total_s)), 7)
            enfriador_obj.get_child("2:TEMP_PRODUCTO").set_value(round(temp_producto, 2))

        # Escritura en el servidor OPC UA
        
        enfriador_obj.get_child("2:TEMP_AGUA").set_value(round(temp_agua, 2))
        enfriador_obj.get_child("2:NIVEL_AGUA").set_value(round(nivel_actual, 2))
        enfriador_obj.get_child("2:VALVULA_AMONIACO").set_value(valvula_amoniaco)
        enfriador_obj.get_child("2:ESTADO_EQUIPO").set_value(estado)

        # DEBUG opcional
        print(f"[{int(tiempo_en_ciclo)}s] TEMP_PRODUCTO={temp_producto:.2f}°C | TEMP_AGUA={temp_agua:.2f}°C | NIVEL_AGUA={nivel_actual:.2f} | ESTADO={estado} | AMONIACO={valvula_amoniaco}")

        if tiempo_en_ciclo >= duracion_total_s:
            break

        time.sleep(1)



def simular_ciclo_enfriamiento2(enfriador_obj, inicio_ciclo_min):
    inicio_simulacion = time.time()
    inicio_ciclo_s = inicio_ciclo_min * 60
    duracion_total_s = 4 * 60 * 60  # 4 horas

    tiempos = []
    temp_producto_list = []
    temp_agua_list = []
    amoniaco_list = []

    while True:
        tiempo_actual_s = time.time() - inicio_simulacion

        if tiempo_actual_s < inicio_ciclo_s:
            time.sleep(10)
            continue

        tiempo_en_ciclo = tiempo_actual_s - inicio_ciclo_s
        if tiempo_en_ciclo > duracion_total_s:
            break  # termina la simulación

        temp_producto = max(75 - (68 * (tiempo_en_ciclo / duracion_total_s)), 7)
        temp_agua = max(25 - (25 * (tiempo_en_ciclo / duracion_total_s)), 0)
        nivel_agua = 100
        valvula_amoniaco = tiempo_en_ciclo <= 7200
        estado = "PRE_ENFRIAMIENTO" if tiempo_en_ciclo < 7200 else "OPERATIVO"

        enfriador_obj.get_child("2:TEMP_PRODUCTO").set_value(round(temp_producto, 2))
        enfriador_obj.get_child("2:TEMP_AGUA").set_value(round(temp_agua, 2))
        enfriador_obj.get_child("2:NIVEL_AGUA").set_value(nivel_agua)
        enfriador_obj.get_child("2:VALVULA_AMONIACO").set_value(valvula_amoniaco)
        enfriador_obj.get_child("2:ESTADO_EQUIPO").set_value(estado)

        print(f"[{int(tiempo_en_ciclo)}s] Enfriador: TEMP_PRODUCTO={temp_producto:.2f}°C | TEMP_AGUA={temp_agua:.2f}°C | ESTADO={estado} | AMONIACO={valvula_amoniaco}")

        # Registrar datos
        tiempos.append(tiempo_en_ciclo / 60)  # en minutos
        temp_producto_list.append(temp_producto)
        temp_agua_list.append(temp_agua)
        amoniaco_list.append(1 if valvula_amoniaco else 0)

        time.sleep(1)

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(tiempos, temp_producto_list, label="Temp Producto (°C)")
    plt.plot(tiempos, temp_agua_list, label="Temp Agua (°C)")
    plt.plot(tiempos, amoniaco_list, label="Válvula Amoniaco (ON=1)", linestyle='--')
    plt.title("Simulación Enfriador")
    plt.xlabel("Tiempo (minutos)")
    plt.ylabel("Valores")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def ejecutar_ciclo(args):
    objeto, inicio_min = args
    ciclo_coccion(objeto, inicio_en_minuto=inicio_min)

def ejecutar_enfriamiento(args):
    objeto, inicio_min = args
    simular_ciclo_enfriamiento(objeto, inicio_min)



if __name__ == "__main__":
    try:
        print("Servidor OPC UA iniciado en", server.endpoint)
        server.start()

        # ----- Definir tareas de cocción -----
        tareas_coccion = [
            (cocina1_obj.get_variables(), 0),
            (cocina2_obj.get_variables(), 60),
            (cocina3_obj.get_variables(), 160),
            (cocina4_obj.get_variables(), 80),
            (cocina5_obj.get_variables(), 60)
        ]

        # ----- Definir tareas de enfriamiento -----
        tareas_enfriamiento = [
            (enfriador1_obj.get_variables(), 10),
            (enfriador2_obj.get_variables(), 10),
            (enfriador3_obj.get_variables(), 10),
            (enfriador4_obj.get_variables(), 10),
            (enfriador5_obj.get_variables(), 10),
            (enfriador6_obj.get_variables(), 10),
            (enfriador7_obj.get_variables(), 10),
            (enfriador8_obj.get_variables(), 10),
        ]
        
        #simular_ciclo_enfriamiento2(enfriador1_obj, 1)
        simular_ciclo_enfriamiento(enfriador2_obj, 2)
        # Ejecutar todas las tareas en paralelo
        with ThreadPoolExecutor() as executor:
            executor.map(ejecutar_ciclo, tareas_coccion)
            executor.map(ejecutar_enfriamiento, tareas_enfriamiento)

    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
        server.stop()
        print("Servidor detenido correctamente.")
