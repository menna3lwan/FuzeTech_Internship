from collections import defaultdict

#https://leetcode.com/u/Menna_Elwan/
class Solution:
    def findLHS(self, nums):
        if len(nums) <= 1:
            return 0

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        max_length = 0
        for num in count:
            if num + 1 in count:
                current_length = count[num] + count[num + 1]
                if current_length > max_length:
                    max_length = current_length

        return max_length