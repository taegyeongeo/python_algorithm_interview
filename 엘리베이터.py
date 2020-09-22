import sys
number="""###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###"""
numbers=[[ele[4*(i-1):4*i-1] for ele in number.split('\n')] for i in range(1,11)]

n=int(sys.stdin.readline())
input_nums=''.join([sys.stdin.readline() for _ in range(5)])
seg_nums=[[ele[4*(i-1):4*i-1] for ele in input_nums.split('\n')] for i in range(1,n+1)]

availNum=[]
availNumLen=[]
for input_num in seg_nums:
    numberCnt=0
    tmp=[]
    for number in numbers:
        isAvail=True
        for x in range(5):
            for y in range(3):
                if(input_num[x][y]==number[x][y] or (input_num[x][y]=='.'and number[x][y]=='#')): continue
                else:
                    isAvail=False
                    break
            if(not isAvail): break
        if(isAvail):
            tmp.append(numberCnt)
        numberCnt+=1
    availNum.append(tmp)
    availNumLen.append(len(tmp))

total_sum=0
total_cnt=1

for size in availNumLen:
    if size==0:
        print(-1)
        exit(0)
    total_cnt*=size

for i in range(n-1,-1,-1):
    mul=1
    for j in range(0,n):
        if(j==n-(i+1)): continue
        mul*=availNumLen[j]
    for num in availNum[n-(i+1)]:
        total_sum+=(num*(10**i)*mul)
#         print(total_sum)
# print(availNum)
print(total_sum/total_cnt)

