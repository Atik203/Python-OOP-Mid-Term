class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        self.__hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        self.seats[show_id] = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def book_seats(self, show_id, booked_seats):
        show_seats = self.seats.get(str(show_id))
        if show_seats is None:
            print("\nInvalid show id\n")
            return
        for seat in booked_seats:
            row, col = seat
            if not (0 <= row < self.rows and 0 <= col < self.cols):
                print("\nInvalid seat\n")
                return
            if show_seats[row][col] == 1:
                print("\nSeat already booked\n")
                return
            show_seats[row][col] = 1
        print(f"\nSeat({row},{col}) booked successfully\n")


    def view_show_list(self):
        print(f'\nHall No: {self.hall_no}\n')
        for show in self.__show_list:
            print(f'ID: {show[0]}      Name:{show[1]}      Time:{show[2]}')

    def view_available_seats(self, show_id):
        for row in self.seats.get(show_id, []): 
            print(row)
        print("\n")


hall1 = Hall(5, 5, 1)
hall1.entry_show("1", "Avengers", "10:00")
hall1.entry_show("2", "Joker", "12:00")
hall1.entry_show("3", "Inception", "3:00")
hall2 = Hall(4, 4, 2)
hall2.entry_show("4", "Spider Man", "10:00")
hall2.entry_show("5", "Iron Man", "12:00")
hall2.entry_show("6", "Thor", "3:00")

while True:
    print("\n******Welcome to Star Cinema******\n")
    print("Choose an option:")
    print("1. View all shows")
    print("2. View available seats")
    print("3. Book Seats")
    print("4. Exit")
    print("*************************\n")
    choice = int(input("Enter your choice: \n"))
    if choice == 1:
        for hall in Star_Cinema._Star_Cinema__hall_list:
            hall.view_show_list()
    elif choice == 2:
        show_id = input("Enter the id of the show: ")
        for hall in Star_Cinema._Star_Cinema__hall_list:
            hall.view_available_seats(show_id)
    elif choice == 3:
        show_id = (input("Enter the id of the show: "))
        row = int(input("Enter the row number: "))
        col = int(input("Enter the column number: "))
        seats = [(row, col)]
        for hall in Star_Cinema._Star_Cinema__hall_list:
            hall.book_seats(show_id, seats)
    
    elif choice == 4:
        break
    else:
        print("Invalid choice")
        break
