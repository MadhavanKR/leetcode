class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [-1] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, min(i+nums[i]+1,len(nums))):
                if dp[j] == 1:
                    dp[i] = 1
                    break
        return dp[0] == 1


if __name__ == '__main__':
    input = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]
    solution = Solution()
    print(solution.canJump(input))
