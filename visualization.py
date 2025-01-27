import matplotlib.pyplot as plt


def plot_average_ratings(average_ratings):
    """
    Generates a bar chart for average ratings by product.

    Args:
        average_ratings (pd.Series): Average ratings indexed by product ID.
    """
    plt.figure(figsize=(12, 6))
    average_ratings.plot(kind='bar', color='skyblue')
    plt.title('Average Ratings by Product', fontsize=16)
    plt.xlabel('Product ID', fontsize=12)
    plt.ylabel('Average Rating', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/average_ratings_by_product.png')
    plt.close()
    print("Average ratings chart saved as 'output/average_ratings_by_product.png'")


def plot_category_distribution(category_counts):
    """
    Generates a pie chart for feedback distribution by category.

    Args:
        category_counts (dict): Counts of feedback per category.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Feedback Distribution by Category', fontsize=16)
    plt.tight_layout()
    plt.savefig('output/category_distribution.png')
    plt.close()
    print("Category distribution chart saved as 'output/category_distribution.png'")


def plot_sentiment_distribution(sentiment_counts):
    """
    Generates a pie chart for sentiment distribution.

    Args:
        sentiment_counts (dict): Counts of feedback per sentiment category.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Sentiment Analysis Results', fontsize=16)
    plt.tight_layout()
    plt.savefig('output/sentiment_distribution.png')
    plt.close()
    print("Sentiment distribution chart saved as 'output/sentiment_distribution.png'")
