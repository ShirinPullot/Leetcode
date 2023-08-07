class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number =''
        for num in digits:
          number += str(num)
        increment_no = int(number)+1
        new_list = []
        for no in str(increment_no):
          new_list.append(int(no))
        return new_list