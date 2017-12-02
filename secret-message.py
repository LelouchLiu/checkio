def find_message(text):
    """Find a secret message"""
    l=[]
    flag=False
    for c in text:
        if c.isupper():
           l.append(c)
           flag=True
    if flag:
        return ''.join(l)
    
    else:
        return ""
find_message1= lambda t:''.join([i for i in t if i.isupper()])
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
