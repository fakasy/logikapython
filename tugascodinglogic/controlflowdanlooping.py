#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4
#control flow dan looping saya gabung e mas 😹 soalnya dah buat loop dulu sebelum baca soal no 4

print("if else")


try:
    x = float(input("Masukkan angka : "))
    print("Nilai x:", x)
    if x > 7:
        print("Nilai x lebih besar dari 7")
    elif x == 7:
        print("Nilai x sama dengan 7")
    else:
        print("Nilai x kurang dari 7")
except ValueError:
    print("Input harus berupa angka.")



print("for loop")

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
try:
    buah = input("Masukkan nama buah: ")
    if buah in buah:
        print("Buah", buah, "ada di daftar buah.")
    else:
        print("Buah", buah, "tidak ada di daftar buah.")
except ValueError:
    print("Input harus berupa string.")



print("looping while")

x = int(input("Masukkan angka: "))
while x < 21:
    print(x, "pizza chicken lion")
    x += 1



print("break dan continue")


for i in range(1, 11):
    if i == 5:
        break
    print(i)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("switch case tidak ada  di piton mas 😹")
print("pakai ini saja")

try:
    x = int(input("Masukkan angka: "))
    if x == 1:
        print("Anda memilih angka 1")
    elif x == 2:
        print("Anda memilih angka 2")
    elif x == 3:
        print("Anda memilih angka 3")
    else:
        print("Anda memilih angka lain")
except ValueError:
    print("Input harus berupa angka.")

