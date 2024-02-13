class Solution:
    def isValid(self, s: str) -> bool:
        chr_dict = {'(': ')', '[': ']', '{': '}'}
        chr_stack =[]
        for chr in s:
            chr_stack.append(chr)
        new_chr_stack = []
        while chr_stack:
            top_chr = chr_stack.pop()
            if new_chr_stack and chr_dict.get(top_chr) == new_chr_stack[-1]:
                new_chr_stack.pop()
            else:
                new_chr_stack.append(top_chr)
        return len(new_chr_stack) == 0
