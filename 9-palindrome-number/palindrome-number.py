class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        a=x
        L=[]
        n=-1
        while a!=0 :
            r=a%10
            a=a//10
            n+=1
            L.append(r)
        new_x=0
        for num in L :
            new_x+=num*(10**n)
            n-=1
        if x==new_x :
            return True
        return False