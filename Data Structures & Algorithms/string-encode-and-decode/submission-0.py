class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            length = str(len(word))
            encoded_sub = length + "#" + word
            encoded_str += encoded_sub
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        # lengthOfString | delim | String
        decoded_str = []
        i = 0
        
        
        while i < len(s):
            j = i
            # while we do not reach our delim we increase the index of j
            while s[j] != '#':
                j += 1
            # then once we reach the delim we grab the string from the beginning to the end and that is our length's string
            length = int(s[i:j])
            # then we make our new beginning where we last left off +1 to move past the delim
            i = j+1
            # and our j will be where i is plus the length so that we can grab the entirity of our string
            j = i + length
            decoded_str.append(s[i:j])
            # begin the process again by making i where we last left off so we can get the new length
            i=j
        return decoded_str



             


                

            
            

