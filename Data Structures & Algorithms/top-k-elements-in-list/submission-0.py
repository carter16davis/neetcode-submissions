class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Hashmap to keep track of int counts
        freq = [[] for i in range(len(nums) + 1)] # index = freq; [] = sublist of ints at given freq

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if (len(result) == k):
                    return result

