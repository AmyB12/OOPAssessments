import unittest


class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []
        self.subtotal = []

    def order(self, item, price, quantity=1):
        self.item = item
        self.price = price
        self.quantity = quantity

        order_details = {'item': item, 'price': price, 'quantity': quantity}
        self.bill.append(order_details)
        for item in self.bill:
            if self.item in item:
                order_details["quantity"] += quantity
                self.bill.append(order_details.copy())

    def remove(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

        # order_details = {'item': item, 'price': price, 'quantity': quantity}
        order_details = self.bill
        for item in order_details:
            items = item['item']
            prices = item['price']
            quant = item['quantity']
            if items == self.item and self.price == prices:
                if quant != self.quantity:
                    # order_details = {'item': item, 'price': price, 'quantity': quantity - quantity}
                    item['quantity'] -= self.quantity
                    # order_details.append(quant)
                if self.quantity == 0:
                    order_details.pop(item)
                    return False
                else:
                    return True

    def get_subtotal(self):
        subtotal = []
        for i in 
        subtotals = sum(d['price'] * d['quantity'] for d in self.bill

        self.subtotal.append(subtotals)
        return self.subtotal

    def get_total(self, service_charge=0.10):
        self.subtotal = []
        self.service_charge = service_charge
        self.total = []

        totals = {'Sub Total': sum(d['price'] * d['quantity']for d in self.bill), 'Service Charge': service_charge,
                  'Total': self.total}

        totals['Service Charge'] = self.service_charge * totals['Sub Total']

        totals['Total'] = totals['Service Charge'] + totals['Sub Total']
        return totals


    def split_bill(self):

        gettingsubtotal = self.subtotal
        gettingnumber = self.number_of_diners

        split_total = [i / gettingnumber for i in gettingsubtotal]

        return split_total
