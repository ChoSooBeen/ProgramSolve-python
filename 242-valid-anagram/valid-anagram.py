class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s :
            if c in map :
                map[c] += 1
            else :
                map[c] = 1
        
        for c in t :
            if c not in map :
                return False
            else :
                map[c] -= 1
                if map[c] == 0 :
                    map.pop(c)
        
        if map :
            return False

        return True