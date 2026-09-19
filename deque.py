from _collections import deque as de

list =de([1,2,3,4,5,7,6])

#right pop
print(list.pop())
#left pop
print(list.popleft())
#right append
print(list.append(5))
print(list)

#left append
print(list.appendleft(1))
print(list)