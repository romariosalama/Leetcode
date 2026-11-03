import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    sorted_heap = []
    heapq.heapify(nums)
    for i in range(len(nums)):
        popped = heapq.heappop(nums)
        heapq.heappush(sorted_heap, popped)
    sorted_heap.reverse()
    return sorted_heap





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
