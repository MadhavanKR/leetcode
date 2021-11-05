#https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        index_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in index_map:
                index_map[nums[i]].append(i)
            else:
                index_map[nums[i]] = [i]
        
        for i in range(n):
            second_num = target - nums[i]
            if second_num in index_map:
                if second_num == nums[i] and len(index_map[second_num]) > 1:
                    return i, index_map[second_num][1]
                elif second_num != nums[i]:
                    return i, index_map[second_num][0]
        
