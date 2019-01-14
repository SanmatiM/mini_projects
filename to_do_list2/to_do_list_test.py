class ToDoListTest:
	def __init__(self,to_do,done):
		self.to_do=to_do
		self.done=done
	
	def add(self):
		n=int(input("Enter number of tasks to be added"))
		for i in range(n):
			item=input("Enter the task to be added")
			self.to_do.append(item)

	def mark_done(self):
		d=input("Enter the task to be marked as done")
		self.to_do.remove(d)
		self.done.append(d)

	def see_tasks(self):
		print("TO DO")
		print(self.to_do)
		print("DONE	")
		print(self.done)