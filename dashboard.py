import time
import sys
import random

def print_header():
    header = """
    ============================================================
    [ NEXUS COMMAND CENTER - EDTECH-ARCHITECT ELITE v2.0 ]
    ============================================================
    System Status: ACTIVE | Encryption: ENABLED | Region: OF/TRABZON
    ------------------------------------------------------------
    """
    print(header)

def simulate_boot():
    steps = [
        "Initializing Synaptic Engine...",
        "Calibrating Holographic Layer Optics...",
        "Establishing Mesh Network Handshake...",
        "Scanning for Student Biometrics...",
        "Syncing with Nexus Cloud Service..."
    ]
    for step in steps:
        sys.stdout.write(f"[BOOT] {step:40}")
        sys.stdout.flush()
        time.sleep(0.4)
        print("[ DONE ]")
    print("\n[ SUCCESS ] SYSTEM FULLY OPERATIONAL.\n")

def simulate_metrics():
    print("--- LIVE PERFORMANCE METRIC STREAM ---")
    try:
        for _ in range(5):
            student_id = f"STU_{random.randint(100, 999)}"
            neural_idx = random.uniform(0.75, 0.98)
            sync_status = "SYNCED" if random.random() > 0.2 else "PENDING"
            
            print(f"> Node: {student_id} | Neuromorphic Index: {neural_idx:.4f} | Status: {sync_status}")
            time.sleep(0.6)
    except KeyboardInterrupt:
        pass
    print("---------------------------------------")

def main():
    print_header()
    simulate_boot()
    simulate_metrics()
    print("\n[INFO] Enter [CTRL+C] to exit Command Center.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[EXIT] Terminating Nexus Session...")
        time.sleep(0.5)
        print("[EXIT] Goodbye, Architect.")

if __name__ == "__main__":
    main()
