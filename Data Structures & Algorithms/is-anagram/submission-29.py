class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1 #this increase the count within s
        for c in t:
            count[c] = count.get(c,0) - 1 #this decreases when a char is seen in t and in s
            if count[c] < 0:
                return False
        return True



