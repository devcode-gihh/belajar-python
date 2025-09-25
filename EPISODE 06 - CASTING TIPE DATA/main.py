# Casting adalah merubah tipe data ke tipe data lain

# INTEGER -> TIPE DATA LAIN
print("TYPE DATA INTEGER -> TYPE DATA LAIN")
data_int = 9
print("1. data :", data_int, "- type =", type(data_int))

data_float = float(data_int)
print("2. data :", data_float, "- type =", type(data_float))
data_str = str(data_int)
print("3. data :", data_str, "- type =", type(data_str))
data_bool = bool(data_int) # akan false jika nilai int = 0
print("4. data :", data_bool, "- type =", type(data_bool))

# FLOAT -> TIPE DATA LAIN
print("-")
print("TYPE DATA FLOAT -> TYPE DATA LAIN")
data_float = 9.9
print("1. data :", data_float, "- type =", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
print("2. data :", data_int, "- type =", type(data_int))
data_str = str(data_float)
print("3. data :", data_str, "- type =", type(data_str))
data_bool = bool(data_float) # akan false jika nilai float = 0
print("4. data :", data_bool, "- type =", type(data_bool))

# BOOLEAN -> TIPE DATA LAIN
print("-")
print("TYPE DATA BOOLEAN -> TYPE DATA LAIN")
data_bool = True
print("1. data :", data_bool, "- type =", type(data_bool))

data_int = int(data_bool)
print("2. data :", data_int, "- type =", type(data_int))
data_float = float(data_bool)
print("3. data :", data_float, "- type =", type(data_float))
data_str = str(data_bool)
print("4. data :", data_str, "- type =", type(data_str))

# STRING -> TIPE DATA LAIN
print("-")
print("TYPE DATA STRING -> TYPE DATA LAIN")
data_str = "33"
print("1. data :", data_str, "- type =", type(data_str))

data_int = int(data_str)
print("2. data :", data_int, "- type =", type(data_int)) # string harus angka
data_float = float(data_str)
print("3. data :", data_float, "- type =", type(data_float)) # string harus angka
data_bool = bool(data_str) # false jika string kosong
print("3. data :", data_bool, "- type =", type(data_bool))