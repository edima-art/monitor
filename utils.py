def print_header():
    print("-" * 30)
    print("OUTIL DE MONITORING SYSTEME")
    print("-" * 30)

def check_anomalies(cpu, ram, disk):
    """Identifie les anomalies de performance[cite: 6, 47]."""
    anomalies = []
    if cpu > 80: anomalies.append("Surcharge CPU")
    if ram > 90: anomalies.append("RAM saturée")
    if disk > 95: anomalies.append("Disque plein")
    return anomalies
