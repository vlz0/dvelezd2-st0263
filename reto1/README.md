# TÓPICOS TELEMÁTICA - ST0263

## Estudiantes: 
- Daniel Vélez Duque, dvelezd2@eafit.edu.co  
- Juan José Villada Calle, jjvilladac@eafit.edu.co

## Profesor: 
- Alvaro Enrique Ospina Sanjuan, aeospinas@eafit.edu.co

## 1. Descripción
Este proyecto se enfoca en la implementación de una red peer-to-peer (P2P) utilizando la arquitectura Chord/DHT para la distribución de archivos y la comunicación entre nodos. La implementación hace uso de tecnologías de comunicación como API REST y gRPC (RPC), integrando múltiples paradigmas de comunicación para crear un sistema distribuido eficiente y escalable. Cada nodo en la red actúa tanto como cliente (PCliente) como servidor (PServidor), permitiendo la distribución, búsqueda y transferencia de archivos en la red P2P.

### 1.1. Aspectos Cumplidos (Requerimientos Funcionales y No Funcionales)
- **API REST:** Se ha implementado una API REST para la interacción básica entre nodos, permitiendo la carga, descarga y listado de archivos, así como la administración de la red, como el proceso de unión de nuevos nodos.
- **Chord/DHT:** La arquitectura de la red está basada en el protocolo Chord, que permite una organización eficiente de los nodos y el direccionamiento de archivos dentro de la red.
- **Manejo de Archivos:** Cada nodo gestiona su propio conjunto de archivos, y la red distribuye estos archivos de acuerdo con el protocolo DHT, asegurando que los archivos sean accesibles de manera eficiente desde cualquier nodo.
- **Simulación de Comunicación RPC (gRPC):** Se ha incorporado una interfaz gRPC para algunas funcionalidades, aunque su implementación es parcial. Esta interfaz permite la comunicación remota entre nodos mediante procedimientos definidos previamente.

### 1.2. Aspectos No Cumplidos
- **gRPC:** Aunque se logró implementar parte de la funcionalidad gRPC, su integración completa con la red no se alcanzó.
- **Despliegue en AWS:** No se logró realizar el despliegue en AWS, por lo que el sistema solo se probó en un entorno local.

## 2.  Información General de Diseño de Alto Nivel
El diseño de la red se basa en la arquitectura Chord/DHT, donde cada nodo en la red tiene un identificador único generado a partir de un hash. Los nodos están organizados en un anillo lógico, y cada nodo conoce a su sucesor y predecesor, lo que permite un eficiente enrutamiento de mensajes y distribución de archivos. La implementación sigue las mejores prácticas de diseño distribuido, asegurando que los nodos sean autónomos y que la red pueda escalar horizontalmente al agregar más nodos.

### Arquitectura
- **Nodo P2P:** Cada nodo puede ser considerado tanto un cliente como un servidor. Como servidor, el nodo responde a las solicitudes de otros nodos, y como cliente, el nodo puede buscar y recuperar archivos de la red.
- **Distribución de Archivos:** Los archivos se distribuyen en la red de acuerdo con la función de hash utilizada por Chord, lo que garantiza una distribución equilibrada y un acceso eficiente.
- **Comunicación REST y gRPC:** La API REST maneja la mayor parte de las operaciones cotidianas, mientras que gRPC se usa para operaciones específicas que requieren una mayor eficiencia en la comunicación entre nodos.

## 3. Descripción del Ambiente de Desarrollo
El desarrollo de este proyecto se realizó utilizando el lenguaje de programación Python. Se usaron diversas bibliotecas y paquetes, principalmente Flask para la API REST, gRPC para la comunicación RPC, y hashlib para la implementación de la función de hash de Chord.

### 3.1 Tecnologías y Versiones:
- `Python`: 3.8
- `Flask`: 2.1.1 (para API REST)
- `gRPC`: 1.40.0 (para comunicación RPC)
- `hashlib`: Parte de la biblioteca estándar de Python (para generación de identificadores de nodos)
- `requests`: 2.26.0 (para manejo de solicitudes HTTP en la API REST)
 
### 3.2 Detalles Técnicos
- Archivo de Configuración: `config.json` se utiliza para especificar la IP, puerto, y otros parámetros de configuración de cada nodo.
- Estructura de Directorios:
  
  ```
  ├── chord.proto
  ├── chord.py
  ├── config.json
  ├── grpc_client.py
  ├── grpc_server.py
  ├── PClient.py
  ├── PServer.py
  └── start.py
  ```

## 4. Guía de Uso
Para ejecutar este proyecto en un ambiente de producción, se requeriría un servidor que soporte Python y tenga instaladas las dependencias listadas anteriormente. Sin embargo, el proyecto será llevado a cabo de manera local por ahora. La configuración de los nodos se haría mediante el archivo `config.json`, especificando la IP, puerto, y otros parámetros.

### 4.1 Configuración de Parámetros
- **Dirección IP:** 127.0.0.1
- **Puertos:** 5000 (HTTP), 50052 (gRPC)
- **URL del Peer Inicial:** El `SEED_PEER_URL` en `config.json` define el nodo inicial al cual se conectará un nuevo nodo al unirse a la red
- **Archivos**

### 4.2 Ejecución del Proyecto
El proyecto no requiere un proceso de compilación debido a que está escrito en Python. Para ejecutarlo, simplemente se debe correr el servidor utilizando el comando `python PServer.py` y el cliente con `python PClient.py`.

- Iniciar el Servidor
  ```
  python PServer.py
  ```
- Iniciar el Cliente, para unirse a la red y listar archivos
  ```
  python PClient.py
  ```

### 4.3. Imágenes del Proyecto
![2](https://github.com/user-attachments/assets/5a4a457a-a5a2-493e-98f3-5d78a65e38ba) 

![1](https://github.com/user-attachments/assets/dc4de873-8659-49f2-b196-e0c9a448e86d)

### 4.4 [Video](https://youtu.be/i3ffRw9Q3vE)
 
## 5. Referencias:
- Stoica, I., et al. (2001). Chord: A scalable peer-to-peer lookup protocol for internet applications. ACM SIGCOMM Computer Communication Review, 31(4), 149-160.
- [Flask Documentation](https://flask.palletsprojects.com)
- [gRPC Documentation](https://grpc.io/docs/)
