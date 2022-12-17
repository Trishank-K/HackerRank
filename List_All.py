if __name__ == '__main__':
    def checkstring(s):
        b=""
        for i in s:
            if i!=" ":
                b+=i
            else: 
                break
        return b

    l = []
    N = int(input())
    for i in range(0,N):
        n = input()
        check = checkstring(n)
        a = len(check)
        if check == "insert":
            l.insert(int(checkstring(n[a+1:])),int(checkstring(n[a+3:])))
        elif check == "print":
            print(l)
        elif check == "remove":
            l.remove(int(checkstring(n[a+1:])))
        elif check == "append":
            l.append(int(checkstring(n[a+1:])))
        elif check == "sort":
            l.sort()
        elif check == "pop":
            l.pop()
        elif check == "reverse":
            l.reverse()