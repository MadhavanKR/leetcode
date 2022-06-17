import collections

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if num2 == "0" or num1 == "0":
            return "0"
        exp = 0
        maxLen = 0
        interm_res = []
        for i in range(n - 1, -1, -1):
            res = []
            rem, carry = 0, 0
            for j in range(m - 1, -1, -1):
                curProd = int(num1[i]) * int(num2[j]) + carry
                rem, carry = curProd % 10, curProd // 10
                # if rem > 0:
                res.append(rem)
            if carry > 0:
                res.append(carry)
            if exp > 0:
                res = [0]*exp + res
            exp += 1
            maxLen = len(res)
            interm_res.append(res)

        print(interm_res)

        finalRes = []
        carry = 0
        for i in range(maxLen):
            runningSum = carry
            for curRes in interm_res:
                if i < len(curRes):
                    runningSum += curRes[i]
            carry = runningSum // 10
            # if runningSum % 10 > 0:
            finalRes.append(runningSum % 10)
        if carry > 0:
            finalRes.append(carry)

        resString = ''.join([str(finalRes[i]) for i in range(len(finalRes) - 1, -1, -1)])
        return resString


if __name__ == '__main__':
    solution = Solution()
    num1 = "999"
    num2 = "0"
    print(solution.multiply(num1, num2))