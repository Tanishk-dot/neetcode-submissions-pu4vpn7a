class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                val = int(stack.pop()) + int(stack.pop())
                stack.append(val)

            elif c == "-":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b-a)

            elif c == "*":
                val = int(stack.pop()) * int(stack.pop())
                stack.append(val)

            elif c == "/":
                a , b = int(stack.pop()) , int(stack.pop())
                stack.append(b/a)

            else:
                stack.append(c)

        return int(stack[-1])

        