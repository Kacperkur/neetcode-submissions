class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # to find the max area between two bars we should have a left and a right pointer on both ends
        # then we calculate the total area which would be min(left,right) * length between the two pointers ( Height x width )
            # we take the min because that is the heighest wall we can get without water leaking
        # we store that total area as our current max
        # if the left is the min, then we increase the pointer to move onto the next option with a higher height
        # if the right is the min, we decrease the pointer until we reach one with a higher height 

        length = len(heights)
        curr_max = 0
        left = 0
        right = length - 1

        while left <= right:

            area = min(heights[left],heights[right]) * (right - left)
            
            if area >= curr_max:
                curr_max = area

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left +=1
        return curr_max

            
            

