class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, i in enumerate(nums):
            remaining = target - i

            for second_index in range(index + 1, len(nums)):
                if nums[second_index] == remaining:
                    return [index, second_index]