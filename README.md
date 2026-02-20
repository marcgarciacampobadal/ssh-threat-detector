# SSH Threat Detector

## Descripción
Proyecto de detección de intentos fallidos de login SSH.  
Analiza logs tipo `auth.log`, detecta intentos fallidos, cuenta intentos por IP y usuario, y clasifica el riesgo.

## Funcionalidades
- Detecta intentos fallidos de login SSH (`Failed password`)  
- Extrae **IP** y **usuario atacado** usando expresiones regulares  
- Cuenta intentos por combinación IP + usuario  
- Clasifica riesgo según un umbral configurable  
- Exporta resultados a **CSV** para análisis externo  

## Uso
1. Asegúrate de tener un archivo de log tipo `sample_auth.log` en la carpeta del proyecto  
2. Ejecuta el script:

```bash
python detector.py