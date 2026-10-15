from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    student = ""
    y = 0
    for i in scores:
        if y < i[1]:
            y = i[1]
            student = i[0]
    return student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
