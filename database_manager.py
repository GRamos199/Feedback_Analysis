import sqlite3
import pandas as pd


def store_results(results):
    """
    Stores processed results in a SQLite database.

    Args:
        results (dict): Processed feedback data.
    """
    conn = sqlite3.connect('db/feedback.db')
    cursor = conn.cursor()

    # Create tables if they do not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentiment_counts (
            sentiment TEXT PRIMARY KEY,
            count INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category_counts (
            category TEXT PRIMARY KEY,
            count INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS average_ratings (
            product_id TEXT PRIMARY KEY,
            average_rating REAL
        )
    ''')

    # Insert sentiment counts
    for sentiment, count in results['sentiment_counts'].items():
        cursor.execute('''
            INSERT OR REPLACE INTO sentiment_counts (sentiment, count)
            VALUES (?, ?)
        ''', (sentiment, count))

    # Insert category counts
    for category, count in results['category_counts'].items():
        cursor.execute('''
            INSERT OR REPLACE INTO category_counts (category, count)
            VALUES (?, ?)
        ''', (category, count))

    # Insert average ratings
    for product_id, avg_rating in results['average_ratings'].items():
        cursor.execute('''
            INSERT OR REPLACE INTO average_ratings (product_id, average_rating)
            VALUES (?, ?)
        ''', (product_id, avg_rating))

    conn.commit()
    conn.close()
    print("Results stored in database.")
