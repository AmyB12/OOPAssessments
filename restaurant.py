import unittest


class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        self.item = item
        self.price = price
        self.quantity = quantity

        order_details = {'item': item, 'price': price, 'quantity': quantity}
        self.bill.append(order_details)
        for order in self.bill:
            if item == order and price == order['price']:
                order_details["quantity"] += quantity
                self.bill.append(order_details.copy())

    def remove(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

        order_details = self.bill
        for item in order_details:
            items = item['item']
            prices = item['price']
            quant = item['quantity']
            if items == self.item and self.price == prices:
                if quant != self.quantity:
                    item['quantity'] -= self.quantity
                if self.quantity == 0:
                    order_details.pop(item)
                    return False
                else:
                    return True

    def get_subtotal(self):
        subtotal = 0
        order_details = self.bill
        for item in order_details:
            subtotal += item['price'] * item['quantity']
        return subtotal

    def get_total(self, service_charge: float = 0.10):
        return {
            'Sub Total': f"£{format(self.get_subtotal(), '.2f')}",
            'Service Charge': f"£{format(self.get_subtotal() * service_charge, '.2f')}",
            'Total': f"£{format(self.get_subtotal() + (self.get_subtotal() * service_charge), '.2f')}",
        }

    def split_bill(self):
        return self.get_subtotal()/self.number_of_diners
