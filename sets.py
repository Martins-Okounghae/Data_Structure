# Creating a set

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

Months = {"Jan", "Feb", "Mar"}

Dates = {21, 22, 17}

print("-------------------------------------------------------------------")
print(Days)
print("-------------------------------------------------------------------")

print(Months)
print("-------------------------------------------------------------------")
print(Dates)
print("-------------------------------------------------------------------")

# Accessing Values in a Set

Days_2 = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

print("-------------------------------------------------------------------")
print("Looping through a set of days of the week")

print("-------------------------------------------------------------------")
for d in Days_2:
    print(d)

print("-------------------------------------------------------------------")
# Adding Items to a Set
print("Adding Items to a Set")

print("-------------------------------------------------------------------")

Days_3 = set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days_3.add("Sun")
print("---------------------------------------------------------------------")

print("Adding Items to a Set")
print("---------------------------------------------------------------------")
print(Days_3)

print("---------------------------------------------------------------------")

# Removing Items from a Set

print("Removing Items from a Set")
print("---------------------------------------------------------------------")
Days_3.discard("Sun")

print("---------------------------------------------------------------------")
print("Delete Sunday from the set Days_3")
print("---------------------------------------------------------------------")
print(Days_3)

print("---------------------------------------------------------------------")
# Union of Sets
print("Union of Sets")
print("---------------------------------------------------------------------")

Days_A  = set(["Mon","Tue", "Wed"])

Days_B = {"Wed", "Thu", "Fri", "Sat", "Sun"}

print("Union set Days_A and Days_B", )

AllDays = Days_A | Days_B
print("--------------------------------------------------------------------")
print(AllDays)

print("------------------------------------------------------------------------")

# Intersection of Sets

print("Intersection of Sets Days_AA and Days_BB")
print("-----------------------------------------------------------------------")

Days_AA = set(["Mon","Tue","Wed"])

Days_BB = {"Wed", "Thu", "Fri", "Sat", "Sun"}

AllDays_2 = Days_AA & Days_BB

print(AllDays_2)

print("-----------------------------------------------------------------------")

# Difference of Sets
print("Difference of Sets")

New_Days_A = set(["Mon","Tue","Wed"])

New_Days_B = {"Wed", "Thu", "Fri", "Sat", "Sun"}

New_AllDays = New_Days_A - New_Days_B
print(New_AllDays)
print("-----------------------------------------------------------------------")

# Compare Sets

print("Compare Sets")
New_Days_A2 = set(["Mon","Tue","Wed"])

New_Days_B2 = {"Mon","Tue","Wed", "Thu", "Fri", "Sat", "Sun"}

Subsets = New_Days_A2 <= New_Days_B2
SuperSet = New_Days_B2 >= New_Days_A2

print(Subsets)

print(SuperSet)
print("-----------------------------------------------------------------------")