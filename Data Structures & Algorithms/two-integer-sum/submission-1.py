class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = target
        indice_table = {}
        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in indice_table:
                return [indice_table[complement], i]
            indice_table[nums[i]] = i
