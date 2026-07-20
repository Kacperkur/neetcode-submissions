class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # my first approach is that I need to do a nested loop to check for each index in i if it has a partner j

        ans = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and ( nums[i] + nums[j] ) == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
