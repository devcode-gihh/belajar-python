# Episode input user

# Data yang dimasukan pasti string
data_str = input("Masukan Username :")
print("Username :", data_str, "-> Type data :", type(data_str))

# Jika kita ingin mengambil integer, maka
data_int = int(input("Masukan Umur :"))
print("Umur :", data_int, "-> type data :", type(data_int))

# Jika kita ingin mengambil float, maka
data_float = float(input("Masukan nilai float :"))
print("Float :", data_float, "-> type data :", type(data_float))

# Jika kita ingin mengambil boolean, maka
data_boolean = bool(int(input("Masukan nilai boolean :")))
print("Boolean :", data_boolean, "-> type data :", type(data_boolean))