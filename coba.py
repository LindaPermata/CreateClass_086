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
    
    def main():
        try:
           panjang = float(input("Masukkan panjang persegi panjang: "))
           lebar = float(input("Masukkan lebar persegi panjang: "))
           if panjang <= 0 or lebar <= 0:
               print(" x negatif atau nol")
               return
           PP = PersegiPanjang(panjang, lebar)
           print(PP)
           print("keliling", PP.keliling())
           print("luas", PP.luas())
        except ValueError:
            print("nilai harus sesuai")
            
    main()
            

            
          
