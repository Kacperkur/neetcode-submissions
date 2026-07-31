class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # make two pointers that point to the lowest and highest valid portions of the list
        low = 0
        high = len(nums) - 1

        # while the two pointers do not cross
        while low <= high:

            # the middle is the total between the low and high divided by 2 and floored
            mid = (low + high) // 2
            # if the current num is less than our target we make the new low 1 past our midpoint
            if nums[mid] < target:
                low = mid + 1
            # if the current num is greater than our target we make the new high 1 less the midpoint
            elif nums[mid] > target:
                high = mid - 1
            # otherwise we are on the nose and can return the index of the target
            else:
                return mid

        return -1

    