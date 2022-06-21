import heapq

class Solution:
    def findCompletableCourse(self, courseImpactMap):
        for k, v in courseImpactMap.items():
            if len(v) == 0:
                return k
        return -1

    def isAllCoursesComplete(self, courseCompletionMap):
        for k, v in courseCompletionMap.items():
            if v == False:
                return False
        return True

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        courseOrder = []
        courseImpactMap = {}
        courseImpact = []

        maxCourseNum = numCourses

        for preReq in prerequisites:
            maxCourseNum = max(maxCourseNum, preReq[0], preReq[1])

        for i in range(maxCourseNum + 1):
            courseImpactMap[i] = []

        for preReq in prerequisites:
            courseImpactMap[preReq[0]].append(preReq[1])

        allCoursesCompleted = False
        courseCompletionMap = {}
        for i in range(numCourses):
            courseCompletionMap[i] = False

        while not allCoursesCompleted:
            completeCourse = self.findCompletableCourse(courseImpactMap)
            if completeCourse == -1:
                return []
            del courseImpactMap[completeCourse]

            for k, v in courseImpactMap.items():
                if completeCourse in v:
                    v.remove(completeCourse)

            if completeCourse < numCourses:
                courseCompletionMap[completeCourse] = True
                courseOrder.append(completeCourse)
            allCoursesCompleted = self.isAllCoursesComplete(courseCompletionMap)

        return courseOrder

        if heapq.nsmallest(1, courseImpact)[0][0] != 0:
            return courseOrder

        while len(courseImpact) > 0:
            impact, courseNo = heapq.heappop(courseImpact)
            if courseNo < numCourses:
                courseOrder.append(courseNo)
        return courseOrder

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    solution = Solution()
    print(solution.findOrder(numCourses, prerequisites))