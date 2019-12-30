def myfunc():
    text = input().split(" ")
    text.sort(key=len)
    print(text)
myfunc()