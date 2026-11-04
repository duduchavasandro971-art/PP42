class MovieTicket:
    # Class attributes
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        # Instance attributes
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        # Increment total tickets sold
        MovieTicket.total_tickets_sold += 1

    def display_details(self):
        print(f"Cinema: {MovieTicket.cinema_name}")
        print(f"Movie: {self.movie_title}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: {self.price} GEL")
        print("-" * 30)


# Create 3 ticket objects
ticket1 = MovieTicket("Avatar", "A1", 15)
ticket2 = MovieTicket("Inception", "B5", 20)
ticket3 = MovieTicket("Interstellar", "C3", 18)

# Print individual ticket details
ticket1.display_details()
ticket2.display_details()
ticket3.display_details()

# Print total tickets sold
print("Total tickets sold:", MovieTicket.total_tickets_sold)