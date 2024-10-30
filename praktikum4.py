class PersegiPanjang:
    def __init__(self, p, l):  # Konstruktor yang benar
        self.p = p
        self.l = l

    def keliling(self):
        return 2*self.p + 2*self.l

    def luas(self):
        return self.p*self.l

    def __str__(self):  # Menggunakan __str__ 
        return "Persegi Panjang, panjang = " + str(self.p) + " cm, dan lebar = " + str(self.l) + " cm"

panjang = float(input("Masukkan panjang persegi panjang: "))
if panjang < 0:
    raise ValueError("Panjang tidak boleh negatif")
lebar = float(input("Masukkan lebar persegi panjang: "))
if lebar < 0:
    raise ValueError("Lebar tidak boleh negatif")
    
pp = PersegiPanjang(panjang, lebar)
print("Keliling persegi panjang =", pp.keliling(), "cm")
print("Luas persegi panjang: ", pp.luas(), "cm2")
print(pp.__str__())
