# def greet(count=0):
#     if count==5:
#         return
#     print("laxman ")
#
#     greet(count+1)
#
# greet()

#tail Recursion
# #back tracking
# def greet(count=0):
#     if count == 4:
#         return
#
#     print("Before:", count)
#     greet(count + 1)
#     print("After:", count)  # Work after recursion
#
# greet()

#recusion using parameters
#
# def func(x,num,count=0):
#
#     if count==num:
#         return
#     print(x,count)
#     func(x,num,count+1)
#     print(x,count)
#
# func("laxman",5)
# def func(num1,num2):
#     if num1>num2:
#         return
#     print(num1)
#     func(num1+1,num2)
#
# func(1,5)


# def sun(i,n):
#     if i>n:
#         return
#     #print(i)
#     sun(i+1,n)
#     print(i)
# sun(1,4)


#parameterized & functional Recursion
#
# def func(sum,i,N):
#     if i >N:
#         print(sum)
#         return
#     func(sum+i,i+1,N)
#
# func(0,1,10)

#function recursion

def func(N):
    if N==0:
        return 1
    return N * func(N-1)


print(func(5))

#reverse an arrays using recursions
num=[5,6,21,134,1,13,11,23]

def reverse(num,left,right):
    if left>=right:
        return
    num[left],num[right]=num[right],num[left]
    reverse(num,left+1,right-1)

def reverse_array(num):
       reverse(num,0,len(num)-1)
       return num
#reverse(num,2,5)
print(reverse_array(num))





















