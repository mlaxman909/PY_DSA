

num= 1111
a= num
reverse =0
while a>0:
    lagest_digit = a%10
    reverse = reverse *10 +lagest_digit
    # print(lagest_digit,end="")
    a =a//10

if num ==reverse:
    print(f"{num} is a palinadrome")

else:
    print("its is not a palinadrone")

