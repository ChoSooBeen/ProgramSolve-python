class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        answer = 0
        idx = 0
        
        while idx < len(s) :
            if idx == len(s) - 1 :
                answer += dic[s[idx]]
                break
            if s[idx] == "I" :
                if s[idx+1] == "V" or s[idx+1] == "X" :
                    answer += (dic[s[idx+1]] - dic[s[idx]])
                    idx += 2
                else :
                    answer += dic[s[idx]]
                    idx += 1
            elif s[idx] == "X" :
                if s[idx+1] == "L" or s[idx+1] == "C" :
                    answer += (dic[s[idx+1]] - dic[s[idx]])
                    idx += 2
                else :
                    answer += dic[s[idx]]
                    idx += 1
            elif s[idx] == "C" :
                if s[idx+1] == "D" or s[idx+1] == "M" :
                    answer += (dic[s[idx+1]] - dic[s[idx]])
                    idx += 2
                else :
                    answer += dic[s[idx]]
                    idx += 1
            else :
                answer += dic[s[idx]]
                idx += 1

        return answer