import subprocess
import shutil
import os

def get_cpu_usage():
    """Récupère l'utilisation CPU via WMIC (Windows)."""
    try:
        # Utilisation de r"" (raw string) pour éviter le SyntaxWarning sur les antislashs
        cmd = "wmic cpu get loadpercentage"
        output = subprocess.check_output(cmd, shell=True).decode().split()
        # La sortie de wmic est typiquement ['LoadPercentage', 'valeur']
        if len(output) >= 2:
            return float(output[1])
        return 0.0
    except Exception:
        return 0.0

def get_ram_usage():
    """Récupère l'utilisation RAM via WMIC (Windows)."""
    try:
        # Récupère la mémoire totale et libre en Ko
        cmd_total = "wmic computersystem get totalphysicalmemory"
        cmd_free = "wmic os get freephysicalmemory"
        
        total = int(subprocess.check_output(cmd_total, shell=True).decode().split()[1]) / 1024
        free = int(subprocess.check_output(cmd_free, shell=True).decode().split()[1])
        
        used_percent = ((total - free) / total) * 100
        return round(used_percent, 2)
    except Exception:
        return 0.0

def get_disk_usage():
    """Récupère l'espace disque de la racine (C:) via shutil."""
    try:
        # Sous Windows, on cible généralement le lecteur C:
        stat = shutil.disk_usage("C:")
        return round((stat.used / stat.total) * 100, 2)
    except Exception:
        # Repli sur le répertoire courant si C: n'est pas accessible
        stat = shutil.disk_usage(os.getcwd())
        return round((stat.used / stat.total) * 100, 2)
