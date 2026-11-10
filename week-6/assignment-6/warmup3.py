def show_temperature():
    temperature = 25
    print(temperature)

show_temperature()

# print(temperature)
# NameError: name 'temperature' is not defined.
def get_temperature():
    temperature = 25
    return temperature

outside_temperature = get_temperature()
print(outside_temperature)