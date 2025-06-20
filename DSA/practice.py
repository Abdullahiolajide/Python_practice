class Product:
    name = "default name"

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price
    
    def __repr__(self):
        return "name: %s " % self.name + "price: %s" % self.price 
product = Product("imge//ef", 3000)
print(product)