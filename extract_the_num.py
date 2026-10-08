from math import sqrt
#count number
# n=46571
#
# num=n
# count=0
# while num>0:
#     last_digit = num%10
#     count+=1
#     num=num//10
# print(count)

#reverse the number
#
# n=43502145
# num=n
# while num>0:
#     last_digit = num%10
#     print(last_digit,end="")
#     num=num//10

#check parlindrome
# n =1111
# result=0
# num=n
# while num>0:
#     last_digit = num%10
#     result=result*10+last_digit
#     num=num//10
# if n==result:
#     print(f"{n} is palindrome")
#
# else:
#     print("it is not a palindrome")

#
# #armstrong number:
# n= 153
# num=n
# length=len(str(n))
# result=0
#
# while num>0:
#     last_digit = num%10
#     result=result+last_digit**length
#     # print(result)
#     num=num//10
#
# if result==n:
#     print(f"{result} is the armstrong number ")
# else:
#     print("it is not an armstrong number")
##factors
num=36
result =[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
    if num//i!=i:
        result.append(num//i)

result.sort()
print(result)





















