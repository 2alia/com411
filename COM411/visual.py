import matplotlib.pyplot as plt
import csv
from datetime import datetime


class Visual:
    def __init__(self):
        pass

    def reviewed_park(self):
        parks = []
        with open ("disneyland_reviews.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                parks.append(row["Branch"])
            park_counts ={}
            for park in parks:
                if park in park_counts:
                    park_counts[park]+=1
                else:
                    park_counts[park]= 1
            labels = [f"{park} ({count})" for park, count in park_counts.items()]
            plt.pie(list(park_counts.values()), labels = labels)
            plt.title("Review distribution")
            plt.show()

    def averages_score_per_park(self):
        park_data = {}
        with open("disneyland_reviews.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                park = row["Branch"]
                rating = int(row["Rating"])

                if park in park_data:
                    park_data[park]["Count"] += 1
                    park_data[park]["Total"] += rating
                else:
                    park_data[park] = {"Count": 1, "Total": rating}
        print("Park Data", park_data)
        average_rating = {park: park_data[park]["Total"] / park_data[park]["Count"] for park in park_data}
        formatted_averages_rating = {park: round(score,2) for park, score in average_rating.items()}
        print("Average Rating:", formatted_averages_rating)
        plt.bar(average_rating.keys(), average_rating.values())
        plt.xlabel("Park")
        plt.ylabel("Average Review Score")
        plt.title("Average Review Scores Per Park")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def top_10_average_high_scores(self):
        park_name = input("Enter the park name: ")
        branch_scores = {}

        with open("disneyland_reviews.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for entry in csv_reader:
                park = entry["Branch"].split('-')[0]
                if park == park_name:
                    reviewer_loc = entry["Reviewer_Location"]
                    branch = entry["Branch"]
                    review_score = int(entry["Rating"])
                    if reviewer_loc not in branch_scores:
                        branch_scores[reviewer_loc] = {"Total": 0, "Count": 0}

                    branch_scores[reviewer_loc]["Total"] += review_score
                    branch_scores[reviewer_loc]["Count"] += 1

        print("collected Branch scores", branch_scores)

        branch_average_scores = {
                branch: branch_scores[branch]["Total"] / branch_scores[branch]["Count"]
                if branch_scores[branch]["Count"] > 0 else 0
                for branch in branch_scores
        }

        top_10 = sorted(branch_average_scores.items(), key=lambda x: x[1], reverse=True)[:10]
        if top_10:
            plt.figure(figsize=(12, 6))
            top_branches, top_scores = zip(*top_10)

            plt.bar(top_branches, top_scores)
            plt.xlabel("Branch")
            plt.ylabel("Average Review Score")
            plt.title(f"Top 10 Branches with Highest Avg Rating in {park_name} - {branch}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("No branches found")

    def park_average_rating_month(self):
        specify_year = int(input("Enter year: "))
        park_name = input("Enter the park:")
        park_ratings = {month: [] for month in range(1, 13)}

        with open("disneyland_reviews.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for entry in csv_reader:
                review_date = entry["Year_Month"]
                if review_date != 'Missing':
                    try:
                        date = datetime.strptime(review_date, "%Y-%m")
                        if date.year == specify_year:
                            month = date.month
                            park = entry["Branch"].split("-")[0]

                            if park == park_name:
                                rating = int(entry["Rating"])
                                park_ratings[month].append(rating)

                    except ValueError:
                        continue


            average_ratings = {month: sum(ratings) / len(ratings) if ratings else 0 for month, ratings in park_ratings.items()}
            sorted_ratings = sorted(average_ratings.items())

            months = [datetime(specify_year, month,1).strftime("%B %Y")for month, _ in sorted_ratings]
            ratings = [rating for _, rating in sorted_ratings]

            print("Collected Data:")
            for i, rating in enumerate(ratings):
                print(f"{months[i]}, Average Rating: {rating:.2f}")

            plt.figure(figsize=(12, 6))
            plt.bar(months, ratings)
            plt.xlabel("Month")
            plt.ylabel("Average Review")
            plt.title(f"Average Review Scores per {park_name} in {specify_year} by Month")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
