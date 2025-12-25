from src.core.synaptic_engine import SynapticEngine
from src.interface.holographic_layer import HolographicLayer
from src.sync.mesh_sync import MeshSyncClient

def test_system_integration():
    print("--- 🎓 EDTECH-ARCHITECT SYSTEM INTEGRATION TEST ---")
    
    # 1. Initialize Components
    ai_engine = SynapticEngine()
    xr_layer = HolographicLayer()
    sync_node = MeshSyncClient("NEXUS_MASTER")
    
    # 2. Simulate AI Performance Analysis
    metrics = ai_engine.analyze_performance("STUDENT_01", [85, 92, 88])
    curriculum = ai_engine.adjust_curriculum("STUDENT_01", metrics)
    
    # 3. Cache Data Locally
    sync_node.update_local_state(curriculum)
    
    # 4. Initialize XR Interface
    xr_layer.initialize_xr_session()
    xr_layer.render_3d_module(curriculum["next_modules"][0])
    
    # 5. Final Sync
    sync_status = sync_node.sync_with_nexus(connection_quality=0.9)
    print(f"--- TEST FINISHED: {sync_status} ---")

if __name__ == "__main__":
    test_system_integration()
