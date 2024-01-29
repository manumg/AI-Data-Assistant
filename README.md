# AI Data Assistant

## Overview
The AI Data Assistant is an intelligent tool designed to help you through your Exploratory Data Analysis (EDA) process and suggest the best ML algorithms based on your business problem. By leveraging the power of OpenAI and LangChain, the assistant helps you in gaining valuable insights into your data, helping you make informed decisions in your data science projects.

## How it Works

1. **Upload CSV File:**
   - Begin your data science journey by uploading a CSV file. The assistant will prompt you to provide the dataset that you want to analyze.

2. **Exploratory Data Analysis:**
   - Once you upload the CSV file, the assistant performs a comprehensive Exploratory Data Analysis, including:
     - Displaying the first 5 rows of the dataset.
     - Providing general descriptions of the features, including statistics like mean, standard deviation, min, and max values.
     - Identifying missing values and duplicates.
     - Generating a data summarization table for numerical features.
     - Analyzing correlations between variables.
     - Identifying outliers and suggesting possible new features.

3. **Variable-Specific Analysis:**
   - The assistant allows you to explore specific variables in-depth. Simply input the variable you are interested in, and the assistant will:
     - Create visualizations for the chosen variable.
     - Provide detailed insights such as summary statistics, normality checks, outlier analysis, trends, and missing value assessments.

4. **User Interaction:**
   - The assistant encourages user interaction by asking if there are more variables to explore. If the user is satisfied, the assistant proceeds to inquire about the business problem.

5. **Data Science Problem and ML Algorithms:**
   - Based on the provided business problem, the assistant converts it into a data science problem.
   - It then suggests a list of the best machine learning algorithms to address the specific data science problem.

## Getting Started

To use the AI Data Assistant:

1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Set up your OpenAI API key as specified in the documentation.
4. Run the Streamlit application using `streamlit run your_app_file.py`.

