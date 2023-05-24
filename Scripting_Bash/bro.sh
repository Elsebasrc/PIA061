#!/bin/bash
#Script bro.sh
#<09-03-2023><Brian Reyna Castillo>
echo "hola ${LOGNAME}"
echo "Hoy es $(date)"
echo "Usuarios actuales conectados, y sus procesos:"
w
ead -p "Escribe tu nombre: " nombre
echo "Hola, $nombre. Seamos amigos!"

