from typing import List, Tuple


def find_min_max(arr: List[int | float]) -> Tuple[int | float, int | float]:
    if not arr:
        raise ValueError("Масив не повинен бути порожнім")

    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        return arr[1], arr[0]
    else:
        mid = len(arr) // 2
        left_min, left_max = find_min_max(arr[:mid])
        right_min, right_max = find_min_max(arr[mid:])
        return (left_min if left_min < right_min else right_min,
                left_max if left_max > right_max else right_max)


if __name__ == "__main__":
    test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_val, max_val = find_min_max(test_array)
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
