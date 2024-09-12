import math
signal_power = 200
noise_power = 20
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)

degree = 45
radians = degree / 180 * math.pi
print(math.sin(radians))

a = math.sqrt(2) / 2.0
print(a)


