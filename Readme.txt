COMO DESCARGAR EL PROYECTO

1. Abrir el navegador web
2. Buscar en el navegador el enlace de github (https://github.com/EmilianoMGomez/GoChino)
3. Una vez que entre en la pagina se debe buscar el boton que dice <>code y luego hacer click en Download Zip para que compience la descarga.
														
4. Una vez descargado hay que ir a la carpeta de descarga (o donde se le descargo el archivo) y descomprimirlo.

COMO INICIO EL JUEGO:

El proyecto esta diseñado para funcionar en un entorno Linux, si no cuenta con Linux debera instalar una maquina virtual en su sistema operativo de la siguiente manera:

Para instalar Linux Ubuntu en una máquina virtual VirtualBox, sigue los siguientes pasos:
    1. Descarga e instala VirtualBox:
        ◦ Visita el sitio web oficial de VirtualBox en https://www.virtualbox.org/
        ◦ Descarga la versión adecuada de VirtualBox para tu sistema operativo anfitrión (Windows, macOS, Linux, etc.).
        ◦ Ejecuta el instalador y sigue las instrucciones para instalar VirtualBox en tu sistema.
    2. Descarga la imagen ISO de Ubuntu:
        ◦ Ve al sitio web oficial de Ubuntu en https://ubuntu.com/
        ◦ Descarga la versión de Ubuntu que deseas instalar. Selecciona la versión LTS (Long Term Support) recomendada para una mayor estabilidad.
        ◦ Asegúrate de elegir la arquitectura correcta (32 o 64 bits) según tu sistema anfitrión.
    3. Crea una nueva máquina virtual en VirtualBox:
        ◦ Abre VirtualBox y haz clic en el botón "Nuevo" para crear una nueva máquina virtual.
        ◦ Asigna un nombre a la máquina virtual y selecciona el tipo de sistema operativo como "Linux".
        ◦ Elige la versión correcta de Ubuntu en la lista desplegable.
        ◦ Asigna la cantidad de memoria RAM que deseas asignar a la máquina virtual. Se recomienda al menos 2 GB para un funcionamiento óptimo.
        ◦ En la siguiente pantalla, selecciona "Crear un disco duro virtual ahora" y elige el tipo de archivo de disco duro virtual (por defecto, "VDI").
        ◦ Selecciona "Dinámicamente asignado" como el tamaño del disco duro virtual y asigna el tamaño deseado para la máquina virtual.
    4. Instala Ubuntu en la máquina virtual:
        ◦ Selecciona la máquina virtual que creaste y haz clic en el botón "Iniciar" para comenzar la instalación.
        ◦ Cuando se te solicite, selecciona la imagen ISO de Ubuntu que descargaste en el paso anterior.
        ◦ Sigue las instrucciones en pantalla para completar el proceso de instalación de Ubuntu. Puedes elegir la configuración y opciones según tus preferencias.
        ◦ Una vez finalizada la instalación, reinicia la máquina virtual.
    5. Configura Ubuntu en la máquina virtual:
        ◦ Después de reiniciar, Ubuntu se ejecutará en la máquina virtual. Sigue las instrucciones iniciales para configurar el idioma, la ubicación y otros detalles.
        ◦ Actualiza Ubuntu a la última versión ejecutando el administrador de actualizaciones o usando el siguiente comando en una terminal:
sudo apt update && sudo apt upgrade
Ahora tienes Ubuntu instalado en una máquina virtual VirtualBox. Puedes usarlo para probar y ejecutar aplicaciones y configuraciones en un entorno 

Una vez que tenemos instalada la maquina virtual con Linux debemos instalar Python de la siguiente manera:
Instalación de Python en Linux:
           1. Abre una terminal en tu sistema Linux. Puedes hacerlo presionando Ctrl + Alt + T en la mayoría de las distribuciones.
           2. Verifica si Python ya está instalado en tu sistema escribiendo el siguiente comando en la terminal y presionando Enter:
python3 --version
    • Si obtienes una respuesta que muestra la versión de Python, significa que ya está instalado. En ese caso, puedes pasar a la sección "Instalación de Pygame".
           3.Si Python no está instalado, ejecuta el siguiente comando en la terminal para instalarlo:
sudo apt update
sudo apt install python3

       4.Durante la instalación, se te pedirá ingresar la contraseña de administrador. Proporciónala y espera a que se complete la instalación de Python.

Ahora debemos instalar la librería Pygame para poder visualizar el juego.
    • Instalación de Pygame en Linux:
           1.En la misma terminal, ejecuta el siguiente comando para instalar las dependencias necesarias para Pygame:
    • sudo apt install python3-pip python3-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
           2.Luego, usa pip, el administrador de paquetes de Python, para instalar Pygame escribiendo el siguiente comando:
            ▪ pip3 install pygame
              
           3.Espera a que pip descargue e instale Pygame junto con sus dependencias.
           
Luego tendremos que ejecutar el juego en Linux:
           1. Abre una terminal y navega hasta el directorio donde se encuentra el archivo del juego.
           2.Ejecuta el siguiente comando para iniciar el juego:
            ▪ python3 nombre_del_juego.py
      
      Reemplaza "nombre_del_juego.py" con el nombre real del archivo del juego que descargaste. Con estos pasos, deberías poder instalar Python y ejecutar juegos hechos con la biblioteca Pygame en una máquina con sistema operativo Linux. Asegúrate de que la persona a la que le entregues este informe siga los pasos con cuidado y tenga en cuenta cualquier requisito adicional mencionado en la documentación del juego que desee ejecutar.

