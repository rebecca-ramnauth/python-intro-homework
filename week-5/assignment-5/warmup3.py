names = ["Ashlyn", "Blair", "Courtney", "Deliah", "Edeline"]
name_search = input("Enter a name to search for: ")

# Assume the name has not been found.
name_found = False

# Loop through the list, checking each name and its index.
# enumerate() gives both the index and the item during each iteration.
for index, name in enumerate(names):
    # Compare both names in lowercase to ignore capitalization.
    if name.lower() == name_search.lower():
        print(f'Found "{name_search}" at index {index}.')
        name_found = True
        break

# Display a message if no matching name was found.
if not name_found:
    print(f'"{name_search}" was not found in the list.')