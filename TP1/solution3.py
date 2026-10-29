def celsius_to_fahrenheit ( celsius, round_to=1): #sign(:) coolon
    temp = celsius*9/5 + 32
    return temp
calculated_temp = celsius_to_fahrenheit(45)
print("F temperature = ",(calculated_temp),"F")
print(f"Rerults: {calculated_temp},F") 

def fahrenheit_to_celsius(fahrenhiet, round_to=1):
    return round ((fahrenhiet-32)*5/9,round_to)

print("\n  °C  |  F")
print("------+------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")
    print ("98.6 F=", fahrenheit_to_celsius(98.6),"°C")
    print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))
      
