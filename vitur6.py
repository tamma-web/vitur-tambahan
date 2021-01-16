def infoSaldo():
    print("\n", "*"*3, "INFO SALDO", "*"*3)
    norek = input("Masukkan nomor rekening: ")
    norek = norek.upper()  # variabel norek dijadikan huruf kapital
    fileNasabah()  # memanggil fungsi fileNasabah
    if norek in dataNasabah:  # kondisional jika variabel norek ada di variabel dataNasabah
        for i in dataNasabah:  # perulangan dalam variabel dataNasabah
            if i == norek:  # jika variabel i adalah norek, isi dari variabel i adalah key dari variabel dataNasabah
                # value index 1 dalam key dari dictionary diprint
                print("Saldo rekening anda:", dataNasabah[norek][1])
    else:
        print("Nomor rekening tidak terdaftar")
infoSaldo()