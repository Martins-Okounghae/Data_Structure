print("---------------------------------------------------------------")

print("Creating a heap")

print("----------------------------------------------------------------")

#Creating a Heap
print()
import  heapq

H = [21,1,45,78,3,5]

# Use heapify to rearrange the elements

heapq.heapify(H)

print(H)


print("----------------------------------------------------------------")

print("Inserting into heap")

print("----------------------------------------------------------------")

# Inserting into heap

add_to_heap = [21,4,45,78,3,5]

# Convert to a heap

heapq.heapify(add_to_heap)

print(add_to_heap)

# Add a new element to the list

heapq.heappush(add_to_heap, 2)

#heapq.heapify(add_to_heap)

print(add_to_heap)

print("-------------------------------------------------------------")
print("Removing an element from a heap")
print("---------------------------------------------------------------")
# Removing from element from a heap

rm_from_heap = [21, 2, 3, 45, 78, 5, 10]

# Create the heap

heapq.heapify(rm_from_heap)

print(rm_from_heap)

# Removing element from the heap

heapq.heappop(rm_from_heap)

print(rm_from_heap)

print("---------------------------------------------------------------")

print("Replacing an element in a heap")

print("--------------------------------------------------------------")


# Replacing an element in a heap

rep_in_heap =[21,4,8,20,89,90,89,100,102,103,105,108]

# Create the heap

heapq.heapify(rep_in_heap)

print(rep_in_heap)

# Replace an element in a list

heapq.heapreplace(rep_in_heap,9)

#heapq.heapify(rep_in_heap)

print(rep_in_heap)


