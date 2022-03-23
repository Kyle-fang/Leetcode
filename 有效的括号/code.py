def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for S in s:
            if S in pairs:
                if not stack or stack[-1] != pairs[S]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(S)
        return not stack
