class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = target
        indice_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indice_table:
                return [indice_table[complement], i]
            else:
                indice_table[nums[i]] = i
