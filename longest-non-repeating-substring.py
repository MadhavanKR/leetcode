#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    
    # def lengthOfLongestSubstring(self, s):
    #     max_substr_len = 0
    #     count = 0
    #     i = 0
    #     while i < len(s):
    #         seen_chars = {}
    #         j = i
    #         while j < len(s) and s[j] not in seen_chars:
    #             seen_chars[s[j]] = True
    #             j += 1
    #         max_substr_len = max(max_substr_len, len(s[i:j]))
    #         i += 1
    #     return max_substr_len

    def lengthOfLongestSubstring(self, s):
        max_substr_len = 0
        start_index = 0
        last_index = {}
        for i in range(len(s)):
            if s[i] in last_index:
                start_index = max(start_index, last_index[s[i]] + 1)
            max_substr_len = max(max_substr_len, i - start_index + 1)
            last_index[s[i]] = i
        return max_substr_len
