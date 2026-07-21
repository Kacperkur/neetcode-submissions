class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate through the whole list
        # for each number increase the frequency of its appearance using a dictionary
        # when complete sort keys by highest value
        # return top k keys
        frequency = {}
        for item in nums:
            frequency[item] = frequency.get(item,0) + 1
        
        sorted_dict = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]
