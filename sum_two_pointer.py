def twoSum(nums, target):
    left, right=0, len(nums)-1
    while(left!=right):
        twosum=nums[left]+nums[right]
        if(twosum>target):
            right-=1
        elif(twosum<target):
            left+=1
        else:
            return left, right
    return left, left
nums=list(map(int,input().split()))
a,b=twoSum(nums,20)
if a==b:
    print('none')
else :
    print(a,b)