class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long_prefix = ""
        min_string = min(strs, key = len)
        len_min_string = len(min_string)
       
        for i in range(len(min_string)):
            fist_letter = min_string[i]
            for j in range(len(strs)):
                if fist_letter != strs[j][i]:
                    return long_prefix
            long_prefix+= fist_letter
        return long_prefix
                    
                
            
            
                
        