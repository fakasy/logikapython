

# integer 
angka = int(input("Masukkan angka: "))
print("ini adalah", type(angka), "isi variabelnya", angka)

# float
desimal = float(input("Masukkan angka dengan memgunakan titik, contoh: 3.14: "))
print("ini adalah", type(desimal), "isivariabelnya", desimal)

# string
teks = input("Masukkan teks: ")
print("ini adalah", type(teks), "isi variabelnya", teks)

# boolean
input("boolean a atau b: ")
a = True
b = False
print("ini adalah", type(a), "isivariabelnya", a)
print("ini adalah", type(b), "isivariabelnya", b)



# list
nama = input("Masukkan nama Anda (pisahkan dengan koma): ")
nama_list = nama.split(",")
print("Halo, " + nama_list[0])

# tuple
tupleku = tuple(input("Masukkan tuple: ").split())
print("ini adalah", type(tupleku), "isi variabelnya",tupleku)

# set
setku = set(input("Masukkan set: ").split())
print("ini adalah", type(setku), "isivariabelnya", setku)

# dictionary
dictku = dict()
dictku['nama'] = input("Masukkan nama: ")
dictku['umur'] = int(input("Masukkan umur: "))
print("ini adalah", type(dictku), "isi variabelnya", dictku)


