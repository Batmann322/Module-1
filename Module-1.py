#Task-1
message = "Hello, this is the first message."
print(message)

message = "Now this is the second message."
print(message)

#Task-2
user_name = "Ivan"
print(f"Hello, {user_name}, would you like to learn some Python today?")

#Task-3
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

#Task-4
user_name = "   \tIvan\n   "
print(f"With spaces: '{user_name}'")
print(f"Lstrip: '{user_name.lstrip()}'")
print(f"Rstrip: '{user_name.rstrip()}'")
print(f"Strip: '{user_name.strip()}'")

#Task-5
print("Nazar Kopylchak")
print("Ukraine")
print("79069")
print("Lviv, Shevchenko St, 360")

#Task-6
distance_meters = 5000
inches = distance_meters * 39.3701
feet = distance_meters * 3.28084
miles = distance_meters * 0.000621371
yards = distance_meters * 1.09361
print(f"Inches: {inches:.2f}")
print(f"Feet: {feet:.2f}")
print(f"Miles: {miles:.2f}")
print(f"Yards: {yards:.2f}")

#Task-7
days = 5
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"Hours:    {hours:<10}")
print(f"Minutes:  {minutes:<10}")
print(f"Seconds:  {seconds:<10}")

#Task-8
celsius = 25
fahrenheit = 32 + 9/5 * celsius
kelvin = celsius + 273.15
print(f"{'Fahrenheit':^15}: {fahrenheit:^15.2f}")
print(f"{'Kelvin':^15}: {kelvin:^15.2f}")

#Task-9
number = 6259
digits = [int(digit) for digit in str(number)]
total_sum = sum(digits)
print(" + ".join(str(digit) for digit in digits) + f" = {total_sum}")

#Task-10
import math

# Координати у градусах
x1, y1 = 39.9075000, 116.3972300  # Пекін
x2, y2 = 50.4546600, 30.5238000   # Київ
x1, y1 = math.radians(x1), math.radians(y1)
x2, y2 = math.radians(x2), math.radians(y2)
earth_radius = 6371.032
distance = earth_radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print(f"Distance: {distance:>10.3f} km")

#Task-11
distance_meters = float(input("Enter distance in meters: "))
print(f"Inches: {distance_meters * 39.3701:.2f}")

#Task-12
distance_meters = 5000 
inches = distance_meters * 39.3701 
print(f"Inches: {inches:.2f}")