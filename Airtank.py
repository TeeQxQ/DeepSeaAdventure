class Airtank:

    def __init__(self, size):
        self.size = size
        self.airLeft = size

    def isEmpty(self):
        return self.airLeft <= 0

    def airLeft(self):
        return self.airLeft

    def consume(self, amount):
        self.airLeft -= amount
        if self.airleft < 0:
            self.airLeft = 0

