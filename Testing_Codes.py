
def revString(name):
  if len(name) < 2:
    print("Your input is less than 2")
  backwards =[]
  for i in range(len(name)-1,-1,-1):
    backwards.append(name[i])
  return backwards


print(revString("m"))