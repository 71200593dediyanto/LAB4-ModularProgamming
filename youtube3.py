# Dedi Yanto_71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Modular Programing

'''Suatu hari Sai mengajak seorang perempuan bernama Yui berpacaran. 
Yui memberi tantangan kepada Sai jika dia memang ingin berpacaran dengan Yui, 
maka Sai harus membuatkan sebuah program kalkulator sederhana yang terdiri dari 
3 perhitungan yaitu dapat menghitung bilangan berpangkat, mencari faktor dari 
angka yang diberikan user, dan mencari akar pangkat dari suatu angka positif. 
Yui memberitahukan jika program harus dapat mengatasi eror jika user menginputkan
selain angka, pada inputan. Karena Sai tidak tau bagaimana membuatnya, dia 
meminta pertolongan untuk membantunya. Bantulah sai untuk membuat sebuah 
program kalkulator sederhana yang dapat:
1.	Menghitung bilangan berpangkat
2.	Mencari faktor dari suatu angka yang diberikan
3.	Mencari akar pangkat dari suatu angka positif yang diberikan.
4.	Rumus-rumus yang akan dipakai harus dibuat sebagai fungsi 
5.	Mengatasi eror jika yang diinputkan user selain angka, pada inputan.
'''

'''
input:
1. bilangan berpangkat

1. angka berapa yg ingin di cari
2. pangkat.
proses:
1. 5
2. 3
5**3 = berapa

output:
hasil
masukan angka 1-3
masukan angka 1-3

'''

# Source CODE

        
def pangkatangka(angka1,pangkat):
    hasil1 = angka1**pangkat
    return(hasil1)

def faktor(angka2):
    lisfaktor = []
    for i in range(1,angka2+1):
        if angka2%i == 0:
            lisfaktor.append(str(i))
        else:
            continue
    return(', '.join(lisfaktor))
def akarbilangan(angka3,akar):
    hasil2 = round(angka3**(1/akar),2)
    return(hasil2)

print("x"*5,"Selamat datang di kalkulator Sederhana Dedi","x"*5)
print("Kalkulator ini hanya tersedia perhitungan\n1.Perhitungan berpangkat\n2.Perhitungan Faktor\n3.Perhitungan akar pangkat")
pilihan = input("Pilihan kalkulator mana yang ingin anda pakai?\n:")
try:
    pilihan = int(pilihan)
    if pilihan == 1:
        angka1 =input("Berapa angka yang ingin dipangkatkan?\n: ")
        pangkat =input("Anda ingin pangkatkan keberapa angka tersebut?\n:")
        try:
            angka1 = float(angka1)
            pangkat = float(pangkat)
            print("Hasil dari ",angka1,"^",pangkat,"adalah ",pangkatangka(angka1,pangkat))
        except:
            print("Silahkan masukkan inputan dengan angka!!/koma dengan(.)")
    elif pilihan == 2:
        angka2 = input("Berapa angka yang ingin dicari faktornya?\n:")
        try:
            angka2 = int(angka2)
            print("Faktor dari ",angka2,"adalah ",faktor(angka2))
        except:
            print("Masukkan inputan dengan angka!!")
    elif pilihan == 3:
        angka3 = input("Masukkan angka yang ingin diakar\n:")
        akar = input("Masukkan jumlah akar\n:")
        try:
            angka3 = int(angka3)
            akar = int(akar)
            if angka3 and akar < 0:
                print("Tolong masukkan bilangan bulat positif!!")
            else:
                print("Akar ",akar,"dari ",angka3,"adalah ",akarbilangan(angka3,akar))
        except:
            print("Masukkan inputan dengan angka!!")
    else:
        print("Maaf, Pilihan hanya tersedia 3 pilihan !!!")
except:
    print("Silahkan masukkan inputan dengan angka!!")
