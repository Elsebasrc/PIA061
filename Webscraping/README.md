## Practica 08 Webscraping

En esta practica se realizo un script en python que se fue realizando paso a paso la construccion hasta el script final, el objetivo es que realiza la recoleccion de informacion de una pagina web y posteriormente pasa los datos de nuestro interes a un archivo csv (excel).

El primer script que realizmos fue [scrape_quotes.py](./scrape_quote.py) el cual servirá para hace una petición a la URL del sitio  web(revisando  que sea  legal el uso de webscraping), analizamos el contenido HTML y generar listas citas y autores para mostrar en pantalla y guardar en un archivo .csv

Ahora  en los siguientes  scripts se fue construyendo un webscraping con Python con  el uso de la pagina FAKE PYTHON.

En el primer script [scrap1.py](./scrap1.py) simplemete nos conectamos  a la URL y extraemos  toda  la informacion.

En el segundo script [scrap2.py](./scrap2.py) implementamos la libreria de  BeautifulSoup con la que se analizara todo lo que encuentre en la etiqueta  'ResultsContainer' el contenido de tod lo  que  se encuentre se extrae.

En el tercer script [scrap3.py](./scrap3.py) buscamos informacion en base a metadatos,en este caso buscamos elementos de class"cart-content"

En el cuarto script [scrap4.py](./scrap4.py) como aun teniamos mucha informacion que no se deseaba, se buscaron titulos con informacion mas precisa.

En el quinto script [scrap5.py](./scrap5.py) una vez que se extrajo  informacion de  los  titulos  que nos importaban, especificamos que queremos que  nos muestre ese resultado en forma de un texto  y sin etiquetas HTML

En el sexto script [scrap6.py](./scrap6.py)como el resultado que se obtuvo anteriormente contiene algunos espacios en blanco que no nos sirven los limpiamos haciendo un ajuste al obtener el texto(.strip)

En el septimo script [scrap7.py](./scrap7.py) como se busca saber los jobs que estan relacionados a desarrollo de Python, entonces la forma de la búsqueda de  la informacion cambia, por lo que se indico  que se la cantidad de informacion  que tuviera  la palabra python.

En el octavo script [scrap8.py](./scrap8.py) una  ves encontrado  los jobs se hicieron iteraciones para desplegar la informacion que  se encontraba dentro de los jobs.Nos da un error ppor que la capa donde buscamos la informacion es en un tercer nivel.
Entonces en el noveno script [scrap9.py](./scrap9.py) hacemos unos ajustes ppara movernos de capa y poder hacer la busqueda correctamente

Ahora en el decimo script [scrap10.py](./scrap10.py) realizamos unos ajustes los cuales nos permiten mostrar la informacion de los python jobs que se encontraron donde buscaremos elementos con etiqueta a y mostraremos todos los elementos de links. En [scrap11.py](./scrap11.py) lo unico que se modifico es la forma de mostrar el link

Y por ultimo en el scrippt [scrap12.py](./scrap12.py) aunque nos muestra los dos elementos de href, en realidad solo nos interesa el elemento de “Apply Here”, el cual filtramos en este codigo.



