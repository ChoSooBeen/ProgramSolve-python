class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        word = s.split(' ')

        if len(pattern) != len(word) :
            return False

        for i in range(len(pattern)) :
            if pattern[i] in dic :
                if dic[pattern[i]] != word[i] :
                    return False
            else :
                if word[i] in dic.values() :
                    return False
                dic[pattern[i]] = word[i]
        return True