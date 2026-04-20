# Railway Reservation System

# Total seats
TOTAL_SEATS = 50

# Store bookings
seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}

# Generate booking ID
booking_id_counter = 1


def check_availability():
    print("\nAvailable Seats:", len(seats))


def book_ticket():
    global booking_id_counter

    if len(seats) == 0:
        print("No seats available!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")

    seat_number = seats.pop(0)

    booking_id = "B" + str(booking_id_counter)
    booking_id_counter += 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_number)


def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        ticket = bookings[booking_id]

        print("\nTicket Details")
        print("Name:", ticket["name"])
        print("Age:", ticket["age"])
        print("Seat:", ticket["seat"])

    else:
        print("Booking ID not found!")


def cancel_ticket():
    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        seat_number = bookings[booking_id]["seat"]

        seats.append(seat_number)
        seats.sort()

        del bookings[booking_id]

        print("Ticket Cancelled Successfully!")

    else:
        print("Booking ID not found!")


while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_availability()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_ticket()

    elif choice == "4":
        cancel_ticket()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
