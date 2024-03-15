class Solution:
    def maxProfit(self, price: List[int]) -> int:
        l,h=price[0],price[0]
        mx,pro=0,0
        for i in range(len(price)):
            print(price[i]<l," ",pro," ",h)
            if price[i]<l:
                l,h=price[i],price[i]
            else:
                h=price[i]
            pro=h-l
            if mx<pro:
                mx=pro
        return mx
