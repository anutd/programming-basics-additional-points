# programming-basics-additional-points

HONOR PLEDGE 
I, Anna Dudenko, fully aknowledge the consequences of academic misconduct.

During my work, I:

1. Did not receive any help
2. Consulted following materials: https://en.wikipedia.org/wiki/Markov_chain (for 3b1b1a)

# 3b1b1a: Simple Text Generation Task

During this task you will be coding a fun little task from my field, natural language processing. You will be implementing a simple traditional model called Markov chain model for the task of text generation.

Task description:

- Choose a book that you like (Keep it under 3mb)
  * Download the book in .txt format
- Create a python file. In it:
  * Open the book file
  * (optional) Clean the text file, e. g. lowercase everything etc.
  * Split the text into a list of its tokens (i. e. words and punctuation). You may use native python methods or consult other libraries
  * Create a dictionary object, where:
    - The keys are the unique tokens
    - The values are lists of the next following words that occur after the key token (1 next word for every occurrence)
  * Generate text. Make it so that:
    - The program chooses the first word randomly from the keys and prints it (you can use random library for this)
    - Then it consults the occurrence list from the dictionary you created to randomly choose the next word to print out (you can use random library for this)
    - Repeat 5.2 200 times

# 3b1b1c: File editing task

Task description:
You have been provided with a text file containing a list of student names along with their test scores. Your task is to read this file, perform some operations on the data, and write the results to a new file. create a students.txt file. In it write:


##
    Alice 85
    Bob 90
    Charlie 75
    David 80
    Emily 92
    Frank 88
    Grace 70
    Henry 85
    Ivy 78
    Jack 95


- File Reading:
  * Open the provided text file in read mode.
  * Read the contents of the file and store them in an appropriate data structure.
- Data Processing:
  * Split each line of the file into student name and test score.
  * Calculate the average score for each student.
- File Writing:
  * Open a new text file in write mode to store the results.
  *Write the student names along with their average scores to the new file. Calculate additional statistics such as the highest and lowest scores, the overall class average, mode, etc.. Write these results to the output file as well.


# 3b1b1b: Data Analysis Using Pandas Task

This time we will be working with a .csv dataset. You are free to consult pandas docs, stackoverflow for your questions.

Task description:
Download the csv file here: https://www.kaggle.com/datasets/lovishbansal123/sales-of-a-supermarket

- Data loading:
  * Load the provided dataset into a Pandas DataFrame. inspect the first few rows of the DataFrame to understand its structure.
- Data cleaning:
  * Check for any missing values in the dataset and handle them appropriately (e.g., by dropping rows or filling missing values). Convert any relevant columns to appropriate data types (e.g., dates, numerical values).
- Data exploration:
  * Calculate summary statistics for numerical columns such as total sales, average sales per month, maximum and minimum sales, etc. Explore categorical columns such as product categories, sales regions, etc., by counting unique values and visualizing distributions.
- Performance analysis:
  * Calculate additional metrics such as profit margins, sales growth rates, and sales contributions by product category or region. Identify top-performing products or regions based on sales volume or revenue.
- Hypothesis testing (optional):
  * Formulate hypotheses about factors that may influence sales (e.g., promotional campaigns, seasonal effects) and perform statistical tests to validate or refute them.
