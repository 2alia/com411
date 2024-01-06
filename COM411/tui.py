from process import Process
from visual import Visual


class TUI:
    def __init__(self):
        pass

    def menu(self):
        print("\nEnter the letter from the following options")
        options = {
            "A": "View Data",
            "B": "Visualise Data",
            "X": "Exit"
        }
        while True:
            for key, value in options.items():
                print(f" [{key}] {value}")

            user = input().upper()

            if user in options:
                if user == "X":
                    print(f"You have chosen option {user} - {options[user]}. Exiting program.")
                    break
                elif user == "A":
                    self.submenu_view_a()
                elif user == "B":
                    self.submenu_view_b()
            else:
                print("Please enter a valid choice.")

    def submenu_view_a(self):
        print("\nPlease enter one of the following options:")
        options = {
            "A": "View Reviews by Park",
            "B": "Number of Reviews by park and Reviewer locations",
            "C": "Average Score per year by Park",
            "D": "Average Score per Park by Reviewer Location",
            "X": "Back to Main Menu"
        }
        process = Process()

        while True:
            for key, value in options.items():
                print(f"[{key}] {value}")

            choice = input().upper()
            if choice in options:
                if choice == "X":
                    break
                elif choice == "A":
                    process.review_by_park()
                elif choice == "B":
                    process.number_reviews()
                elif choice == "C":
                    process.average_score_year_parks()
                elif choice == "D":
                    pass
                else:
                    print("Invalid")

    def submenu_view_b(self):
        visual = Visual()
        print("\nPlease enter one of the following options:")
        options_2 = {
            "A": "Most Reviewed Parks",
            "B": "Average Scores",
            "C": "Park Ranking by nationality",
            "D": "Most Popular Month by park",
            "X": "Back to Main Menu"

        }
        while True:
            print("\nPlease enter one of the following options:")
            for key, value in options_2.items():
                print(f"[{key}] {value}")
            choice = input().upper()
            if choice in options_2:
                if choice == "X":
                    break
                elif choice == "A":
                    visual.reviewed_park()
                elif choice == "B":
                    visual.averages_score_per_park()
                elif choice == "C":
                    visual.top_10_average_high_scores()
                elif choice == "D":
                    pass
                else:
                    print("Invalid")