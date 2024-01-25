class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        if not t :
            return False
            
        idx = 0
        for c in t :
            if c == s[idx] :
                idx += 1
            if idx == len(s) :
                break
        if idx == len(s) :
            return True
        return False