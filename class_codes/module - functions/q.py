from queue import Queue

q = Queue()

q.put("c")
q.put("a")
q.put("b")

# print(list(q))
print(q.get())

if q.empty() is True:
    print("Queue is empty")
else:
    print("Queue is not empty")
