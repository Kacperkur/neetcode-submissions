class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The simplest solution I can think of is that I run a loop that will convert both strings into dictionaries 
        # the iterations will end once the word is complete, comparing the contents of the dictionaries using a set,
        # if S != T in length it should be false, 

        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False
        # now that we confirmed they are of the same length we can use len(s) or len(t)
        else:
            for i in range(len(s)):
                dict1[s[i]] = dict1.get(s[i],0) + 1
                dict2[t[i]] = dict2.get(t[i],0) + 1
            # use set arithmetic to compare dictionaries 
            if dict1 == dict2:
                return True
        return False




