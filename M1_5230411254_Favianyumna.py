import math

def tigadimensi():
    print('Ketik 1 untuk menghitung nilai kubus')
    print('Ketik 2 untuk menghitung nilai balok')
    print('Ketik 3 untuk menghitung nilai prisma segitiga')
    print('Ketik 4 untuk menghitung nilai piramida')
    print('===============INSTRUKSI=====================')
    print('Keterangan: Masukkan nilai panjang, lebar, dan sebagainya dalam satuan cm')
    
    Permulaan = int(input('Masukkan pilihan anda: '))
    
    if Permulaan == 1:
        panjang = float(input('Masukkan nilai panjang: '))
        vol_kubus = panjang ** 3
        luas_permukaan_kubus = 6 * (panjang ** 2)
        print(f'Volume Kubus: {vol_kubus} cm³')
        print(f'Luas Permukaan Kubus: {luas_permukaan_kubus} cm²')

    elif Permulaan == 2:
        panjang = float(input('Masukkan nilai panjang: '))
        lebar = float(input('Masukkan nilai lebar: '))
        tinggi = float(input('Masukkan nilai tinggi: '))
        vol_balok = panjang * lebar * tinggi
        luas_permukaan_balok = 2 * (panjang * lebar + lebar * tinggi + tinggi * panjang)
        print(f'Volume Balok: {vol_balok} cm³')
        print(f'Luas Permukaan Balok: {luas_permukaan_balok} cm²')

    elif Permulaan == 3:
        a = float(input('Masukkan panjang sisi segitiga pertama: '))
        b = float(input('Masukkan panjang sisi segitiga kedua: '))
        c = float(input('Masukkan panjang sisi segitiga ketiga: '))
        d = float(input('Masukkan tinggi prisma: '))

        s = (a + b + c) / 2
        luas_segitiga = math.sqrt(s * (s - a) * (s - b) * (s - c))

        vol_prismasgt = luas_segitiga * d
        luas_prismasgt = 2 * luas_segitiga + (a + b + c) * d

        print(f'Volume Prisma Segitiga: {vol_prismasgt} cm³')
        print(f'Luas Permukaan Prisma Segitiga: {luas_prismasgt} cm²')

    elif Permulaan == 4:
        panjang = float(input('Masukkan nilai panjang: '))
        lebar = float(input('Masukkan nilai lebar: '))
        tinggi = float(input('Masukkan nilai tinggi: '))
        vol_pirals = panjang * lebar * tinggi / 3
        luas_pirals = panjang * lebar + (panjang + lebar) * math.sqrt((lebar / 2) ** 2 + tinggi ** 2)
        print(f'Volume Piramida Alas Persegi: {vol_pirals} cm³')
        print(f'Luas Permukaan Piramida Alas Persegi: {luas_pirals} cm²')

    print('Masukkan 0 untuk memakai ulang program ini')
    print('Masukkan apapun selain 0 untuk berhenti di program ini')

    konfirmasi = int(input('Masukkan di sini: '))

    if konfirmasi == 0:
        tigadimensi()
    else:
        print('Terimakasih sudah menggunakan program ini.')

tigadimensi()