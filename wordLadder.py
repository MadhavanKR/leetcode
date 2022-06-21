import collections

class Solution:

    def generateNeighbors(self, word):
        words = []
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(len(word)):
            wordArr = list(word)
            for ch in chars:
                wordArr[i] = ch
                words.append(''.join(wordArr))
        return words

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or len(beginWord) == 0 or len(endWord) == 0 or len(wordList) == 0:
            return 0

        wordMap = {}
        for word in wordList:
            wordMap[word] = 1

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while len(queue) > 0:
            currentWord, level = queue.popleft()
            currentNeighbors = self.generateNeighbors(currentWord)
            # print(len(currentNeighbors))
            for neighbor in currentNeighbors:
                if wordMap.get(neighbor, -1) == -1:
                    continue
                if neighbor == endWord:
                    return level + 1
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append((neighbor, level + 1))
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    print(solution.ladderLength(beginWord, endWord, wordList))
