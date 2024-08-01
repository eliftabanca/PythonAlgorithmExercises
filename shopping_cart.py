#Write a Python class that stores the selected products, their prices, and the quantities added to the cart in a list. 
#This class should store the products and related information, and it should include a method to print all items in the cart. 
#Create an instance of this class with example data and print the items in the cart.

#Bir kullanıcının seçtiği ürünleri, fiyatlarını ve sepete eklenen miktarları bir liste ile tutan bir Python sınıfı yazınız. 
#Bu sınıf, ürünleri ve ilgili bilgileri saklamalı ve sepetteki tüm ürünleri ekrana yazdıran bir metod içermelidir.
#Örnek verilerle bu sınıfın bir örneğini oluşturun ve sepetteki ürünleri ekrana yazdırın

class ShoppingCart:
    def __init__(self):
        self.shopping = [ ["Bag", "100", "10"], ["Tshirt", "70", "5"], ["Had", "50", "90"] ]

instance_shopping = ShoppingCart()

print(instance_shopping)





