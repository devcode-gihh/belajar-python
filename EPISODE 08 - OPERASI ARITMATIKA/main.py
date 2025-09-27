# Operasi aritmatika

a = 10
b = 3

# Operasi penjumlahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi modulus (sisa bagi) %
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas operasi, operational precedence
'''
1. kurung -> ()
2. eksponen -> **
3. perkalian -> *, /, **, %, //
4. pertambahan dan pengurangan -> +, -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print("(", x, "+", y, ")", "*", z, "=", hasil)