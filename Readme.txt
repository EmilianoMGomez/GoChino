Instalación de Python en Linux:
1-Abre una terminal en tu sistema Linux. Puedes hacerlo presionando Ctrl + Alt + T en la mayoría de las distribuciones.
2-Verifica si Python ya está instalado en tu sistema escribiendo el siguiente comando en la terminal y presionando Enter:

      python3 --version


Si obtienes una respuesta que muestra la versión de Python, significa que ya está instalado. En ese caso, puedes pasar a la sección "Instalación de Pygame".

3-Si Python no está instalado, ejecuta el siguiente comando en la terminal para instalarlo:

	sudo apt update
	sudo apt install python3


4-Durante la instalación, se te pedirá ingresar la contraseña de administrador. Proporciónala y espera a que se complete la instalación de Python.

Instalación de Pygame en Linux:
	1-Asegúrate de tener Python instalado siguiendo los pasos anteriores.
	2-En la misma terminal, ejecuta el siguiente comando para instalar las dependencias necesarias para Pygame:

		sudo apt install python3-pip python3-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev


	3-Luego, usa pip, el administrador de paquetes de Python, para instalar Pygame escribiendo el siguiente comando:

		pip3 install pygame


	4-Espera a que pip descargue e instale Pygame junto con sus dependencias.

		Ejecutar un juego de Pygame en Linux:
		1-Descarga el juego de Pygame que deseas ejecutar. Asegúrate de tener el archivo del juego con la extensión .py.
		2-Abre una terminal y navega hasta el directorio donde se encuentra el archivo del juego.
		3-Ejecuta el siguiente comando para iniciar el juego:

			python3 nombre_del_juego.py


		Reemplaza "nombre_del_juego.py" con el nombre real del archivo del juego que descargaste.

Con estos pasos, deberías poder instalar Python y ejecutar juegos hechos con la biblioteca Pygame en una máquina con sistema operativo Linux. 
Asegúrate de que la persona a la que le entregues este informe siga los pasos con cuidado y tenga en cuenta cualquier requisito adicional mencionado en la documentación del juego que desee ejecutar.