# 매번 모든 맵을 탐색하지 않고 이전 상태를 저장하여 시간을 최적화

import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split(' '))
sv=[[False for _ in range(c)] for _ in range(r)] # 백조 방문 배열
wv=[[False for _ in range(c)] for _ in range(r)] # 물 방문 배열
dx=[1,0,-1,0]
dy=[0,1,0,-1]
lake=[] # 호수 맵
tar=[] # 백조의 위치
wq, tmp_wq, sq, tmp_sq = deque(),deque(),deque(),deque() # 리스트 보다 데큐가 빠르다

for x in range(r):
    row=list(sys.stdin.readline().rstrip())
    lake.append(row)
    for y, val in enumerate(row):
        if val=='L': # 백조의 위치를 파악한다.
            wq.append((x,y))
            tar.append((x,y)) # 위치를 저장하고
            lake[x][y]='.' # 물로 치환
        if val=='.': # 처음 모든 물을 큐에 넣는다.
            wq.append((x,y))
            wv[x][y]=1

def meeting():
    while sq:
        if(sq[0]==tar[1]): return True # 같으면 끝
        x,y=sq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(0>nx or nx>=r or 0>ny or ny>=c): continue
            if(sv[nx][ny]): continue
            if(lake[nx][ny]=='.'): # 물이면 현재 큐로
                sq.append((nx,ny))
            else: # 얼음이면 다음 큐로
                tmp_sq.append((nx,ny)) 
            sv[nx][ny]=True
    return False # 다르면 0

def melting():
    while wq:
        x,y=wq.popleft()
        if lake[x][y]=='X': # 다음 큐가 현재 큐로 됐을 때 녹인다
            lake[x][y]='.'
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(0>nx or nx>=r or 0>ny or ny>=c): continue
            if(wv[nx][ny]): continue
            if(lake[nx][ny]=='X'): # 얼음이면 다음 큐로
                tmp_wq.append((nx,ny))
            else: # 물이면 현재큐로
                wq.append((nx,ny))
            wv[nx][ny]=True

day=0
sq.append(tar[0])
sv[tar[0][0]][tar[0][1]]=True
while True:
    melting()
    if meeting(): break
    day+=1
    sq, wq = tmp_sq, tmp_wq
    tmp_sq, tmp_wq = deque(),deque()
print(day)



