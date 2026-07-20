class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(set(nums)) == len(nums)):
            return False
        return True
        '''hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False'''
        