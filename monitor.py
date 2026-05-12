import subprocess
import shutil
import os

def get_cpu_usage():
    """Récupère l'utilisation CPU via la commande top (Linux)."""
    try:
        # Commande pour extraire le pourcentage d'utilisation CPU
        cmd = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\([0-9.]*\)%* id.*/\\1/' | awk '{print 100 - $1}'"
        cpu = subprocess.check_output(cmd, shell=True).decode().strip()
        return float(cpu)
    except Exception:
        return 0.0

def get_ram_usage():
    """Récupère l'utilisation RAM via /proc/meminfo[cite: 43]."""
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
        total = int(lines[0].split()[1])
        available = int(lines[2].split()[1])
        used_percent = ((total - available) / total) * 100
        return round(used_percent, 2)
    except Exception:
        return 0.0

def get_disk_usage():
    """Récupère l'espace disque de la racine via shutil[cite: 87]."""
    stat = shutil.disk_usage("/")
    return round((stat.used / stat.total) * 100, 2)
