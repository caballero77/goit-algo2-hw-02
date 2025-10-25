"""
Завдання 2. Оптимізація черги 3D-принтера в університетській лабораторії

Розробіть програму для оптимізації черги завдань 3D-друку з урахуванням
пріоритетів та технічних обмежень принтера, використовуючи жадібний алгоритм.

Пріоритети завдань:
1 (найвищий) — Курсові/дипломні роботи
2 — Лабораторні роботи
3 (найнижчий) — Особисті проєкти
"""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    print_jobs = sorted([item for item in print_jobs if item['volume'] < constraints['max_volume']],
                        key=lambda x: (x['priority'], x['print_time']))

    print_order = []
    total_time = 0
    i = 0
    while i < len(print_jobs):
        current_batch = []
        current_volume = 0
        while (i < len(print_jobs) and
               len(current_batch) < constraints['max_items'] and
               current_volume + print_jobs[i]['volume'] <= constraints['max_volume']):
            current_batch.append(print_jobs[i])
            current_volume += print_jobs[i]['volume']
            i += 1
        total_time += max(job['print_time'] for job in current_batch)
        print_order.extend(job['id'] for job in current_batch)

    return {
        "print_order": print_order,
        "total_time": total_time
    }


def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")


if __name__ == "__main__":
    test_printing_optimization()
