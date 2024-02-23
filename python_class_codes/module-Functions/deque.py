# double ended queue
# from collections import deque

# stack = deque()


# stack.append("a")
# stack.append("b")
# stack.append("c")

# print(stack)

# topmost_item = stack.pop()
# print("top of stack", topmost_item)
# print(stack)


# double ended queue
from collections import deque

queue = deque()


queue.append("a")
queue.append("b")
queue.append("c")

print(queue)

first_item = queue.popleft()
print(first_item)
print("queue now", queue)
