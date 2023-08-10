from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Discord easy commands plus'
LONG_DESCRIPTION = 'Discord easy commands plus, a library to make discord bots in a easy way'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name= "discord_easy_commands_plus", 
        version=VERSION,
        author="JRaDev",
        author_email="<tuemail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["discord","flask","threading"], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
