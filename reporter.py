from datetime import datetime

def generate_report(cpu, ram, disk, cpu_threshold=80, disk_threshold=90):
    """Crée un fichier rapport texte lisible[cite: 92]."""
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu_status = "critique" if cpu > cpu_threshold else "normal"
    ram_status = "critique" if ram > 85 else "normal"  # Seuil RAM arbitraire
    disk_status = "critique" if disk > disk_threshold else "normal"

    report_content = f"""===== RAPPORT SYSTEME =====
Date: {date_str}
CPU: {cpu}% ({cpu_status})
RAM: {ram}% ({ram_status})
Disque: {disk}% ({disk_status})

Recommandations:
"""
    if cpu > cpu_threshold:
        report_content += "- Vérifier les processus actifs\n"
    if disk > disk_threshold:
        report_content += "- Libérer de l'espace disque\n"
    if cpu_status == "normal" and disk_status == "normal":
        report_content += "- Aucune action requise.\n"

    with open("rapport_systeme.txt", "w") as f:
        f.write(report_content)
    
    print(f"Rapport généré le {date_str}")
