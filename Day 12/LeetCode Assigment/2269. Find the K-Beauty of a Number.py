class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        #https://leetcode.com/u/Menna_Elwan/
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            n = int(substring)

            if n != 0 and num % n == 0:
                count += 1

        return count