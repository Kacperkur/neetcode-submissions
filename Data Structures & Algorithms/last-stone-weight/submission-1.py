class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # firstly sort the array
        # after the array is sorted compare the first two elements
        # if they are == to each other pop() both
        # if the second stone is less than the first stone then destory it and subtract the first stone - the pop() value of the second stone 
        # keep looping until the length of the array is <= 1

        while len(stones) > 1:

            stones.sort(reverse=True)
            print(stones)
            
            
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)

            elif stones[0] > stones[1]:
                destroyed = stones.pop(1)
                stones[0] = stones[0] - destroyed

        if stones:
            return stones[0]
        else:
            return 0
