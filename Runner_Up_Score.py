if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    i=1
    n = len(arr)
    while(i<=n):
        j=0
        while(j<=n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j+=1
        i+=1
    max = arr[len(arr)-1]
    i=len(arr)-1
    while(i>=0):
        if(max!=arr[i]):
            max = arr[i]
            break
        i-=1
    print(max)
