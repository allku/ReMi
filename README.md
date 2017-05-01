# Remi
Aplicación para recuperar la información de comprobantes electrónicos del SRI Ecuador

* Instalación en Mac OSX para Oracle

    - Descargar Oracle Instant Client http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html
        + instantclient-basic-macos.x64-11.2.0.4.0.zip 
        + instantclient-sqlplus-macos.x64-11.2.0.4.0.zip 
        + instantclient-sdk-macos.x64-11.2.0.4.0.zip
    - Copiar en un directorio todos los archivos, por ejemplo: /Users/jorgequiguango/opt/instantclient_11_2
        
        >libocci.dylib.11.1
        >libociei.dylib
        >libocijdbc11.dylib
        >libsqlplus.dylib
        >libsqlplusic.dylib
        >ojdbc5.jar
        >ojdbc6.jar
        >sdk
        >sqlplus
        >uidrvci
        >xstreams.jar
        
    - Crear enlaces simbólicos en el terminal
        + ln -s libclntsh.dylib.11.1 libclntsh.dylib
        + ln -s libocci.dylib.11.1 libocci.dylib
    - Añadir al archivo .bash_profile: nano .bash_profile 
        #Oracle Instant Client
        export ORACLE_HOME=/Users/jorgequiguango/opt/instantclient_11_2
        export DYLD_LIBRARY_PATH=$ORACLE_HOME
        export LD_LIBRARY_PATH=$ORACLE_HOME
        export NLS_LANG=AMERICAN_AMERICA.UTF8
        export PATH=$PATH:$ORACLE_HOME
    - Ejecutar: source .bash_profile 
    - Añadir el nombre del host al archivo /etc/hosts: sudo nano /etc/hosts
        127.0.0.1       localhost       maclibro        maclibro.local
    - Probar la conexión: sqlplus lucila/l@//192.168.1.18:1521/orcl
    - En Mac OSX ya está pre-instalador Python 2.7, caso contrario descargar del sitio oficial.
    - Instalar pip: sudo easy_install pip
    - Instalar sqlAlchemy: sudo pip install sqlalchemy
    - Instalar cx_Oracle: sudo pip install cx_oracle
    
