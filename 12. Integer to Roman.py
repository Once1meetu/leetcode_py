class Solution:
    def intToRoman(self, num: int) -> str:
        #variables
        thousand=num//1000
        hundred=(num%1000)//100
        teen=(num%100)//10
        ones=num%10
        res="M"*thousand
        res+=self.rym(hundred,"M","D","C")
        res+=self.rym(teen,"C","L","X")
        res+=self.rym(ones,"X","V","I")
        return res
    def rym(self,x,a_10,a_5,a_1):
        res=""
        if x == 9:
            res += a_1+a_10
        elif x == 4:
            res += a_1+a_5
        elif x < 4:
            res += a_1 * x
        elif x > 4:
            res += a_5 + a_1 * (x - 5)
        return res