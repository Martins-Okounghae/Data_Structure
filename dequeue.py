import collections

print("-----------------------------------------------")

print("Double-ended queue")

print("-----------------------------------------------")


DounbleEnded = collections.deque(["Mon","Tue","Wed"])

DounbleEnded.append("Thu")

print("Appended at right - ")
print(DounbleEnded)

DounbleEnded.appendleft("Sun")

print("Appended at left is - ")
print(DounbleEnded)


DounbleEnded.pop()

print("Deleting from right - ")

print(DounbleEnded)



DounbleEnded.popleft()
print("Deleting from left - ")
print(DounbleEnded)





