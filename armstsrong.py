a = 12344
nums = a
length = len(str(a))
result = 0

while nums > 0:
    digit = nums % 10
    result = result + digit ** length
    nums = nums // 10

if result == a:
    print("Armstrong number")
else:
    print("Not an Armstrong number")