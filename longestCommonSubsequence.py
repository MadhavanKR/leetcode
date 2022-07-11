from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1), len(text2)

        def bottomUp():
            dp = [[0] * (m + 1) for _ in range(n + 1)]

            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    firstChar = text1[i]
                    firstOccurence = text2.find(firstChar, j, m)
                    excluding = dp[i + 1][j]
                    including = 0 if firstOccurence == -1 else 1 + dp[i + 1][firstOccurence + 1]
                    dp[i][j] = max(excluding, including)
            # prettyPrint(dp)
            return dp[0][0]

        def prettyPrint(matrix):
            for row in matrix:
                print(row)

        @cache
        def dpUtil(i, j):
            if i == n or j == m:
                return 0

            firstChar = text1[i]

            firstOccurence = text2.find(firstChar, j, m)

            # no match
            excluding = dpUtil(i + 1, j)

            # match
            including = 0 if firstOccurence == -1 else 1 + dpUtil(i + 1, firstOccurence + 1)

            return max(excluding, including)

        # return dpUtil(0, 0)
        return bottomUp()

if __name__ == '__main__':
    solution = Solution()
    s1, s2 = 'abcde', 'ace'
    print(solution.longestCommonSubsequence(s1, s2))