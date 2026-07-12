class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"{":"}", "(":")","[":"]"}
        stack = []

        for ch in s:
            if ch in matches:
                stack.append(ch)
            else:
                if len(stack) > 0:
                    open = stack.pop()
                    if matches[open] != ch:
                        return False
                else:
                    return False

        return len(stack) == 0