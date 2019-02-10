from random import randint

def getRandomChar(charList, length=None):
    ret = ''
    if length:
        mLength = length
    else:
        mLength = randint(5, 10)

    for i in range(mLength):
        ret += charList[randint(0, len(charList)-1)]

    return ret

charList = [chr(i) for i in range(97, 122)]
print getRandomChar(charList)
