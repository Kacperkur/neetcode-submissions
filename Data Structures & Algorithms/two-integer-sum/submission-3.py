class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # my first approach is that I need to do a nested loop to check for each index in i if it has a partner j

        # ans = []

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (i != j) and ( nums[i] + nums[j] ) == target:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans


        # Instead I could create a dictionary and for each number subtract it from the target and check if the difference exists in what I have already checked
        ans = []
        seen = {}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
            
            seen[num] = i 
       

