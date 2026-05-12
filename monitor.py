import subprocess
import shutil

def get_metrics():
    """Récupère les métriques système de base sous Windows."""
    metrics = {"cpu": 0.0, "ram": 0.0, "disk": 0.0}
    try:
        # CPU : Pourcentage de charge [cite: 39]
        cpu_out = subprocess.check_output("wmic cpu get loadpercentage", shell=True).decode().split()
        if len(cpu_out) >= 2: metrics["cpu"] = float(cpu_out[1])

        # RAM : Pourcentage d'utilisation [cite: 40]
        ram_free = int(subprocess.check_output("wmic os get freephysicalmemory", shell=True).decode().split()[1])
        ram_total = int(subprocess.check_output("wmic computersystem get totalphysicalmemory", shell=True).decode().split()[1]) / 1024
        metrics["ram"] = round(((ram_total - ram_free) / ram_total) * 100, 2)

        # Disque : Pourcentage utilisé sur C: [cite: 41]
        du = shutil.disk_usage("C:")
        metrics["disk"] = round((du.used / du.total) * 100, 2)
    except Exception as e:
        print(f"Erreur de lecture : {e}")
    
    return metrics
