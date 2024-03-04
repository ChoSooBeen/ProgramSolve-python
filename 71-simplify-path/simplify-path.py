class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.strip().split('/')
        stack = []

        for i in range(len(names)) :
            if names[i] == '' or names[i] == '.' :
                continue
            elif names[i] == '..' :
                if stack :
                    stack.pop()
            else :
                stack.append(names[i])
        
        result = ''
        for s in stack :
            result += '/' + s
        
        if result == '' :
            result = '/'
        
        return result