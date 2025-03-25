class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
       #https://leetcode.com/u/Menna_Elwan/
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_len = 0
        current_len = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                current_len = 1
                if current_len > max_len:
                    max_len = current_len

                for j in range(i + 1, len(nums)):
                    if nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                        current_len += 1
                        if current_len > max_len:
                            max_len = current_len
                    else:
                        break

        return max_len