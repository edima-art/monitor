import time
import monitor
import reporter
import utils  

def start():
    print("Démarrage du monitoring SecOps...") [cite: 3]
    try:
        while True: [cite: 70]
            # 1. Collecte
            data = monitor.get_metrics()
            
            # 2. Analyse (via utils)
            anomalies = utils.check_anomalies(data['cpu'], data['ram'], data['disk'])
            utils.print_status(data)
            
            if anomalies:
                print(f"ATTENTION : {', '.join(anomalies)}") [cite: 47]
            
            # 3. Rapport
            reporter.write_report(data)
            
            # 4. Pause [cite: 72]
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nArrêt de l'outil.")
