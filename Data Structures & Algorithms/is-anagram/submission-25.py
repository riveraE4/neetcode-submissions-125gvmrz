class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        string = s
        string2 = t
        s = ''.join(sorted(string,key=str.lower))
        t = ''.join(sorted(string2,key=str.lower))

        return s == t



