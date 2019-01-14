from to_do_list import ToDoList
to_do=[]
done=[]
a=ToDoList(to_do,done)
c=int(input("Enter choice\n 1:Enter task\n 2:Exit"))
if c==1:
	n=int(input("Enter number of tasks to be added"))
	for i in range(n):
		item=input("Enter the task to be added")
		a.add(item)
	d=input("Enter the task to be marked as done")
	a.mark_done(d)
	a.see_tasks()
else:
	exit()
