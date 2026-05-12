def check_anomalies(cpu, ram, disk):
    """Analyse les données pour identifier les surcharges[cite: 45, 47]."""
    anomalies = []
    if cpu > 80: anomalies.append("Surcharge CPU")
    if ram > 85: anomalies.append("RAM saturée")
    if disk > 90: anomalies.append("Disque plein")
    return anomalies

def print_status(data):
    """Affiche un résumé simple dans la console pour le suivi en temps réel."""
    print(f"--- Stats : CPU {data['cpu']}% | RAM {data['ram']}% | DISK {data['disk']}% ---")
