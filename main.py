import time
import Monitor
import reporter
import utils

def run_monitoring():
    utils.print_header()
    
    try:
        while True:
            # 1. Collecte
            cpu = monitor.get_cpu_usage()
            ram = monitor.get_ram_usage()
            disk = monitor.get_disk_usage()
            
            # 2. Analyse
            anomalies = utils.check_anomalies(cpu, ram, disk)
            if anomalies:
                print(f"ALERTE : {', '.join(anomalies)}")
            
            # 3. Rapport
            reporter.generate_report(cpu, ram, disk)
            
            # 4. Attente (60 secondes) [cite: 72]
            print("En attente du prochain cycle...")
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\nArrêt du monitoring.")

if __name__ == "__main__":
    run_monitoring()
