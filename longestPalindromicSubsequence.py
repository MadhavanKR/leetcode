from functools import cache, lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        def bottomUp():
            dp = [[0] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = 1

            for length in range(2, n + 1):
                for start in range(n - length + 1):
                    end = start + length - 1
                    startChar = s[start]
                    endChar = s[end]
                    if length == 2 and startChar == endChar:
                        dp[start][end] = 2;
                    elif startChar == endChar:
                        dp[start][end] = 2 + dp[start + 1][end - 1]
                    else:
                        including = dp[start][end - 1]
                        excluding = dp[start + 1][end]
                        dp[start][end] = max(including, excluding)
            return dp[0][n - 1]

        def prettyPrint(matrix):
            for row in matrix:
                print(row)

        @cache
        def dpUtil(start, length):
            if length == 1 or length == 0:
                return length

            if s[start] == s[start + length - 1]:
                return 2 + dpUtil(start + 1, length - 2)
            else:
                including = dpUtil(start, length - 1)
                excluding = dpUtil(start + 1, length - 1)
                return max(including, excluding)

        # return dpUtil(0, n)
        return bottomUp()

if __name__ == '__main__':
    solution = Solution()
    input = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
    print(solution.longestPalindromeSubseq(input))