import matplotlib.pyplot as plt
import csv
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
        park_scores = {}
        with open("disneyland_reviews.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for entry in csv_reader:
                park = entry["Branch"]
                review_score = int(entry["Rating"])

            if park in park_scores:
                park_scores[park]["Total"] += review_score
                park_scores[park]["Count"] += 1
            else:
                park_scores[park] = {"Total": review_score, "Count": 1}

        average_scores = {park: scores["Total"] / scores["Count"] for park, scores in park_scores.items()}

        parks = list(average_scores.keys())
        scores = list(average_scores.values())
        plt.bar(parks, scores)
        plt.xlabel("Park")
        plt.ylabel("Average Review Score")
        plt.title("Average Review Scores Per Park")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return average_scores



visual = Visual()
visual.reviewed_park()
visual.averages_score_per_park()


