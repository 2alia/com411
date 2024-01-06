import csv
from tui import TUI
class Disneyland:
    def __init__(self):
        self.file_path = "disneyland_reviews.csv"
    def line_dashes(self, title, chr):
        dash_line = chr * len(title)
        print(dash_line)
        print(title)
        print(dash_line)

    def number_reviews(self):
        browse_name = input("Which park would you like to analyse: ")
        browse_location = input("Enter the location: ")
        review_count = 0
        file = csv.reader(open("disneyland_reviews.csv"))

        for row in file:
            if browse_name in row and browse_location in row:
                review_count += 1

        print(f"\nThe number of reviews for {browse_name} from {browse_location}: {review_count}\n")

    def run(self):
        title = "Disneyland review Analyser"
        self.line_dashes(title, "-")
        self.number_reviews()
        tui = TUI()
        tui.menu()


if __name__ == "__main__":
    main = Disneyland()
    main.run()