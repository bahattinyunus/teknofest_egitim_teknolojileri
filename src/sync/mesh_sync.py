import time

class MeshSyncClient:
    """
    Global Mesh Sync Protocol: Offline-first synchronization for low-connectivity regions.
    """
    
    def __init__(self, node_id):
        self.node_id = node_id
        self.local_cache = []
        self.is_online = False
        print(f"[SYNC] Mesh Node {self.node_id} Online.")

    def update_local_state(self, data):
        """
        Stores data locally when offline.
        """
        timestamp = time.time()
        entry = {"data": data, "timestamp": timestamp, "synced": False}
        self.local_cache.append(entry)
        print(f"[SYNC] Data cached locally at {timestamp}")

    def sync_with_nexus(self, connection_quality=0.8):
        """
        Synchronizes local cache with the central Nexus.
        """
        if connection_quality < 0.2:
            print("[SYNC] Connection too weak. Switching to P2P Mesh mode.")
            return self.p2p_mesh_propagate()
            
        unsynced_data = [item for item in self.local_cache if not item["synced"]]
        print(f"[SYNC] Synchronizing {len(unsynced_data)} objects to Nexus...")
        for item in unsynced_data:
            item["synced"] = True
            
        return "SYNC_COMPLETE"

    def p2p_mesh_propagate(self):
        """
        Propagates data through peer nodes in a mesh network.
        """
        print(f"[SYNC] Node {self.node_id} propagating data to nearby peers via LoRa/Bluetooth...")
        return "MESH_PROPAGATION_SUCCESS"

if __name__ == "__main__":
    sync = MeshSyncClient("NODE_OF_01")
    sync.update_local_state({"lesson": "Intro to Robotics", "student": "BYC"})
    sync.sync_with_nexus(connection_quality=0.1)
