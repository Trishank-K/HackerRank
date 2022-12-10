if __name__ == '__main__':
    records = []
    count = 0
    max=1000
    names = []

    def findmax(lis):
        max1=0
        for i in range(len(lis)):
            if(max1>lis[i][1]):
                max1=lis[i][1]
        return max1

    for i in range(int(input())):
        name = input()
        score = float(input())
        records = records + [[name,score]]
    max=findmax(records)
    for i in range(len(records)):
        if(max==records[i][1]):
            records[i][1]=-1
    max = findmax(records)
    for i in range(len(records)):
        if(max==records[i][1]):
            names += [records[i][0]]
    names.sort()
    for names in names:
        print(names)