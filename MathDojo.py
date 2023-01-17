# Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.

class MathDojo:
    # attribute: result
    # 2 methods: add and subtract (take at least one parameter but could take many more)

    def __init__(self):
        self.result = 0

    def add(self, num1, *nums):
        if len(nums) > 0:
            for n in nums:
                self.result = self.result + n
        self.result += num1
        return self.result

    def subtract(self, num1, *nums):
        if len(nums) > 0:
            for n in nums:
                self.result -= n
        self.result -= num1
        return self.result
    

# create an instance:
md = MathDojo()

# # to test:
x = md.add(2)
x = md.add(2,5,1)
x = md.subtract(3,2)
x = md.result
print(x)	# should print 5




# run each of the methods a few more times and check the result!

