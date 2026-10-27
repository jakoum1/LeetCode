class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        a=x
        x_rev=0
        while a>0 :
            x_rev=(x_rev*10) + (a%10)
            a//=10
        return x==x_rev
