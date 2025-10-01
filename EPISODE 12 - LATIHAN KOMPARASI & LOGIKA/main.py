# Latihan logika & komparasi

# Membuat gabungan area rentang dari angka
print("++++++3--------10+++++++")
# ++++++3--------10+++++++
inputUser = float(input("Masukan angka yang bernilai < 3 atau > 10:"))

# ++++++3-----------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------------10+++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# Hasil akhir penggabungan
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)

print("------3++++++++10-------")
# ------3++++++++10-------
# Kasus irisan
inputUser = float(input("Masukan angka yang bernilai > 3 atau < 10:"))

# ------3+++++++++++++++++
# Memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# +++++++++++++++10-------
# Memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

# Hasil akhir penggabungan
isCorrect2 = isLebihDari and isKurangDari
print("Angka yang anda masukan: ", isCorrect2)