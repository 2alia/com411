import csv

class Process:
    def __init__(self):
        pass


    def review_by_park(self,):
        search =  input("which park would your like to review ")
        file = csv.reader(open("disneyland_reviews.csv"))
        review_count = 0
        for row in file:
            if search in row:
                print(row)
                review_count += 1
        print(f"\nNumber of reviews for {search} is: {review_count}\n")

    def number_reviews(self):
        browse_name = input("Which park would you like to analyse: ")
        browse_location = input("Enter the location: ")
        review_count = 0
        file = csv.reader(open("disneyland_reviews.csv"))

        for row in file:
            if browse_name in row and browse_location in row:
                review_count += 1

        print(f"\nThe number of reviews for {browse_name} from {browse_location}: {review_count}\n")



    def average_score_year_parks(self):
        browse_name = input("Enter the name of the park: ")
        browse_year = input("Enter the year: ")
        review_count = 0
        total_count = 0
        file = csv.reader(open("disneyland_reviews.csv"))

        for row in file:
            if browse_name in row and browse_year in row[2]:
                total_count += int(row[1])
                review_count += 1
        if review_count != 0:
            average_rating = total_count / review_count
            print(f"\nThe average rating for {browse_name} in {browse_year} is: {average_rating:.2f}\n")
        else:
            print(f"\nNo reviews for {browse_name} in {browse_year}\n")