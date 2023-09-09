class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Answer=[]
        for i in range(1,n+1):
            print(i)
            if i%3==0 and i%5==0:
                Answer.append('FizzBuzz')
            elif i%3==0:
                Answer.append('Fizz')
            elif i%5==0:
                Answer.append('Buzz')
            else:
                Answer.append(str(i))
        return Answer

                
                

                
            
        