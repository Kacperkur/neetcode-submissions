class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Taking the input and removing non alphanumeric
        cleaned_text = "".join(filter(str.isalnum, s)).lower()
        length = len(cleaned_text)
        # For each character we are going to move two pointers from the head and tail
        for i, char in enumerate(cleaned_text):
        # Then if by the time they reach halfway through they should have the same text
            if i > length // 2:
                break

            head = cleaned_text[i]
            tail = cleaned_text[-1-i]

            if head == tail:
                continue
            else:
                return False
        return True

            

            
