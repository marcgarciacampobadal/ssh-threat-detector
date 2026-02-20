import re

# Archivo de log
log_file = "sample_auth.log"

# Diccionario para contar intentos por (IP, usuario)
failed_attempts = {}

# Umbral para clasificar riesgo
threshold = 2  # más de 2 intentos = riesgo ALTO

# Leer archivo
with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line:
            # Extraer IP
            ip_match = re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
            ip = ip_match.group() if ip_match else "unknown"

            # Extraer usuario atacado
            user_match = re.search(r"for (invalid user )?(\S+) from", line)
            user = user_match.group(2) if user_match else "unknown"

            # Contar intentos por (IP, usuario)
            key = (ip, user)
            if key in failed_attempts:
                failed_attempts[key] += 1
            else:
                failed_attempts[key] = 1

# Mostrar resultados
for (ip, user), count in failed_attempts.items():
    risk = "ALTO" if count > threshold else "MEDIO"
    print(f"IP: {ip} | Usuario: {user} | Intentos fallidos: {count} | Riesgo: {risk}")