import random

class SynapticEngine:
    """
    Synaptic AI Engine: Core logic for adaptive learning and student performance analysis.
    Designed for TEKNOFEST EdTech-Architect Division.
    """
    
    def __init__(self, model_version="2025.alpha"):
        self.version = model_version
        self.knowledge_base = {}
        print(f"[NEXUS] Synaptic Engine {self.version} Initialized.")

    def analyze_performance(self, student_id, scores):
        """
        Analyzes student performance to detect learning difficulties.
        :param student_id: Unique identifier for the student.
        :param scores: List of recent test scores or interaction metrics.
        :return: Dict containing performance metrics and difficulty flags.
        """
        avg_score = sum(scores) / len(scores) if scores else 0
        difficulty_flag = avg_score < 60
        
        metrics = {
            "avg_score": avg_score,
            "consistency": self._calculate_consistency(scores),
            "difficulty_detected": difficulty_flag,
            "neuromorphic_index": random.uniform(0.7, 0.95)
        }
        
        print(f"[NEXUS] Analysis complete for Student {student_id}. Difficulty: {difficulty_flag}")
        return metrics

    def adjust_curriculum(self, student_id, metrics):
        """
        Dynamically adjusts the curriculum based on performance metrics.
        """
        if metrics["difficulty_detected"]:
            strategy = "Reinforcement Path - Fundamental Focus"
            pace = "0.75x"
        else:
            strategy = "Accelerated Path - Advanced Modules"
            pace = "1.25x"
            
        curriculum_update = {
            "strategy": strategy,
            "pace": pace,
            "next_modules": ["Module_A1", "Module_B2"] if metrics["difficulty_detected"] else ["Module_X9", "Module_Y4"]
        }
        
        print(f"[NEXUS] Curriculum adjusted for Student {student_id} to: {strategy}")
        return curriculum_update

    def _calculate_consistency(self, scores):
        if not scores: return 1.0
        variance = sum((x - (sum(scores)/len(scores)))**2 for x in scores) / len(scores)
        return 1.0 / (1.0 + variance)

if __name__ == "__main__":
    engine = SynapticEngine()
    test_metrics = engine.analyze_performance("DEV_01", [45, 52, 48, 60])
    engine.adjust_curriculum("DEV_01", test_metrics)
