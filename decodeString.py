import collections

class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        stack = collections.deque([])

        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curDecodedString = []
                while len(stack) > 0:
                    curChar = stack.pop()
                    if curChar == '[':
                        break
                    curDecodedString.append(curChar)
                k = ''
                while len(stack) > 0:
                    curChar = stack.pop()
                    if 0 <= ord(curChar) - ord('0') <= 9:
                        k = curChar + k
                    else:
                        stack.append(curChar)
                        break
                k = int(k)
                for j in range(k):
                    for ch in curDecodedString[::-1]:
                        stack.append(ch)
            i += 1

        return ''.join(stack)

if __name__ == '__main__':
    # "3[a]2[bc]"
    # "3[a2[c]]"
    # "2[abc]3[cd]ef"

    solution = Solution()
    encodedString = "2[abc]3[cd]ef"
    print(solution.decodeString(encodedString))
