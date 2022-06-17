def maxNumber(number):
    maxNum = number
    numberString = list(str(number))
    print(numberString)
    count, total = 0, 0
    for i in range(len(numberString)):
        j = i + 1
        maxTillNow = numberString[i]
        while j < len(numberString):
            total += 1
            if numberString[j] > numberString[i] and numberString[j] >= maxTillNow:
                count += 1
                maxTillNow = numberString[j]
                newNum = int(''.join(numberString[:i] + numberString[i:j+1][::-1] + numberString[j+1:]))
                if newNum > maxNum:
                    maxNum = newNum
            j += 1
        # i = j
    print('number of computations: {}/{}'.format(count, total))
    print('maxNumber obtained for {} is {}'.format(number, maxNum))

if __name__ == "__main__":
    inputList = [5340, 2043, 602, 1356, 1080, 123456, 988868, 5235]
    for input in inputList:
        maxNumber(input)
