def checkio(*args):
    mi=0
    ma=0
    if args==None:
        return 0
    for x in args:
        if mi==0 and ma==0:
            ma=x
            mi=x
        else:
            if x>ma:
                ma=x
            if x<mi:
                mi=x
    return ma-mi

def checkioanswer(*args):
    try:
        return max(args) - min(args)
    except ValueError:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
