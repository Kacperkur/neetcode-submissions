class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i would convert the array into a dictionary and if a key's value was greater than 1 i would return true
        dictionary = {}

        for item in nums:
            dictionary[item] = dictionary.get(item,0) + 1
            if dictionary[item] > 1:
                return True
        return False
