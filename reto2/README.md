# TÓPICOS TELEMÁTICA - ST0263

## Estudiantes: 
- Daniel Vélez Duque, dvelezd2@eafit.edu.co  
- Juan José Villada Calle, jjvilladac@eafit.edu.co

## Profesor: 
- Alvaro Enrique Ospina Sanjuan, aeospinas@eafit.edu.co

## 1. Descripción
Este proyecto consiste en el despliegue de un sistema de gestión de contenidos (CMS) WordPress en un clúster Kubernetes con alta disponibilidad. La configuración incluye un balanceador de cargas en la capa de aplicación para distribuir el tráfico entre varias réplicas de WordPress, un servidor de base de datos MySQL, y un servidor de archivos NFS para almacenamiento compartido. Aunque la implementación está enfocada en un entorno sin un dominio propio ni certificado SSL, la infraestructura sigue los principios de escalabilidad y robustez de Kubernetes

### 1.1. Aspectos Cumplidos (Requerimientos Funcionales y No Funcionales)
- **Wordpress en Kubernetes:** WordPress se despliega en Kubernetes con múltiples réplicas para asegurar alta disponibilidad y escalabilidad. Kubernetes gestiona las réplicas, reiniciándolas en caso de fallo y permitiendo el autoescalado según la carga.
- **Balanceo de Cargas:** Nginx distribuye el tráfico entre las réplicas de WordPress, asegurando un reparto equilibrado de solicitudes y evitando la sobrecarga de una única instancia.
- **Base de Datos MySQL:** MySQL se ejecuta en un contenedor Docker, funcionando como la base de datos de WordPress. Está configurada para integrarse directamente con WordPress y escalarse según la demanda.

### 1.2. Aspectos No Cumplidos
- **Dominio del Sitio:** Aunque no se logró conseguir un dominio propio para el despliegue de la aplicación, esta igual funciona sin ningún tipo de inconveniente en la propia dirección que el AWS proporciona.
- **NFS:** Se cumplió parcialmente, aunque en teoria el almacenamiento NFS se usa para compartir archivos entre todas las instancias de WordPress, asegurando un acceso común a los mismos datos y archivos de usuario.
  
## 2.  Información General de Diseño de Alto Nivel
El diseño del sistema se basa en la orquestación de contenedores utilizando Kubernetes en la nube. El LMS Moodle se despliega en múltiples réplicas para asegurar alta disponibilidad y escalabilidad, mientras que los servicios de base de datos y almacenamiento se externalizan para optimizar la gestión de datos.

### Arquitectura
- **Clúster Kubernetes:** Kubernetes gestiona las réplicas de la aplicación, garantizando alta disponibilidad y escalabilidad automática en función del tráfico y los recursos.
- **Balanceador de Cargas:** Nginx se encarga de repartir el tráfico entre las réplicas de la aplicación, optimizando el uso de recursos y evitando que una instancia se sobrecargue.
- **Base de Datos y NFS:** Tanto la base de datos y el sistema de archivos se gestionan fuera de la aplicación, lo que mejora la escalabilidad y permite administrar estos recursos de forma independiente.

## 3. Descripción del Ambiente de Desarrollo
El proyecto fue desarrollado utilizando Kubernetes para la orquestación de contenedores y tecnologías asociadas para la integración de base de datos, balanceo de cargas, y sistemas de archivos.

### 3.1 Tecnologías y Versiones:
- `Kubernetes`: 1.21.2 (EKS en AWS)
- `Nginx`: 1.21.3 (para balanceo de cargas)
- `Docker`: 20.10 (para la gestión de contenedores)
- `NFS`: 4.2
 
### 3.2 Detalles Técnicos
- Archivo de Configuración: En primer lugar, `kustomization.yaml` se utiliza para generar el `mysql-pass`. Posteriormente, el `mysql-deployment.yaml` configurará el servicio y el despliegue de MySQL. Finalmente, el `wordpress-deployment.yaml` configura el servicio y despliegue de WordPress, que se conecta al servicio de MySQL usando las credenciales definidas en el secreto.
  
- Estructura de Directorios:
  
  ```
  ├── kustomization.yaml
  ├── mysql-deployment.yaml
  ├── nfs-server.yaml
  └── wordpress-deployment.yaml
  ```

## 4. Guía de Uso
Para ejecutar este proyecto, se necesita acceso unicamente al clúster Kubernetes en la nube (AWS EKS), ya que las configuraciones específicas para la base de datos y el sistema de archivos se encuentran en los archivos YAML correspondientes.

### 4.1 Imágenes del Proyecto

![1](https://github.com/user-attachments/assets/50b20e95-efca-4b10-8a36-f0ac4a6b4df9)

![3](https://github.com/user-attachments/assets/4e524a99-a5cf-445b-904b-3d9be24a20cd)

![2](https://github.com/user-attachments/assets/b06db77d-9d59-49ba-9a25-51caffda54d9)

### 4.4 [Video](https://youtu.be/n34wxBE0g68)
 
## 5. Referencias:
- WordPress Foundation. (2024). WordPress documentation. Recuperado de https://wordpress.org/support/article/installation/
- Amazon Web Services, Inc. (2024). AWS documentation. Recuperado de https://docs.aws.amazon.com/
