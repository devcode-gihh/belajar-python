# a = 10, a adalah variabel dengan nilai 10

# TIPE DATA PYTHON
# tipe data: Angka satuan / tidak ada koma (integer)
data_integer = 1374
print("1. data :", data_integer)
print("- bertipe :", type(data_integer))

# tipe data: Angka dengan koma / pecahan (float)
data_float = 3.3
print("2. data :", data_float)
print("- bertipe :", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "berisi huruf / angka"
print("3. data :", data_string)
print("- bertipe :", type(data_string))

# tipe data: biner true/false (boolean)
data_boolean = True
print("4. data :", data_boolean)
print("- bertipe :", type(data_boolean))

# TYPE DATA PYTHON KHUSUS
# bilangan kompleks
data_complex = complex(5,6)
print("5. data :", data_complex)
print("- bertipe :", type(data_complex))

# TYPE DATA DARI BAHASA C
from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("6. data :", data_c_double)
print("- bertipe :", type(data_c_double))