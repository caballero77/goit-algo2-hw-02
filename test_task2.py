import pytest
from task_2 import optimize_printing, PrintJob, PrinterConstraints


class TestPrintingOptimization:
    def test_same_priority(self):
        jobs = [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
        ]
        constraints = {"max_volume": 300, "max_items": 2}

        result = optimize_printing(jobs, constraints)

        assert "print_order" in result
        assert "total_time" in result
        assert isinstance(result["print_order"], list)
        assert isinstance(result["total_time"], (int, float))

        assert len(result["print_order"]) == 3
        assert set(result["print_order"]) == {"M1", "M2", "M3"}

        assert result["total_time"] == 270

    def test_different_priorities(self):
        jobs = [
            {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},   # дипломна
            {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}   # особистий проєкт
        ]
        constraints = {"max_volume": 300, "max_items": 2}

        result = optimize_printing(jobs, constraints)

        assert len(result["print_order"]) == 3
        assert set(result["print_order"]) == {"M1", "M2", "M3"}

        assert result["print_order"][0] == "M2"

        assert result["total_time"] == 270

    def test_volume_exceeded(self):
        jobs = [
            {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
            {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
            {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
        ]
        constraints = {"max_volume": 300, "max_items": 2}

        result = optimize_printing(jobs, constraints)

        assert len(result["print_order"]) == 3
        assert set(result["print_order"]) == {"M1", "M2", "M3"}

        assert result["total_time"] == 450

    def test_single_job(self):
        jobs = [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120}
        ]
        constraints = {"max_volume": 300, "max_items": 2}

        result = optimize_printing(jobs, constraints)

        assert result["print_order"] == ["M1"]
        assert result["total_time"] == 120

    def test_max_items_constraint(self):
        jobs = [
            {"id": "M1", "volume": 50, "priority": 1, "print_time": 60},
            {"id": "M2", "volume": 50, "priority": 1, "print_time": 70},
            {"id": "M3", "volume": 50, "priority": 1, "print_time": 80},
            {"id": "M4", "volume": 50, "priority": 1, "print_time": 90}
        ]
        constraints = {"max_volume": 500, "max_items": 2}

        result = optimize_printing(jobs, constraints)

        assert len(result["print_order"]) == 4
        assert set(result["print_order"]) == {"M1", "M2", "M3", "M4"}

    def test_priority_ordering(self):
        jobs = [
            {"id": "M1", "volume": 100, "priority": 3, "print_time": 100},
            {"id": "M2", "volume": 100, "priority": 1, "print_time": 100},
            {"id": "M3", "volume": 100, "priority": 2, "print_time": 100},
        ]
        constraints = {"max_volume": 400, "max_items": 3}

        result = optimize_printing(jobs, constraints)

        m2_idx = result["print_order"].index("M2")
        m3_idx = result["print_order"].index("M3")
        m1_idx = result["print_order"].index("M1")

        assert m2_idx < m3_idx < m1_idx

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
