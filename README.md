# TAREA4

*******************************************************
******** PUNTO 1 - INSTALAR Y CORRER CÓDIGO ***********
*******************************************************

# TOMANDO EN CUENTA QUE SE TIENE ANACONDA O CONDA INSTALADO
# SI SE TIENE INSTALADO CON EL PATH INCLUIDO EN EL PATH DE
 WINDOWS SE PUEDE DESDE CMD
# SI EL PATH NO FUE INCLUIDO, ENTONCES ABRIR UNA CONSOLA
 DESDE LA INSTALACION DE CONDA/ANACONDA

# PRIMERO CREAR VIRTUAL ENV

	conda create -n tarea4
	
	# Se genera directorio
	 ../tarea4

# ACTIVAR V ENV

	conda activate tarea4

# INSTALAR LIBERERÍAS 

	conda install pip
	pip install gensim
	pip install nltk
        pip install --upgrade numpy	
	
# INGRESAR AL DIRECTORIO DEL PROYECTO

	# cd C:\Users\chris\anaconda3\envs\tarea4
	cd ..\tarea4
	
# EN EL DIRECTORIO DE ESTE VENV CREADO
# COPIAR LOS ARCHIVOS DE LA CARPETA DEL GIT
# EN SUS RESPECTIVOS DIRECTORIOS. EL DUMP DE WIKIPEDIA COMPLETO PESA 19GB RAZÓN POR LA QUE NO LO SUBIMOS PERO LO PUEDE DESCARGAR DE
# https://dumps.wikimedia.org/enwiki/20220620/enwiki-20220620-pages-articles-multistream1.xml-p1p41242.bz2 DESCOMPRIMIR Y CAMBIAR
# LA EXTENSIÓN A XML POSTERIORMENTE CREAR UNA CARPETA LLAMADA articles-corpus

	..\tarea4\wiki_parser.py
	..\tarea4\wiki_topic_model.py
	..\tarea4\enwiki-20220620-pages-articles-multistream1.xml
	
# CORRER LOS ARCHIVOS EN SIGUIENTE ORDEN

	wiki_parser.py
	wiki_topic_model.py

# FINALIZAR

	conda deactivate

# RETOMAR

	conda activate tarea4
	cd ..\tarea4	
