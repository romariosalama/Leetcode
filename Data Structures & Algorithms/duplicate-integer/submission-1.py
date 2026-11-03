class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        lst = []
        for i in nums:
            if i in lst:
                return True
            lst.append(i)
            
        return False