class Solution:
    def findSubarrays(self, nums):
        seen_sums = set()
        for i in range(1, len(nums)):
            current_sum = nums[i] + nums[i - 1]
            if current_sum in seen_sums:
                return True
            seen_sums.add(current_sum)
        return False