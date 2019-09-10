def unique(aStr):
    if len(aStr) == 0 or len(aStr) == 1 :
        return True
    sortedStr = sorted(aStr)
    for i, val in enumerate(sortedStr):
        print(i)
        if not i == 0:
            if sortedStr[i] == sortedStr[i - 1]:
                return False
    return True

def test():
    assert unique("a") == True
    assert unique("aa") == False
    assert unique("abcdefghijklmnopqrstuvwxyz") == True
    assert unique("abcdefghijklmnopqrstuvwxyzz") == False
    assert unique("234asv") == True
    assert unique("AaA") == False
    assert unique("") == True