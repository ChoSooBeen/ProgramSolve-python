class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        end = 0
        result = 0
        while end < len(s) :
            if s[end] not in dic :
                dic[s[end]] = 1
                end += 1
                result = max(result, end-start)
            else :
                del dic[s[start]]
                start += 1

        return result