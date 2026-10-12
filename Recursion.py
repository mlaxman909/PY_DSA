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

def func(x,num,count=0):

    if count==num:
        return
    print(x,count)
    func(x,num,count+1)
    print(x,count)

func("laxman",5)













