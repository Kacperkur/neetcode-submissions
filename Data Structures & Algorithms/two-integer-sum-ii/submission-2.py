class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        answer = []
        length = len(numbers)
        
        # one pointer iterates through each of the elements becoming the pivot
        # then because index1 > index2 we only check forwards

        for i, number in enumerate(numbers):
            index = 0
            anchor = numbers[i]

            while index + i < length:
                explorer = numbers[index + i]
                # index1 < index2, so the explorer must be at a different index
                if explorer + anchor == target:

                    answer.append(i + 1)
                    answer.append(index + i + 1)
                    return answer
                
                index += 1
        return answer