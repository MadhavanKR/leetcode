import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, a):
        n = len(a)
        res = -sys.maxsize
        for i in range(n):
            for j in range(n-1, i, -1):
                temp = abs(a[i] - a[j]) + abs(i - j)
                if temp > res:
                    res = temp
        return res

if __name__ == '__main__':
    input = [1, 3, -1]
    solution = Solution()
    print(solution.maxArr(input))