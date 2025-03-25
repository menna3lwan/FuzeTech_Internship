class Solution(object):
    #META INTERVIEW PROBLEM
    # https://leetcode.com/u/Menna_Elwan/
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            seen.add(substring)

        return list(repeated)