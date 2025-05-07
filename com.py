import os
import subprocess
from datetime import datetime, timedelta

# ======= CONFIGURACIONES =======
repositorio = '/home/angeljsh/Documentos/commits/'  # Cambia a tu ruta local si es diferente
archivo = 'contribuciones.txt'
fecha_inicio = '2025-03-26'  # Nueva fecha de inicio
fecha_fin = datetime.today().strftime('%Y-%m-%d')  # Fecha actual
remote_name = 'origin'       # Nombre del remoto (origin por defecto)
branch = 'master'            # Nombre de la rama (main por defecto)
# ===============================

# Convertir fechas a objetos datetime
start_date = datetime.strptime(fecha_inicio, '%Y-%m-%d')
end_date = datetime.strptime(fecha_fin, '%Y-%m-%d')

# Cambiar al directorio del repositorio
os.chdir(repositorio)

# Crear el archivo si no existe
if not os.path.exists(archivo):
    with open(archivo, 'w') as f:
        f.write('Contribuciones de GitHub:\n')

# Bucle para cada día desde la fecha de inicio hasta la fecha de fin, omitiendo fines de semana
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:  # 0-4 son lunes a viernes
        with open(archivo, 'a') as f:
            f.write(f'Contribución del {current_date.strftime("%Y-%m-%d")}\n')
        
        # Realizar el commit con fecha específica
        subprocess.run(['git', 'add', archivo])
        subprocess.run([
            'git', 'commit',
            '--date', current_date.strftime('%Y-%m-%dT12:00:00'),
            '-m', f'Contribución del {current_date.strftime("%Y-%m-%d")}'
        ])
    
    # Avanzar al siguiente día
    current_date += timedelta(days=1)

# Hacer push al repositorio remoto
subprocess.run(['git', 'push', remote_name, branch])

print(f"✅ ¡Contribuciones realizadas y subidas a GitHub desde el 17/02/2025 hasta {fecha_fin}, omitiendo fines de semana!")