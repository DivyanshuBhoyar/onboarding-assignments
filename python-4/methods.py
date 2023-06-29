class Ticket:
    price = 50

    def __init__(self):
        self.is_booked = False

    def book(self, no):
        self.is_booked = True
        total_price = Ticket.calc_offer_price(Ticket.price) * no
        print(f"{no} ticket booked with total price {total_price}")

    @classmethod
    def incr_price(cls):
        cls.price += cls.price / 10

    
    @staticmethod
    def calc_offer_price(price):
        return price - price * 0.02




