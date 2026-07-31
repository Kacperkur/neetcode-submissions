class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # make two pointers that point to the lowest and highest valid portions of the list
        low = 0
        high = len(nums) - 1

        # while the two pointers do not cross
        while low <= high:

            # the middle is the total between the low and high divided by 2 and floored
            mid = (low + high) // 2
            # if the middle is the target return the index
            if nums[mid] == target:
                return mid
            # if the current num is less than our target we make the new low 1 past our midpoint
            elif nums[mid] < target:
                low = mid + 1
            # if the current num is greater than our target we make the new high 1 less the midpoint
            else:
                high = mid - 1
            
        return -1

    