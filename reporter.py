from datetime import datetime

def write_report(data):
    """Génère un rapport textuel exploitable[cite: 7, 29]."""
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Définition des statuts [cite: 47]
    c_status = "critique" if data["cpu"] > 80 else "normal"
    r_status = "critique" if data["ram"] > 85 else "normal"
    d_status = "critique" if data["disk"] > 90 else "normal"

    rapport = f"""===== RAPPORT SYSTEME =====
Date: {date_now}
CPU: {data['cpu']}% ({c_status})
RAM: {data['ram']}% ({r_status})
Disque: {data['disk']}% ({d_status})

Recommandations:
"""
    if c_status == "critique": rapport += "- Vérifier les processus actifs\n" [cite: 60]
    if d_status == "critique": rapport += "- Libérer de l'espace disque\n" [cite: 60]
    if "critique" not in [c_status, r_status, d_status]: rapport += "- RAS : Système stable\n"

    with open("rapport_systeme.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    print(f"[{date_now}] Rapport mis à jour.")
