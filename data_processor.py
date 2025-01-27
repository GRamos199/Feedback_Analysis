import pandas as pd
from collections import Counter
from textblob import TextBlob  # Added for simple sentiment analysis


def classify_rating(rating):
    """
    Classifies rating into categories: positive, neutral, or negative.

    Args:
        rating (int): Customer rating.

    Returns:
        str: Classification label.
    """
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"


def sentiment_analysis(text):
    """
    Perform simple sentiment analysis using TextBlob.

    Args:
        text (str): Feedback text.

    Returns:
        str: Sentiment label (positive, neutral, negative).
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


def process_feedback(data):
    """
    Processes feedback data and generates metrics.

    Args:
        data (pd.DataFrame): Raw feedback data.

    Returns:
        dict: Processed results.
    """
    # Classify ratings
    data['sentiment_rating'] = data['rating'].apply(classify_rating)

    # Perform sentiment analysis on text
    data['sentiment_text'] = data['feedback_text'].apply(sentiment_analysis)

    # Sentiment distribution
    sentiment_counts = data['sentiment_text'].value_counts().to_dict()

    # Category distribution
    category_counts = data['category'].value_counts().to_dict()

    # Average ratings by product
    average_ratings = data.groupby('product_id')['rating'].mean().sort_values(ascending=False)

    # Keyword extraction (simple example)
    all_words = ' '.join(data['feedback_text']).lower().split()
    common_words = Counter(all_words).most_common(10)

    return {
        "sentiment_counts": sentiment_counts,
        "category_counts": category_counts,
        "average_ratings": average_ratings,
        "common_words": common_words,
        "filtered_data": data  # Full processed data for filtering
    }


def filter_feedback(data, category=None, start_date=None, end_date=None, product_id=None):
    """
    Filters feedback data based on given criteria.

    Args:
        data (pd.DataFrame): Feedback data.
        category (str): Feedback category to filter.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.
        product_id (str): Product ID to filter.

    Returns:
        pd.DataFrame: Filtered feedback data.
    """
    if category:
        data = data[data['category'] == category]

    if start_date:
        data = data[data['timestamp'] >= start_date]

    if end_date:
        data = data[data['timestamp'] <= end_date]

    if product_id:
        data = data[data['product_id'] == product_id]

    return data
