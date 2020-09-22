import sys
n=int(sys.stdin.readline())
worktable=[sys.stdin.readline().rstrip('\n').split(' ') for _ in range(n)]

res=0
def calculate(today, earn):
    global res
    if(today<n):
        res=max(res,earn)
        nextEarn=earn+int(worktable[today][1])
        nextDay=today+int(worktable[today][0])
        for i in range(n-today):
            calculate(nextDay+i,nextEarn)
    # 마지막 날까지 일하는 경우
    elif today==n: res=max(res,earn)
    else: return

for i in range(n):
    calculate(i,0)

print(res)