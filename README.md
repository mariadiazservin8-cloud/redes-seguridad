# Prácticas de Redes y Comunicaciones con Python

Este repositorio contiene una serie de scripts desarrollados en Python utilizando exclusivamente la **biblioteca estándar** para tareas de administración de redes, diagnóstico de conectividad, escaneo de puertos y resolución de DNS.

---

## Requisitos del Sistema

* **Python 3.x** instalado en el sistema operativo.
* Conectividad de red (para las pruebas de ping, resolución DNS y escaneo de puertos).
* Permisos de red adecuados para la ejecución de comandos `ping` y apertura de sockets TCP.

---

##  Índice de Programas

1. [Prueba de Conectividad Individual (`e03_ping.py`)](#1-prueba-de-conectividad-individual-e03_pingpy)
2. [Barrido de Ping en Subred (`e04_barrido.py`)](#2-barrido-de-ping-en-subred-e04_barridopy)
3. [Escaneo de Puertos TCP (`e05_escaneo.py`)](#3-escaneo-de-puertos-tcp-e05_escaneopy)
4. [Resolución de Nombres DNS y Reversa (`resolucion_dns.py`)](#4-resolución-de-nombres-dns-y-reversa-resolucion_dnspy)
5. [Medición de Latencia y Calidad TCP (`latencia_tcp.py`)](#5-medición-de-latencia-y-calidad-tcp-latencia_tcppy)
6. [Verificación HTTPS y Certificados SSL/TLS (`verificar_ssl.py`)](#6-verificación-https-y-certificados-ssltls-verificar_sslpy)
e07_latencia_tcp.py	Medición de rendimiento	Mide los tiempos de respuesta de conexiones TCP y calcula estadísticas de latencia.
e08_https_certificado.py	Seguridad HTTPS (TLS)	Verifica conexiones HTTPS y obtiene información sobre los certificados SSL/TLS.
Descripción detallada de los scripts
---

##  Descripción de los Programas

### 1. Prueba de Conectividad Individual (`e03_ping.py`)
* **Descripción:** Envía un único paquete `ping` adaptable al sistema operativo (utiliza la opción `-n` en Windows y `-c` en Linux/macOS). Devuelve un valor booleano (`True` o `False`) indicando si el host respondió correctamente dentro de un tiempo límite.

### 2. Barrido de Ping en Subred (`e04_barrido.py`)
* **Descripción:** Realiza un escaneo masivo y concurrente de hosts activos en una subred completa utilizando hilos (`ThreadPoolExecutor`). Valida el tamaño de la red, optimiza el tiempo de respuesta frente a un escaneo secuencial y mide el tiempo total de ejecución.

### 3. Escaneo de Puertos TCP (`e05_escaneo.py`)
* **Descripción:** Comprueba el estado de una lista predefinida de puertos conocidos y servicios asociados (como HTTP, SSH, FTP, RDP, MySQL, SMB, etc.) sobre una dirección IP o dominio, utilizando sockets TCP con un tiempo de espera controlado para evitar bloqueos.

### 4. Resolución de Nombres DNS y Reversa (`resolucion_dns.py`)
* **Descripción:** Realiza consultas de resolución DNS directa (`gethostbyname_ex`) para obtener nombres canónicos, alias y múltiples direcciones IP, midiendo la latencia de la consulta en milisegundos. Además, incluye la resolución inversa (registro PTR) a partir de la IP obtenida.

### 5. Medición de Latencia y Calidad TCP (`latencia_tcp.py`)
* **Descripción:** Evalúa la calidad de la conexión hacia un host y puerto específico mediante múltiples intentos consecutivos. Calcula estadísticas de red esenciales: tiempos mínimo, máximo, promedio y el porcentaje de pérdida de paquetes.

### 6. Verificación HTTPS y Certificados SSL/TLS (`verificar_ssl.py`)
* **Descripción:** Realiza una petición web mediante HTTPS midiendo el tiempo de respuesta y capturando el código de estado HTTP. Adicionalmente, inspecciona el canal seguro cifrado para extraer la fecha de expiración del certificado SSL/TLS y calcular los días restantes de validez.
* 7. Medición de latencia TCP (e07_latencia_tcp.py)

Realiza mediciones del tiempo de respuesta de conexiones TCP y utiliza estadísticas para calcular valores como promedio y mediana.

8. Verificación de certificados HTTPS (e08_https_certificado.py)

Permite verificar conexiones HTTPS, consultar información de certificados SSL/TLS y comprobar su período de validez
