class Product:
    def __init__(self, name, price, quantity, may_expire, shipped):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expired = may_expire
        self.shipped = shipped

    def isshipped(self):
        return self.shipped
    
class Customer:
    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def remove_balance(amount):
        if amount <= balance:
            balance -= amount
            return True
        else:
            return False
        
    @staticmethod
    def add_balance(amount):
        balance += amount
        return True
        
class Cart:
    def __init__(self):
        self.items = []
        self.quantities = []

    def add_item(self, product, quantity):
        self.items.append(product)
        self.quantities.append(quantity)
        product.quantity -= quantity
        if product.quantity <= 0:
            print("Product is out of stock")
            self.items.remove(product)
            
    def calculate_total(self):
        total = 0
        subtotal = 0
        fees = 0
        lst = []
        for idx, item in enumerate(self.items):
            if item.expired:
                continue
            if item.shipped:
                subtotal += item.price * self.quantities[idx]
                print(subtotal)
                fees += item.price * self.quantities[idx] * 0.1
                continue

        total += subtotal + fees
        lst.append(subtotal)
        lst.append(fees)
        lst.append(total)   
        return lst
    
    def clear_cart(self):
        self.items = []
    
    def isempty(self):
        return len(self.items) == 0
    
    def get_quantity(self):
        return self.quantities

Customer(10000)
cart = Cart()
cheese = Product("Cheese", 100, 20, True, True)
tv = Product("TV", 10000, 10, False, True)
scratchCard = Product("ScratchCard", 100, 19, False, False)


cart.add_item(cheese, 2)
cart.add_item(tv, 1)
cart.add_item(scratchCard, 3)

lst = cart.calculate_total()
print("\nCONSOLE OUTPUT")
print("** SHIPPMENT NOTICE **")

if cheese.isshipped():
    weight1 = 0.4
if tv.isshipped():
    weight2 = 1.0

print(f"2X Cheese\t{weight1}kg\n1X TV\t\t{weight2}kg\nTotal Package weight {weight1 + weight2}\n-------------------------")
print("** Checkout receipt **")
print(f"Subtotal: \t{lst[0]}")
print(f"Shipping: \t{lst[1]}")
print(f"Total: \t\t{lst[2]}")

