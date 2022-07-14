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
# EN SUS RESPECTIVOS DIRECTORIOS. EL DUMP DE WIKIPEDIA COMPLETO PESA 19GB RAZÓN POR LA QUE SOLO SUBIMOS UN EJEMPLO.

	..\tarea3\data
	..\tarea3\notebooks
	
# CORRER LOS NOTEBOOKS

	cd notebooks
	dir
	jupyter notebook topic_modelling_NPL2.ipynb

# FINALIZAR

	conda deactivate

# RETOMAR

	conda activate tarea4
	cd ..\tarea4
	jupyter notebook topic_modelling_NPL2.ipynb
