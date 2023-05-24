#!/bin/bash
#Script nomber.sh
#<09-03-2023>-<Brian Reyna Castillo>
echo "hola ${LOGNAME}"
echo "Hoy es $(date)"
echo "Usuarios actuales conectados, y sus procesos:"
w

#Leer 3 numeros asignados a 3 variables 
read -p "Proporciona un numero para la variable 1: " n1
read -p "Proporciona un numero para la variable 2: " n2
read -p "Proporciona un numero para la variable 3: " n3
#
# Despliega los 3 numeros proporcionados por el usuario
echo "Numero 1 - $n1"
echo "Numero 2 - $n2"

echo "Numero 3 - $n3"
