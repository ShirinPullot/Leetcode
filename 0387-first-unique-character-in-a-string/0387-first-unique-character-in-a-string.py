class Solution:
    def firstUniqChar(self, s: str) -> int:
        n_dict ={}
        n=1
        for i,chr in enumerate(s):
            if chr not in n_dict:
                n_dict[chr]=n
            else:
                n_dict[chr]=n+1
        for i,chr in enumerate(s):
            if n_dict[chr]==1:
                return i
        return -1
       
            
                
        

        