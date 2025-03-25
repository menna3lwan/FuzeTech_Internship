class Solution(object):
    def countPairs(self, deliciousness):
        from collections import Counter
        c = Counter(deliciousness)
        powerOfT = {2**i for i in range(22)}
        poss = 0
        for x in c.keys():
            if x * 2 in powerOfT:
                poss += c[x] * (c[x] - 1) // 2
            for i in powerOfT:
                y = i - x
                if y != x and y > -1:
                    poss += c[x] * c[y]
            c[x] = 0
        return poss % (10**9 + 7)