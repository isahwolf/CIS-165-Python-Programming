#Isaiah Wolf 5-6-24
#Isaiah_program_6

class Customer:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.type = pet_type
        self.age = age

class Invoice:
    #Sales tax constant
    SALES_TAX_RATE = 0.0975
    
    def __init__(self, customer, pet, charges):
        self.customer = customer
        self.pet = pet
        self.charges = charges
    
    def calculate_tax(self):
        #Calculate sales tax
        return round(self.charges * self.SALES_TAX_RATE, 2)
    
    def calculate_total(self):
        #Calculate total charges including tax
        return self.charges + self.calculate_tax()
    
    def display_invoice(self):
        #Display invoice details
        print("Invoice:")
        print("Customer Name: ", self.customer.name)
        print("Customer Address: ", self.customer.address)
        print("Customer Phone: ", self.customer.phone)
        print("Customer Email: ", self.customer.email)
        print("Pet Name: ", self.pet.name)
        print("Pet Type: ", self.pet.type)
        print("Pet Age: ", self.pet.age)
        print("Charges: $", format(self.charges, ',.2f'))
        print("Sales Tax: $", format(self.calculate_tax(), ',.2f'))
        print("Total Charges: $", format(self.calculate_total(), ',.2f'))

def main():
    #Get customer information
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")
    customer_email = input("Enter customer email address: ")
    
    #Get pet information
    pet_name = input("Enter pet name: ")
    pet_type = input("Enter pet type: ")
    pet_age = int(input("Enter pet age: "))
    
    #Get charges for grooming services
    charges = float(input("Enter charges for grooming services: "))
    
    #Create customer object
    customer = Customer(customer_name, customer_address, customer_phone, customer_email)
    
    #Create pet object
    pet = Pet(pet_name, pet_type, pet_age)
    
    #Create invoice object
    invoice = Invoice(customer, pet, charges)
    
    #Display invoice
    invoice.display_invoice()

if __name__ == "__main__":
    main()
