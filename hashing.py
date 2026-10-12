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


#
# s="Aalsdkkamdadsddaz"
# q=["a","s","k","d","m","z"]
# hash_list=[0]*127
# ascii_list = [chr(i) for i in range(65, 127)]
#
# hashmap ={chr(i) for i in range(65, 127)}
#
# for i in s:
#     ascii_value= ord(i)
#     index= ascii_value-65
#     hash_list[index]+=1
# for ch in q:
#     ascii_value=ord(ch)
#     index=ascii_value-97
# print(hash_list)
# print(hashmap)
#


#character hashing

s = "Aalsdkkamdadsddaz"
q = ["a", "s", "k", "d", "m", "z"]

hash_list = [0] * 127

ascii_list = [chr(i) for i in range(65, 123)]
hashmap = {chr(i): 0 for i in range(65, 123)}

# Count character frequencies
for ch in s:
    ascii_value = ord(ch)
    hash_list[ascii_value] += 1
    hashmap[ch] += 1

# Print frequencies of the requested characters
for ch in q:
    print(ch, "=", hash_list[ord(ch)])

print("Hash list:", hash_list)
print("ASCII list:", ascii_list)
print("Hash map:", hashmap)



