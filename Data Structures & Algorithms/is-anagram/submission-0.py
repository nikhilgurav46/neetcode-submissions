class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        Hashs = {}
        Hasht = {}

        for i in range(len(s)):
            Hashs[s[i]] = Hashs.get(s[i], 0) + 1
            Hasht[t[i]] = Hasht.get(t[i], 0) + 1
        
        for c in Hashs:
            if Hashs[c] != Hasht.get(c, 0):
                return False
        
        return True
        