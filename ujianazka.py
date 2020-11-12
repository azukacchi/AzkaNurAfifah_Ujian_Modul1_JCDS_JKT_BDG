### Azka Nur Afifah
### Ujian Modul 1

### nomor 1
def create_phone_number():
    angka = input('Input your phone number: ')
    # angka = '@!##%#$'
    if angka.isdigit():
        if len(angka) == 10:
            kodearea = angka[:3]
            telp = angka[3:]
            print(f'({kodearea}) {telp[:4]}-{telp[4:]}')
        else: print('Digits must be in length of 10, not more or less')
    elif '-' in angka:
        print('Input only positive number')
     
    else: 
        for i in angka:
            if i.isalpha():
                print('Invalid input. No alphabet')
                break
            elif i in '1234567890':
                continue
            else:
                print('Invalid input. No Symbols')
                break
    
create_phone_number()

### akhir nomor 1

### nomor 2

def moveZeros(daftar):
    listbaru = []
    hapus = 0
    for i in daftar:
        if i == 0:
            if type(i) == bool:
                listbaru.append(i)
            else:
                hapus += 1
        else:
            listbaru.append(i)
    for i in range(hapus):
        listbaru.append(0)
    print(f'result: {listbaru}')
    
daftar1 = [False, 1, 0, 1, 2, 0, 1, 3, 'a']
daftar2 = [0, 0, 0, 'Test', 0, 3, 'a', True, False]
daftar3 = [0, True, True, False, 'a', 'b', 1, 1, 1]

moveZeros(daftar1)
moveZeros(daftar2)
moveZeros(daftar3)

### akhir nomor 2


## nomor 3
class Statistic():

    def mean(self, nilai):
        if self.cek(nilai):
            # print('lanjut')
            jml = 0
            for i in nilai:
                jml += i
            rata2 = jml/len(nilai)
            # print(f'{rata2:.3f}')
            return rata2
        # else: pass
    
    def median(self, nilai):
        if self.cek(nilai):
            nilai.sort()
            m = len(nilai)
            if m%2 == 0:
                tengah = int(m/2)
                # print((nilai[tengah-1]+nilai[tengah])/2)
                return (nilai[tengah-1]+nilai[tengah])/2
            else:
                tengah = int((m+1)/2)
                # print(nilai[tengah-1])
                return nilai[tengah-1]
            # print(f'indeks: {tengah}')
            # print(nilai)
    
    def mode(self, nilai):
        if self.cek(nilai):
            nilai.sort()
            # nilai2 = list(nilai)
            # print(nilai2)
            nilaibaru = set(nilai)
            nilaibarulist = list(nilaibaru)
            # print(nilaibaru)
            freklist = [0 for i in range(len(nilaibaru))]
            for i in nilai:
                # frek = 0
                if i in nilaibaru:
                    # frek += 1
                    freklist[nilaibarulist.index(i)] += 1
            # print(freklist)
            
            nilaimaks = max(freklist)
            nilaimodus = []
            for angka, frek in zip(nilaibarulist, freklist):
                if frek == nilaimaks:
                    nilaimodus.append(angka)
            if len(nilaimodus) > 1:
                # print('Tidak ada modus')
                return f'Tidak ada modus'
            else:
                # print(nilaimodus[0])
                return nilaimodus[0]
    
    def std(self, nilai):
        if self.cek(nilai):
            rata = self.mean(nilai)
            jmltotal = 0
            for i in nilai:
                jml = (i-rata)**2
                jmltotal += jml
            stdev = (jmltotal/len(nilai))**0.5
            # print(f'{stdev:.3f}')
            return stdev
            # return stdev

    
    def cek(self, nilai):
        for i in nilai:
            if isinstance(i, int):
                continue
            else:
                print('Invalid input! All values must be Integer.')
                return False
        return True

nilai1 = [12,10,10,10,10]
nilai2 = [4,5,2,1,6,7]
nilai3 = [1,2,3,'a']
st = Statistic()
print('mean')
print(st.mean(nilai1))
print(st.mean(nilai2))
print(st.mean(nilai3))
print('med')
print(st.median(nilai1))
print(st.median(nilai2))
print(st.median(nilai3))
print('mod')
print(st.mode(nilai1))
print(st.mode(nilai2))
print(st.mode(nilai3))
print('std')
print(st.std(nilai1))
print(st.std(nilai2))
print(st.std(nilai3))
