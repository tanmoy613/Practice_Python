class Train:
    def __init__(self, trainname, trainnumber, seats, fair):
        self.trainname = trainname
        self.trainnumber = trainnumber
        self.seats = seats
        self.fair = fair
    def getFair(self):
        if self.trainnumber==11045:
            print('The fair of the train is Rs 90')
        elif self.trainnumber==11406:
            print('The fair of the train is Rs 290')
    def getSeatStatus(self):
        print('Total number of available seats ', self.seats)
    def bookTicket(self):
        if self.seats > 0:
            print('Your ticket has been booked.')
            print(f'Your confirmed seat number is {self.seats}')
            self.seats -= 1

t = Train('Rajdhani Express', 11406, 10, 290)
t.getFair()
t.getSeatStatus()
t.bookTicket()
t.getSeatStatus()    