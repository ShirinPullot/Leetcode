class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_char = {}
        substr_start_i = 0
        max_length = 0
        for i, char in enumerate(s):
            if char in string_char and string_char[char] >= substr_start_i:
                substr_start_i= string_char[char]+1
            else:
                max_length = max(max_length, i-substr_start_i+1)
            string_char[char] =i
        return max_length
            
            