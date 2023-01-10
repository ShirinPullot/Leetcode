class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict={}
        t_dict={}
        for char in s:
            if char in s_dict:
                s_dict[char]+=1
            if char not in s_dict:
                s_dict[char]=1
        for char in t:
            if char in t_dict:
                t_dict[char]+=1
            if char not in t_dict:
                t_dict[char]=1
        if s_dict==t_dict:
            return True
        else:
            return False