class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, nums):
        i = num + nums
        print(i)
        return self
    
    def subtract(self, num, nums):
        e = num - nums
        print(e)
        return self
            


# crear una instancia:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2)
print(x)	

