def checkio(words):
    l=words.split(' ')
    num=0
    for s in l:
        if s.isalpha():
            num+=1
            if num>2:
                return True
        else:
            num=0
    return  False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"