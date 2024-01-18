class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine :
            dic[c] = dic[c]+1 if c in dic else 1
        
        for r in ransomNote :
            if r in dic :
                if dic[r] == 0 : return False
                dic[r] = dic[r] - 1
            else :
                return False
        return True