#DAY 1 OF DSA
#TWO SUM DONE!!!


class sum():
    def twosum(self,nums,target):

        hashMap ={}
        for i ,num in enumerate(nums):
            result =target-num
            if result in hashMap:
                return [hashMap[result],i]
            hashMap[num]=i



s=sum()
print(s.twosum([1,2,3,4,5],9))

