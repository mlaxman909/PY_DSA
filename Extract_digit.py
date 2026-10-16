

# num= 1111
# a= num
# reverse =0
# while a>0:
#     lagest_digit = a%10
#     reverse = reverse *10 +lagest_digit
#     # print(lagest_digit,end="")
#     a =a//10
#
# if num ==reverse:
#     print(f"{num} is a palinadrome")
#
# else:
#     print("its is not a palinadrone")

#String is palindrome
# def func():
#     s="lamal"
#     n=len(s)
#     left=0
#     right=n-1
#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         left +=1
#         right -=1
#
#     return True
#
# print(func())


#palindrome using recursion
def func(s,left,right):
    if left>=right:
        return True
    if s[left] !=s[right]:
        return False
    return func(s,left+1,right-1)

print(func("laxman",0,5))





