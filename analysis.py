import csv
from collections import Counter
import matplotlib.pyplot as plt

def clean_and_split_names(names):
    return [name.strip() for name in names.split(',')]

def plot_horizontal_bar_chart(data, title, xlabel, ylabel, color):
    labels, values = zip(*data)
    plt.figure(figsize=(25, 12))
    plt.barh(labels, values, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()

def main():
    all_comment_authors = []

    with open('reddit_technology_posts.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_comment_authors.extend(clean_and_split_names(row['Comment Authors']))

    top_10_authors = Counter(all_comment_authors).most_common(10)

    print("Top 10 Authors with the Most Comments:")
    for i, (author, comments) in enumerate(top_10_authors, 1):
        print(f"{i}. Author: {author}, Comments: {comments}")
    plot_horizontal_bar_chart(top_10_authors, 'Top 10 Authors with the Most Comments','Comments','Authors', 'skyblue')

    top_comment_authors = []
    top_comment_scores = []

    with open('reddit_technology_posts.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            score = int(row['Top Comment Score'])
            author = row['Top Comment Author']
            if author and score:  
                top_comment_authors.append(author)
                top_comment_scores.append(score)

    sorted_comment_data = sorted(zip(top_comment_authors, top_comment_scores), key=lambda x: x[1], reverse=True)

    top_10_comment_data = sorted_comment_data[:10]

    print("\nTop 10 High Scoring Comments and Authors:")
    for i, (author, score) in enumerate(top_10_comment_data, 1):
        print(f"{i}. Author: {author}, Score: {score}")
    plot_horizontal_bar_chart(top_10_comment_data, 'Top 10 High Scoring Comments and Authors','Comment Score', 'Authors','lightgreen')

if __name__ == "__main__":
    main()
