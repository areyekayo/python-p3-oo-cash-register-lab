#!/usr/bin/env python3

class CashRegister:
	def __init__(self, discount=0):
		self.discount = discount
		self.total = 0
		self.items = []
		self.last_transaction_amount = 0
			
	def add_item(self, title, price, quantity=1):
		self.total += price * quantity
		self.last_transaction_amount = price * quantity
		i = 1
		while i <= quantity:
			self.items.append(title)
			i += 1

	def apply_discount(self):
		if self.discount == 0:
			print("There is no discount to apply.")
		else:
			total_after_discount = int(self.total - (self.total * float(self.discount / 100)))
			print(f"After the discount, the total comes to ${total_after_discount}.")
			self.total = total_after_discount

	def void_last_transaction(self):
		self.total = self.total - self.last_transaction_amount
        
	
        

