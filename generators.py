def linear_congruential_generator(noOfRandomNums):
    Xo = 100
    m = 7
    a = 3
    c = 3
    randomNums = [0] * (noOfRandomNums)
    for i in range(1, noOfRandomNums):
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m
    return randomNums