def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call with only the name
greet("Rebecca")

# Call with both arguments
greet("Rebecca", "Good morning")

# Call with greeting as a keyword argument
greet("Rebecca", greeting="Good evening")