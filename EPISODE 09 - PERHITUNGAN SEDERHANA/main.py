# Latihan konversi satuan temperature

# Program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukan suhu dalam celcius : "))
print("Suhu adalah", celcius, "Celcius")

# reamur
# rumus -> (4/5) * C
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
# rumus -> (9/5) * C + 32
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
# rumus -> C + 273
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")