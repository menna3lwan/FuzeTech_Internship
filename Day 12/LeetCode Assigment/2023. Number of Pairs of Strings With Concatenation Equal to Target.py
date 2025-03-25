class Solution:
    def numOfPairs(self, nums, target):
        l = {}
        t = len(target)
        v = 0

        for index, num in enumerate(nums):
            nl = len(num)

            if nl not in l:
                l[nl] = []

            isp = num == target[:nl]
            is_suffix = num == target[-nl:]

            if isp and (t - nl) in l:
                v += l[t - nl].count(True)

            if is_suffix and (t - nl) in l:
                v += l[t - nl].count(False)

            if isp:
                l[nl].append(False)
            if is_suffix:
                l[nl].append(True)

        return v