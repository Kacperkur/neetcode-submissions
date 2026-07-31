class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # get the midpoint of the list of nums
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + high

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        

        