

def doesBrickFit(a, b, c, w, h):
    #initialize
    first = a
    second = b

    #get the smallest two of the 3 values
    if c < first:
        first = c
        if a < second:
            second = a
    elif c < second:
        second = c
        if b < first:
            first = b

    #make sure first is smaller than second
    if first < second:
        temp = first
        first = second
        second = temp

    #determine if brick could fit
    if w < h:
        if first <= w and second <= h:
            return True
        else:
            return False
    else:
        if first <= h and second <= w:
            return True
        else:
            return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(doesBrickFit(1,1,1,1,1))
    print(doesBrickFit(1,2,1,1,1))
    print(doesBrickFit(1,2,2,1,1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
