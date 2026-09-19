class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hashmap= {}

        for char in s:
            if char in hashmap:
                 hashmap[char] = hashmap[char] + 1

            else:
                hashmap[char]=1


        for char in t:
            if char not in hashmap:
                return False

            hashmap[char] = hashmap[char] -1

            if hashmap[char] <0:
                return False


        return True




s = Solution()
print(s.isAnagram("laxman","laaxmn"))