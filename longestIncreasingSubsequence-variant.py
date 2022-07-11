
def maxSum(products):
    print('products: {}'.format(products))
    n = len(products)
    leftToRight = [0] * len(products)
    rightToLeft = [0] * len(products)
    leftToRight[0] = products[0]
    rightToLeft[n-1] = products[n-1]
    minExpected = products[n-1] - 1
    for i in range(n-2, -1, -1):
        print('index {} - minExpected: {}'.format(i, minExpected))
        if products[i] <= minExpected:
            rightToLeft[i] = rightToLeft[i+1] + products[i]
            minExpected = products[i] - 1
        elif (rightToLeft[i+1] + minExpected) > products[i]:
            rightToLeft[i] = rightToLeft[i+1] + minExpected
            minExpected = minExpected - 1
        else:
            rightToLeft[i] = products[i]
            minExpected = products[i] - 1

    print('rightToLeft: {}'.format(rightToLeft))
    minExpected = products[0] + 1
    for i in range(1, n):
        if products[i] <= minExpected:
            leftToRight[i] = products[i] + products[i] - 1
            minExpected = products[i] + 1
        else:
            leftToRight[i] = leftToRight[i-1] + products[i]
            minExpected = products[i] + 1
    print('leftToRight: {}'.format(leftToRight))
    return max(max(rightToLeft), max(leftToRight))

if __name__ == '__main__':
    productsList = [[7, 4, 5, 2, 6, 5], [2, 5, 6, 7], [2, 9, 4, 7, 5, 2]]
    for products in productsList:
        print(maxSum(products))