from collections import Counter
#https://leetcode.com/u/Menna_Elwan/
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if cnt[c] == 2:
                return c