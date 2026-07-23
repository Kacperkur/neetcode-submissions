class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create a dictionary that will carry all complements
        complements = defaultdict(int)
        # for each item in the dict
        for i in range(len(numbers)):
            # find the complement that is needed to fulfill the target
            temp = target - numbers[i]
            # if it exists in the dict, then we found our answer
            if complements[temp]:
                return [complements[temp], i + 1]
            # otherwise update the complements with the index
            complements[numbers[i]] = i + 1
        return []


        # answer = []
        # length = len(numbers)
        
        # # one pointer iterates through each of the elements becoming the pivot
        # # then because index1 > index2 we only check forwards

        # for i, number in enumerate(numbers):
        #     index = 0
        #     anchor = numbers[i]

        #     while index + i < length:
        #         explorer = numbers[index + i]
        #         # index1 < index2, so the explorer must be at a different index
        #         if explorer + anchor == target:

        #             answer.append(i + 1)
        #             answer.append(index + i + 1)
        #             return answer
                
        #         index += 1
        # return answer