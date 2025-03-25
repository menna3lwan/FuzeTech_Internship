class Solution:
    def fourSum(self, nums, target):
        results = []
        nums.sort()
        LT = target

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                tt = LT - nums[i] - nums[j]

                while left < right:
                    lr_sum = nums[left] + nums[right]

                    if lr_sum == tt:
                        result = [nums[i], nums[j], nums[left], nums[right]]
                        if result not in results:
                            results.append(result)
                        left += 1
                        right -= 1
                    elif lr_sum < tt:
                        left += 1
                    else:
                        right -= 1

        return results