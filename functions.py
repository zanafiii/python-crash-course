# This code is the example of returning mutliple variables from a function
def multVar():
    firstVar = 3
    secondeVar = 5
    thirdVar = 7
    return firstVar, secondeVar, thirdVar;

a, b, c = multVar()
print(a, b, c)