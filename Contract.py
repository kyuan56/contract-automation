class Contract:
	def __init__(self,num):
		self.num=int(num)
		self.price=0
		self.name=""
	def addPrice(self,price,discount):
		self.price=price*discount
	def addName(self,name):
                self.name=name
	def isSame(self,num):
		return (self.num==int(num))
