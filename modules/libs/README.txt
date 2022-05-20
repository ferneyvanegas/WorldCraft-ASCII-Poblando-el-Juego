====================================================
ORIGEN LIBRERÍA
====================================================
El contenido de esta carpeta son módulos utilizados en la 
anterior vesión de WorldCraft ASCII (Reto 4). 

Su documentación se encuentra detallada en dicha entrega.

====================================================
SOBRE LA INTEGRACIÓN
====================================================
Para poderla integrar con esta versión de WorldCraft ASCII
es probable que se hayan hecho algunas adaptaciones mínimas,
sin embargo su lógica y propósito se mantienen.

====================================================
POR QUÉ INTEGRAR ESTA LIBRERÍA?
====================================================
Particularmente se decidió la reutilización de las librerías
por cuanto uno de los requerimientos era la construcción de los
muros, lo cual ya se había logrado en la entrega del reto 4.

====================================================
DIMENSIONES
====================================================
La dimensión del juego por defecto es 50x50. Sin embargo, si se 
quiere maniobrar con dimensiones diferentes, sírvase descomentar 
la línea 23 y comentar la línea 24 de la función get_walls en
game_walls.py