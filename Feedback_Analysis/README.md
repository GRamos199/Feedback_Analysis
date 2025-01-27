# Feedback Analysis Project

## Overview

This project processes customer feedback from a CSV file, performs analysis, stores the results in a database, and generates visualizations for insights. It is containerized with Docker for easy setup and deployment.

## Features

- **Average Ratings by Product**: Displays average ratings for each product.
- **Feedback Distribution by Category**: Shows the number of feedback entries per category.
- **Sentiment Analysis**: Provides a simple analysis of feedback text.
- **Data Filtering**: Allows filtering by category, product, or date range.
- **Database Storage**: Saves processed results in a SQLite database.
- **Visualizations**: Generates charts for insights.

---

## Project Structure

```
project/
|-- data/                # Input CSV files (e.g., feedback.csv)
|-- db/                  # SQLite database file (e.g., feedback.db)
|-- output/              # Generated visualizations (e.g., PNG charts)
|-- main.py              # Main entry point for the application
|-- data_loader.py       # Loads and validates CSV data
|-- data_processor.py    # Processes and analyzes feedback
|-- database_manager.py  # Handles database storage
|-- visualization.py     # Generates visualizations
|-- Dockerfile           # Docker container configuration
|-- docker-compose.yml   # Docker Compose configuration
|-- requirements.txt     # Python dependencies
```

---

## Requirements

### Python Environment (Optional, Outside Docker)

- Python 3.9 or later
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Docker

- Docker Engine installed on your system.
- Docker Compose (optional).

---

## Running the Project

### Using Docker

#### 1. Build the Docker Image

Run this command in the terminal from the project directory:

```bash
docker build -t feedback_analysis .
```

#### 2. Run the Container

```bash
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/output:/app/output -v $(pwd)/db:/app/db feedback_analysis
```

- **`-v` flags**: Mount local folders into the container to persist data outside the container.
- Processed data will be saved in:
  - `db/feedback.db`
  - `output/` (charts).

#### 3. Stop the Container

To stop, press `Ctrl+C` in the terminal.

### Using Docker Compose

#### 1. Run the Application

```bash
docker-compose up --build
```

This will:

- Build the image (if not already built).
- Start the container and run the program.

#### 2. Stop the Application

```bash
docker-compose down
```

---

## Results

- **Database**:

  - Located in `db/feedback.db`.
  - Stores:
    - Sentiment counts.
    - Feedback category distribution.
    - Average ratings by product.

- **Visualizations**:
  - Charts saved in `output/` folder:
    - `sentiment_distribution.png`: Pie chart of sentiment analysis.
    - `category_distribution.png`: Pie chart of category distribution.
    - `average_ratings_by_product.png`: Bar chart of average ratings.

---

## Development Notes

### Filtering Example

You can filter feedback data in `main.py` using the `filter_feedback` function:

```python
filtered_data = filter_feedback(feedback_data, category="Customer Support", start_date="2024-01-01")
print(filtered_data.head())
```

### Tests

Run `tests.py` (if implemented) to validate functionality.

---

## Future Enhancements

- Use advanced sentiment analysis models (e.g., HuggingFace transformers).
- Add a web interface for dashboard visualization.
- Automate feedback ingestion from external sources.

---
