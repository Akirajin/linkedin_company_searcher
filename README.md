## README.md

**Application:** Searcher

**Language:** Python 3.10

**Dependencies:**

* Poetry
* Docker (optional)

**Description:**

This application searches for company websites using Google Search and stores the results in a file.

**Installation:**

1. Clone the repository to your local machine.

**Running:**

**With Docker (recommended):**

1. Open a terminal and navigate to the project root directory.
2. Run the following command:

```
docker build -t searcher . && docker run searcher
```

**Without Docker:**

1. Install Poetry: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
2. Install Python 3.10: [https://www.python.org/downloads/](https://www.python.org/downloads/)
3. Open a terminal and navigate to the project root directory.
4. Run the following command:

```
poetry run python src/app.py
```

**Input:**

Place your companies name list in one or more CSV files in the `input` folder.

**Output:**

The application will print the search results to the console and save them as a file named `output` in the `output` folder. The file will contain pairs of company names and their corresponding website links.

**Future Enhancements:**

* Use a faster language like Rust, Java, or Go for better performance.
* Implement more robust error checking and handling.

**Contribution:**

Feel free to contribute to this project by creating pull requests on GitHub.
