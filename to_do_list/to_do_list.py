class ToDoList:
	def __init__(self,to_do,done):
		self.to_do=to_do
		self.done=done
	
	def add(self,task):
	
		self.to_do.append(task)

	def mark_done(self,t):

		self.to_do.remove(t)
		self.done.append(t)

	def see_tasks(self):
		print("TO DO")
		print(self.to_do)
		print("DONE	")
		print(self.done)


