class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        # make an initialized dict
        result = defaultdict(list)
        
        # for each word in the input
        for word in strs:
            count = [0] * 26
            # count the characters in each word
            for ch in word:
                count[ord(ch) - ord('a')] +=1
            # add the char signature as a key to the result, so other words with same signature are added
            result[tuple(count)].append(word)

        return list(result.values())
                    
        # answer = []
        # seen = set()
        # # word is our anchor, the current word
        # for word in strs:
        #     if word in seen:
        #         continue

        #     anagram = []
            
        #     # option is the iterative choice 
        #     for option in strs:
                
        #         # if the length of either is not the same then it cannot be an anagram
        #         if len(option) != len(word):
        #             continue

        #         curr_word = {}
        #         next_word = {}
        #         # for each letter in the word add them to a dictionary
        #         for i in range(len(word)):
        #             curr_word[word[i]] = curr_word.get(word[i], 0) + 1
        #             next_word[option[i]] = next_word.get(option[i], 0) + 1              
                
        #         # add the anagram option to the list, and the set of seen words
        #         if curr_word == next_word:
        #             anagram.append(option)
        #             seen.add(option)

        #     # append the anagram to the answer, it expects a list of lists of strings
        #     answer.append(anagram)
        
                
        # return answer

