class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        frequency = {}
        for ch in t:
            if ch not in frequency:
                frequency[ch] = 0
            frequency[ch] += 1

        i, j = 0, 0
        res = ""
        windowCounts = {}
        while j < len(s):
            if s[j] not in windowCounts:
                windowCounts[s[j]] = 0
            windowCounts[s[j]] += 1

            while self.isWindowDesirable(windowCounts, frequency):
                if res == "" or len(s[i:j+1]) < len(res):
                    res = s[i:j+1]
                windowCounts[s[i]] -= 1
                i += 1
            j += 1
        return res

    def isWindowDesirable(self, windowCounts, frequency):
        for k, v in frequency.items():
            if k not in windowCounts or windowCounts[k] < v:
                return False
        return True

    def containsSubstring(self, substr, frequency):
        substrFreq = {}
        for ch in substr:
            if ch not in substrFreq:
                substrFreq[ch] = 0
            substrFreq[ch] += 1

        for k, v in frequency.items():
            if k not in substrFreq or substrFreq[k] < v:
                return False
        return True

    def bruteForceMinWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        frequency = {}
        for ch in t:
            if ch not in frequency:
                frequency[ch] = 0
            frequency[ch] += 1
        res = ""
        for i in range(0, len(s) - len(t) + 1):
            for k in range(i, len(s) - len(t) + 1):
                for j in range(0, len(s) - len(t) + 1):
                    substr = s[k:k + len(t) + j]
                    if self.containsSubstring(substr, frequency):
                        if res == "" or len(substr) < len(res):
                            res = substr
        return res

if __name__ == '__main__':
    s, t = "ADOBECODEBANC", "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))
