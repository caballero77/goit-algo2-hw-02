import pytest
from task_1 import find_min_max


class TestFindMinMax:
    def test_simple_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        min_val, max_val = find_min_max(arr)
        assert min_val == 1
        assert max_val == 9

    def test_single_element(self):
        arr = [42]
        min_val, max_val = find_min_max(arr)
        assert min_val == 42
        assert max_val == 42

    def test_two_elements(self):
        arr = [1, 2]
        min_val, max_val = find_min_max(arr)
        assert min_val == 1
        assert max_val == 2

    def test_negative_numbers(self):
        arr = [-5, -1, -10, -3, -7]
        min_val, max_val = find_min_max(arr)
        assert min_val == -10
        assert max_val == -1

    def test_mixed_numbers(self):
        arr = [-5, 10, -3, 7, 0, -15, 20]
        min_val, max_val = find_min_max(arr)
        assert min_val == -15
        assert max_val == 20

    def test_all_same_elements(self):
        arr = [5, 5, 5, 5, 5]
        min_val, max_val = find_min_max(arr)
        assert min_val == 5
        assert max_val == 5

    def test_empty_array(self):
        arr = []
        with pytest.raises(ValueError):
            find_min_max(arr)

    def test_large_array(self):
        arr = list(range(1000, 0, -1))
        min_val, max_val = find_min_max(arr)
        assert min_val == 1
        assert max_val == 1000

    def test_floats(self):
        arr = [1.5, 2.7, 0.3, 9.9, 3.14]
        min_val, max_val = find_min_max(arr)
        assert min_val == 0.3
        assert max_val == 9.9

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
