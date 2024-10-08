nama =input("Nama : ")
nim =input("Nim : ")
kelas =input("kelas : ")
aksipertama =float(input("Masukkan aksi pertama : "))
aksikedua =float(input("Masukan aksi kedua : "))

operasi = input("masukkan perintah (+,-,*,/): ")

if operasi == '+':
    hasil = aksipertama + aksikedua
elif operasi == '-':
    hasil = aksipertama - aksikedua
elif operasi == '*':
    hasil = aksipertama * aksikedua
elif operasi == '/':
    if aksikedua != 0:
        hasil = aksipertama / aksikedua
    else:
        hasil = "Error: Pembagian dengan nol!"
else:
    hasil = "Error: Operator tidak valid!"

    print(f"\nNama: {nama}\nNIM: {nim}\nKelas: {kelas}")
print(f"Hasil dari {aksipertama} {operasi} {aksikedua} = {hasil}")