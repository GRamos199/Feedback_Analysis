from data_loader import load_csv
from data_processor import process_feedback, filter_feedback
from database_manager import store_results
from visualization import (
    plot_average_ratings, 
    plot_category_distribution, 
    plot_sentiment_distribution
)


def main():
    # Step 1: Load feedback data
    feedback_data = load_csv('data/feedback.csv')

    # Step 2: Process feedback
    results = process_feedback(feedback_data)

    # Step 3: Store results in database
    store_results(results)

    # Step 4: Generate visualizations
    plot_average_ratings(results['average_ratings'])
    plot_category_distribution(results['category_counts'])
    plot_sentiment_distribution(results['sentiment_counts'])

    # Example filtering (optional)
    filtered_data = filter_feedback(feedback_data, category="Customer Support")
    print(f"Filtered Data: \n{filtered_data.head()}")

    print("Process complete! Results stored and dashboard generated.")


if __name__ == "__main__":
    main()
