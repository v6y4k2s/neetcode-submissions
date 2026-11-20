class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        j = 0

        for i in nums:
            if i == 1:
                c += 1
            elif i == 0:
                c = 0

            if c > j:
                j = c

        return j