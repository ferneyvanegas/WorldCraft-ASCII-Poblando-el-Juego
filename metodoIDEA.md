# WORLD CRAFT ASCII: Poblando el juego
> **Ferney Vanegas Hernández**

>**Misión TIC 2022**

>**Reto 5**


##  **Contexto**
 Los jugadores aceptados y asignados a un mundo en el popular juego WorldCraft: ASCII llegan al mundo (en el juego), pero este se encuentra vacío.

## PROBLEMA (I)
### **El problema**
Los jugadores de World ASCII llegan a un mundo vacío sin criaturas, ni posición de su ávatar, ni información del juego.
### **Objetivos**
* Generar un número dado de criaturas pasivas y otro de criaturas hostiles.
* Cada criatura debe tener un *'Perfil'* (Información de identificación)
* El jugador también debe poseer un *'Perfil'* (Información de identificación)
* Construir el mundo con muros, criaturas y el jugador
* Reportar el estado del juego
###  **Interesados**
* Los jugadores y aficionados del juego WorldCraft ASCII
### **Restricciones**
* La cantidad total de criaturas (pasivas más hostiles) no puede ser mayor que 50
* Si la mayor cantidad de criaturas son 50, por cada tipo debe haber al menos la misma cantidad disponible
* Los muros, criaturas y jugador no pueden ocupar la misma coordenada en el juego

## DEFINICIÓN (D)
### **Información Suministrada**
* Hay criaturas Pasivas
* Hay criaturas Hostiles
* Las criaturas deben ser escogidas aleatoriamente de una lista de criaturas (Pasivas u Hostiles)
* Cada critarura debe tener un perfil con la siguiente info: 
    * Tipo (Pasiva / Hostil)
    * Nombre
    * Símbolo (carácter que lo representa)
    * Fila donde debe aparecer (generada aleatoriamente)
    * Columna donde debe aparecer (generada aleatoriamente)
    * Fecha y hora en la que aparece (tomada del sistema)
* El jugador también debe tener un perfil con la siguiente info:
    * Tipo (Jugador)
    * Alias
    * Fila donde debe aparecer (generada aleatoriamente)
    * Columna donde debe aparecer (generada aleatoriamente)
    * Fecha y hora en la que aparece (tomada del sistema)
    * Numero de corazones (inicia con 10)
* Debe dibujarse el mundo **con los muros**
* Debe dibujarse en el mundo las criauras y el jugador
* En algún lugar del mundo debe mostrarse la siguiente información del juego:
    * Número total de muros
    * Vidas del jugador
    * Número total de criaturas en el juego

### **Información Requerida**
* Tuplas en Python
* Diccionarios en Python
* Claridad en los conceptos de pilas y colas para implementar en Python
* Listas
* Funciones
* Librerias ó Módulos (importacioń)
* Reutilización de código

### **Dividir el problema en subproblemas**
* Definir un repositorio de criaturas (de donde tomarlas)
* Definir un repositorio de símbolos para criaturas
* Definir un repositorio de Alias para **EMULAR** al jugador
* Integrar versiones anteriores del Programa para construir el mundo
* Agregar a las criaturas
    * Validar que no queden entre los muros
    * Validar que no queden una encima de otra
    * Validar que queden en el tablero
    * Validar que quepan en el mundo
* Agregar al jugador en el juego
    * Validar que no quede entre los muros
    * Validar que no quede encima de una criatura
    * Validar que quede en el tablero
* Asignar un lugar para mostrar los datos de juego

## Estrategia (E)
### **Ejemplo particular**
El siguiente ejemplo muestra una emulación de resultados para contruir un mundo con criaturas, el jugador y estadísticas:

*Datos*
![img_ej_1](img/Ej1_1.jpg 'Ejemplo imagen 1')
*Gráfica*
![img_ej_2](img/Ej1_2.jpg 'Ejemplo imagen 2') 
 
### **Estrategia de solución**
1. Obtener las colas (hostiles y pasivas)
2. Generar los diccionarios (hostiles y pasivos) en listas
3. Generar diccionario del jugador
4. Integrar librerías pasadas para obtener listado de coordenadas
5. Renderizar tablero
    * Muros
    * Criaturas
    * Jugador
    * Mostrar información del juego

*La siguiente gráfica es una representación de la estratégia:*
![img_estrategia](img/Estrategia.jpg 'Estrategia') 

Adicionalmente, con el fin de evitar que las criaturas, el jugador y el muro queden uno encima del otro, registraré cada posición activa en un listado frente al cual se comparará antes de generar una posición en fila y columna.
 
 
## Algoritmos (A)

### Algoritmo get_hostile_creatures
*Parámetros: cant*
* Funcion h_creatures<- get_hostile_creatures() :
    * cant_creatures = 50
    * /*h_creatures contendrá 50 estilos de criaturas (nombres)*/
    * Dimensionar h_creatures[cant_creatures]
    * Retornar Llamar barajar(0 hasta h_creatures[cant])
* FinFuncion
***
### Algoritmo get_passive_creatures
*Parámetros: cant*
* Funcion p_creatures<- get_postile_creatures() :
    * cant_creatures = 50
    * /*p_creatures contendrá 50 estilos de criaturas (nombres)*/
    * Dimensionar p_creatures[cant_creatures]
    * Retornar Llamar barajar(0 hasta p_creatures[cant])
* FinFuncion
*** 
### Algoritmo create_creatures
*Parámetros: cant_p, cant_h*
* Funcion p_creatures, h_creatures <- create_creatures ():
    * p_creatures = Llamar get_passive_creatures(cant)
    * h_creatures = Llamar get_hostile_creatures(cant)
    * Retornar p_creatures, h_creatures
* FinFuncion
***
### Algoritmo creatures
*Parámetros: Ninguno*
* Funcion creatures <- creatures()
    * cant_h_creatures = 50
    * cant_p_creatures = 50
    * Mientras cant_h_creatures + cant_p_creatures > 50 Entonces:
        * Escribir 'Creacioń de Criaturas. No pueden ser más de 50 en total'
        * Escribir 'Ingresa el número de criaturas hostiles'
        * Leer cant_h_creatures
        * Escribir 'Ingresa el número de criaturas pasivas'
        * Leer cant_p_creatures
    * FinMientras
    * p_creatures, h_creatures = create_creatures(cant_p_creatures, cant_h_creatures)
    * symbols_p_creatures, symbols_h_creatures = Llamar get_symbols_creatures(cant_p_creatures, cant_h_creatures)
    * Dimensionar creatures[4]
    * creatures[0] = [h_creatures]
    * creatures[1] = [p_creatures]
    * creatures[2] = [symbols_h_creatures]
    * creatures[3] = [symbols_p_creatures]
    * Retornar creatures
* FinFuncion
***
### Algoritmo get_symbols_creatures()
*Parámetros: cant_p, cant_p*
* Funcion symbols_creatures <- get_symbols_creatures()
    * ascii = 33
    * Para cont<-0 hasta cant_p con Paso 1 Haga:
        * /* ASCII es una librería del lenguage que a partir de un número obtiene caracteres ascii*/
        * symbols_p[cont]=Llamar ASCII(ascii)
        * ascii+=1
    * FinPara

    * ascii = 84
    * Para cont<-0 hasta cant_h con Paso 1 Haga:
        * /* ASCII es una librería del lenguage que a partir de un número obtiene caracteres ascii*/
        * symbols_p[cont]=Llamar ASCII(ascii)
        * ascii+=1
    * FinPara
    * Retornar symbols_p, symbols_h
* FinFuncion
***
### Algoritmo dim_creatures
*Parámetros: Dimesionar creatures, general_coords*
* Funcion dim_creatures<- dim_creatures():
    * Dimensionar dim_creatures[cant_creatures]
    * Para i<-0 hasta 1 con Paso 1 Haga:
        * cant_creatures = Llamar Longitud(creatures[i])
        * Si i == 0 Entonces:
            * typ = 'passive'
        * SiNo:
            * typ = 'hostile'
        * Para j<-0 hasta cant_creatures con Paso 1 Hacer:
            * inserted = False
            * Dimensionar coord[2]
            * Mientras inserted == False Haga:
                * coord[0] = Azar(0 hasta general_coords['dim'])
                * coord[1] = Azar(0 hasta general_coords['dim'])
                * Si coord in general_coords['coords'] == False
                    * general_coords['coords'] = general_coords['coords'] + coord
                    * inserted == True
                * FinSi
            * FinMientras
            * dim_creatures = dim_creatures + {
            * 'typ' : type,
            * 'name' creatures[i][j] ,
            * 'symbol' creatures[i + 2][j],
            * 'row' : , coord[0],
            * 'col' : , coord[1],
            * /*date es funcioń del sistema*/
            * 'date' : Llamar date()
        * }
        * FinPara
    * FinPara
    * Retornar dim_creatures, general_coords
* FinFuncion
***
### Algoritmo dim_player
*Parámetros: alias, general_coords*
* Funcion player<- dim_player() :
    * inserted = False
    * Dimensionar coord[2]
    * Mientras inserted == False Haga:
        * coord[0] = Azar(0:general_coords['dim'])
        * coord[1] = Azar(0:general_coords['dim'])
        * Si coord in general_coords['coords'] == False
            * general_coords['coords'] = general_coords['coords'] + coord
            * inserted == True
        * FinSi
    * FinMientras
    * /* ASCII es una librería del lenguage que a partir de un número obtine caracteres ascii*/
    * symbol = Llamar ASCII(229)
    * dim_player = {
        * 'typ' : 'player',
        * 'alias' : alias ,
        * 'symbol' : symbol: ,
        * 'row' : , coord[0], 
        * 'col' : , coord[1], 
        * /*date es funcioń del sistema*/
        * 'date' : Llamar date(),
        * 'hearts' : 10
    * }
    * Retornar player, general_coords
* FinFuncion
***
### Algoritmo emul_alias_player
*Parámetros: Ninguno*
* Funcion alias<- emul_alias_player():
    * /*Se llenará con 20 alias*/
    * Dimensionar alias_list[20]
    * return alias_list[Azar[0:20]]
* FinFuncion
***
### Algoritmo: construct_game
*Parámetros: game_params*
* Funcion construct_walls():
    * BRICK=*#*
    * SPACE=' '
    * Longitud_game_params['walls'] = 32  /* Suponiendo, este valor varia pero hace referencia a la cantidad de coordenadas */
    * Para cada i<-0 Hasta game_params['dim'] con Paso 1 Hacer
        * row = ''
        * Para cada j<-0 Hasta game_params['dim'] con Paso 1 Hacer
            * /*Con i y j ya tenemos una coordenada. Ahora, revisar si está en la lista*/
            * creature=''
            * player=''
            * wall_exists=False
            * creature_exists=False
            * player_exists=False

            * /*Revisar si en la coordenada existe ladrillo*/
            * Para cada coord<-0 Hasta Longitud_game_params['walls'] con Paso 1 Hacer:
                * Si game_params['walls'][coord][0] == i and game_params['walls'][coord][1]==j Entonces
                    * wall_exists=True
                * FinSi
            * FinPara

            * /*Revisar si en la coordenada existe criatura hostiles (pos=0) ó pasivas (pos=1)*/
            * Para cada pos<-0 hasta 1 con paso 1 Hacer:
                * Para cada coord<-0 Hasta Longitud_game_params['creatures'][pos] con Paso 1 Hacer:
                    * Si game_params['creatures'][pos][i]['raw'] == i and game_params['creatures'][pos][i]['col']==j Entonces
                        * creature_exists=True
                        * creature = i game_params['creatures'][pos][i]['symbol']
                    * FinSi
                * FinPara
            * FinPara

            * /*Revisar si está el jugador en la coordenada*/
            * Si game_params['player']['row'] == i and game_params['player']['col'] == j Entonces:
                * player_exists = True
                * player = game_params['player']['symbol']
            * FinSi

            * Si wall_exists=True Entonces
                * row+=BRICK
            * SiNo
                * Si creature_exists=True Entonces:
                    * row+=creature
                * Sino
                    * Si player_exists = True Entonces:
                        * row+=player
                    * Sino
                        * row+=SPACE
                    * FinSi
                * FinSi
            * FinSi
        * FinPara
        * Escriba row
    * FinPara
* FinFuncion
***
### Algoritmo info_panel
*Parámetros: number_walls, game_params*
* Funcion info_panel() :
    * p_creatures = 0
    * Para cada i<-0 hasta Llamar longitud(game_params['creatures']) con Paso 1 Hacer:
        * Si game_params['creatures'][i]['typ'] == 'passive' Entonces:
            * p_creatures+=1
        * FinSi
    * FinPara
    * Escribir 'Total de muros:' number_walls
    * Escribir 'Vidas del jugador:' game_params['player]['hearts']
    * Escribir 'Número total de criaturas:' Llamar longitud(game_params['creatures])
    * Escribir 'Pasivas' p_creatures
    * Escribir 'Hostiles' Llamar longitud(game_params['creatures]) - p_creatures
* FinFuncion
***
### Algoritmo main
*Parámetros: ninguno*
* Funcion main()
    * /*===================================*/
    * /*FUNCIONES IMPORTADAS DE LA VERSION ANTERIOR DE WARCRAFT ASCII (Reto 4)*/
    * Leer dim /*Dimensiones del cuadrado. Un número*/
    * Leer pos /*Cantidad de posiciones*/
    * Dimension rows = Llamar get_rows(dim, pos)
    * Dimension columns = Llamar get_columns(dim, pos)
    * Dimension widths = Llamar get_widths(dim, pos)
    * Dimension longs = Llamar get_longs(dim, pos)
    * Dimension walls = Llamar get_walls(rows, columns, widths, longs, dim)
    * /*===================================*/
    * Dimensionar general_coords['dim'] = dim
    * general_coords['coords'] = []
    * Para i<-0 hasta longitud_walls con Paso 1 Hacer:
        * general_coords[i] = walls[i]
    * FinPara
    * Dimensionar creatures[Llamar creatures()]
    * creatures[0], general_coords['coords'] = Llamar dim_creatures(creatures[0], creatures[2], general_coords, 'hostile')
    * creatures[1], general_coords['coords'] = Llamar dim_creatures(creatures[1], creatures[3], general_coords, 'passive')
    * /*Se podría solicitar por pantalla el alias. En este caso, se emulará ello y se tomará de un listado un alias aleatorio*/
    * player, general_coords['coords'] = Llamar dim_player(Llamar emul_alias_player(), general_coords)
    * /*Empaquetar*/
    * Dimensionar game_params[4]
    * game_params['dim'] = dim
    * game_params['walls'] = walls
    * game_params['creatures] = creatures
    * game_params['player] = player
    * /*Renderización*/

    * /*===================================*/
    * /*FUNCIÓN MEJORADA DE LA VERSION ANTERIOR DE WARCRAFT ASCII (Reto 4)*/
    * Llamar construct_game(game_params)
    * /*===================================*/
    * /*===================================*/
    * /*Contruir panel de Información del Juego*/
    * Llamar info_panel(pos, game_params)
    * /*===================================*/
* FinFuncion
***
## Logros (L)
 