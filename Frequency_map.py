nums=[1,2,3,4,5,62,11,1,1,1,2,2,3,4,5,6]
# dict1={}
# x=1
# for i in range (0,len(nums)):
#     if  nums[i] in dict1:
#         dict1[nums[i]]+=1
#     else:
#       dict1[nums[i]]=1
#
# print(dict1[x])


hashmap={}
n=len(nums)
for i in range(0,n):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1

print(hashmap)