
languages1 = ["Python", "Java", "C++", "Cobra"]
languages2 = ["Python", "JavaScript", "Cobra", "Ruby"]

# Convert both lists into sets to remove duplicates from each line.
set1 = set(languages1)
set2 = set(languages2)

# Print the set operations.
#If used operator it would be print("Union:", set1 | set2)
print("Union:", set1.union(set2))
#If used operator it would be print("Intersection:", set1 & set2)
print("Intersection:", set1.intersection(set2))

# Print the languages that are in the first set but not the second. If did set2-set 1 then
# would have languages that are in the second set but not the first.
# If used operator it would be print("Difference:", set1 - set2)
print("Difference:", set1.difference(set2))
