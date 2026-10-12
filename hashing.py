# n= [1,2,3,3,4,5,6,7,3,1]
# m=[1,2,22,33,1,23,1,2,7,8,9]
# hashmap=[0]*11
#
# for num in n:
#     hashmap[num]+=1
# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hashmap[num])



s="alsdkkamdadsdda"
q=["q","k","a","d","s"]
hashmap ={}

for i in s:
    if i in q:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1

print(hashmap)