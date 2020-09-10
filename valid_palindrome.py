import collections
import re
def ispalindrome_1(s:str) -> bool:
    strs:Deque=collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char)
    while(len(strs)>1):
        if(strs.pop()!=strs.popleft()):
            return False
    return True

def ispalindrome_2(s:str) -> bool:
    s=s.lower()
    s=re.sub('[^0-9a-z]','',s)
    return s==s[::-1]

a = input()
if ispalindrome_2(a):
    print("is palin")
else:
    print("is not palin")