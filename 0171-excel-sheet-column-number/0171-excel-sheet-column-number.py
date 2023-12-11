class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        uppercase_alphabet = ""
        for i in range(ord('A'), ord('Z') + 1):
            uppercase_alphabet += chr(i)
        alpha_dict = {}
        number_range = range(1,28)
        for letter, num in zip(uppercase_alphabet, number_range):
            alpha_dict[letter] = num
        coloumn_no = 0
        for i, ch in enumerate(reversed(columnTitle)):
            coloumn_no += alpha_dict[ch]*(26**i)
        return coloumn_no
                
            