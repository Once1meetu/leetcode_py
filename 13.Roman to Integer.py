"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        I=s.find('I')#calculate ones
        temp=s.find('V')
        if I==temp:
            I=999
        if (temp<I and temp!=-1) or I==-1:
            I=temp
        cur_ones=s[I:]
        X=s.find('X')#calculate tens
        temp=s.find('L')
        if X==temp:
            X=I
        if (temp<X and temp!=-1) or X==-1:
            X=temp
        if X>I:#I=4 or 9
            X=I
        cur_tens=s[X:I]
        C=s.find('C')#calculate hundreds
        temp=s.find('D')
        if C==temp:
            C=X
        if (temp<C and temp!=-1) or C==-1:
            C=temp
        if C>X:#X=4 or 9
            C=X
        cur_hundred=s[C:X]
        cur_thousand=s[:C]
        res=0
        res+=self.rym(cur_thousand,"1","1","M")*1000
        res+=self.rym(cur_hundred,"M","D","C")*100
        res+=self.rym(cur_tens,"C","L","X")*10
        res+=self.rym(cur_ones,"X","V","I")
        return res
    def rym(self,x,a_10,a_5,a_1):#how to make rym into decimal
        local=0
        if x == a_1+a_10:
            local=9
        elif x == a_1+a_5:
            local=4
        else:
            if x.startswith(a_5):
                local+=5
                x=x[1:]
            while x.startswith(a_1):
                x=x[1:]
                local+=1
        return local