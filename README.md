# ReMi - Python 3
Aplicación para recuperar la información de comprobantes electrónicos del SRI Ecuador.

## Oracle

### Instalación del conector de Oracle en Mac OSX
1. Descargar Oracle Instant Client. https://www.oracle.com/database/technologies/instant-client/downloads.html


        > instantclient-basic-macos.x64-11.2.0.4.0.zip 
        > instantclient-sqlplus-macos.x64-11.2.0.4.0.zip 
        > instantclient-sdk-macos.x64-11.2.0.4.0.zip


2. Descomprimir y copiar en un directorio todos los archivos, por ejemplo: /Users/allku/opt/instantclient_11_2

        libocci.dylib.11.1
        libociei.dylib
        libocijdbc11.dylib
        libsqlplus.dylib
        libsqlplusic.dylib
        ojdbc5.jar
        ojdbc6.jar
        sdk
        sqlplus
        uidrvci
        xstreams.jar
        
3. Crear enlaces simbólicos en el terminal:

        ln -s libclntsh.dylib.11.1 libclntsh.dylib
        ln -s libocci.dylib.11.1 libocci.dylib

4. Añadir al archivo .bash_profile: 

        vim .bash_profile 

        #Oracle Instant Client
        export ORACLE_HOME=/Users/allku/opt/instantclient_11_2
        export DYLD_LIBRARY_PATH=$ORACLE_HOME
        export LD_LIBRARY_PATH=$ORACLE_HOME
        export NLS_LANG=AMERICAN_AMERICA.UTF8
        export PATH=$PATH:$ORACLE_HOME


5. Ejecutar: 

        source .bash_profile 

6. Añadir el nombre del host al archivo /etc/hosts: 

       sudo vim /etc/hosts

       127.0.0.1       localhost       maclibro        maclibro.local
       
7. Probar la conexión: 

        sqlplus lucila/l@//192.168.1.18:1521/orcl

8. Descargar Python 3 de el sitio oficial https://www.python.org o https://brew.sh/ e instalar
9. Instalar pip, si no está instalado, por ejemplo:

       easy_install pip3
       
10. Instalar cx_Oracle: 

        pip3 install cx_oracle

### Instalación del conector de Oracle en Windows

1. Descargar Oracle Instant Client. https://www.oracle.com/database/technologies/instant-client/downloads.html
        
        > instantclient-basic-windows.x64-11.2.0.4.0.zip
        > instantclient-sqlplus-nt-11.2.0.4.0.zip
        > instantclient-sqlplus-windows.x64-11.2.0.4.0.zip
        
2. Descomprimir y copiar en un directorio todos los archivos, por ejemplo: C:\instantclient_11_2

        sdk
        vc8
        vc9
        adrci.exe
        adrci.sym
        genezi.exe
        genezi.sym
        glogin.sql
        oci.dll
        oci.sym
        ocijdbc11.dll
        ocijdbc11.sym
        ociw32.dll
        ociw32.sym
        ojdbc5.jar
        ojdbc6.jar
        orannzsbb11.dll
        orannzsbb11.sym
        oraocci11.dll
        oraocci11.sym
        oraociei11.dll
        oraociei11.sym
        orasql11.dll
        orasql11.sym
        Orasqlplusic11.dll
        sqlplus.exe
        sqlplus.sym
        uidrvci.exe
        uidrvci.sym
        xstreams.jar

3. Añadir C:\instantclient_11_2 al PATH: 

        1. Ejecutar el comando sysdm.cpl.
        2. Opciones avanzadas.
        3. Variables de entorno.
        4. Variables del sistema.
        5. Elegir de la lista la variable Path.
        6. Editar.
        7. En Valor de la variable, copiar al principio "C:\instantclient_11_2;" con punto y coma al final.

4. Probar la conexión: 

        sqlplus lucila/l@//192.168.1.18:1521/orcl

5. Si intenta con Python 2, descargar Microsoft Visual C++ Compiler for Python 2.7 del sitio de Microsoft https://www.microsoft.com/en-us/download/details.aspx?id=44266 e instalar. O puedes mirar aquí según la versión de python que uses https://wiki.python.org/moin/WindowsCompilers.
6. Descargar Python del sitio oficial https://www.python.org e instalar con todas las opciones activadas.
7. Instalar cx_Oracle: 

        pip3 install cx_oracle

### Instalación del conector de Oracle en Ubuntu.

1. Descargar Oracle Instant Client. https://www.oracle.com/database/technologies/instant-client/downloads.html

        > instantclient-basic-linux.x64-11.2.0.4.0.zip
        > instantclient-sdk-linux.x64-11.2.0.4.0.zip
        > instantclient-sqlplus-linux.x64-11.2.0.4.0.zip
        
2. Descomprimir y copiar en un directorio todos los archivos, por ejemplo: /app/instantclient_11_2

        adrci
        genezi
        glogin.sql
        libclntsh.so.11.1
        libnnz11.so
        libocci.so.11.1
        libociei.so
        libocijdbc11.so
        libsqlplusic.so
        libsqlplus.so
        ojdbc5.jar
        ojdbc6.jar
        sdk
        sqlplus
        uidrvci
        xstreams.jar

3. Crear enlaces simbólicos en el terminal:
        
        ln -s libclntsh.so.11.1 libclntsh.so
        ln -s libocci.so.11.1 libocci.so
        
4. Crear el archivo oracle.conf y añadir la ruta:

        sudo vim /etc/ld.so.conf.d/oracle.conf
        
        /app/instantclient_11_2
        
5. Ejecutar el comando e instalar las dependencias

        sudo ldconfig
        sudo apt install libaio-dev libaio1
        
6. Añadir al archivo .bashrc: 

        vim .bashrc

        #Oracle Instant Client
        export LD_LIBRARY_PATH=/app/instantclient_11_2:$LD_LIBRARY_PATH
        export PATH=/app/instantclient_11_2:$PATH

7. Ejecutar: 

        source .bashrc 
        
8. Probar la conexión: 

        sqlplus lucila/l@//192.168.1.18:1521/orcl
        
9. Instalar Python 3, si no está instalado:

        sudo apt install python3

10. Instalar pip, si no está instalado:

        sudo apt-get install python3-pip
       
11. Instalar cx_Oracle

        pip3 install cx_oracle        
        
## Instalar sqlAlchemy: 

        pip3 install sqlalchemy

