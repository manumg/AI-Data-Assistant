# AI-Data-Assistant
AI Data assistant wiht LangChain, OpenAI and Streamlit that will help you in your EDA process, variable analysis and model selection.

Overview
The AI Data Assistant is an intelligent tool designed to help you thorugh your Exploratory Data Analysis (EDA) processand suggest the best ML algorithms based on your business problem. By leveraging the power of OpenAI and LangChain, the assistant assists you in gaining valuable insights into your data, helping you make informed decisions in your data science projects.

How it Works
Upload CSV File:

Begin your data science journey by uploading a CSV file. The assistant will prompt you to provide the dataset that you want to analyze.
Exploratory Data Analysis:

Once you upload the CSV file, the assistant performs a comprehensive Exploratory Data Analysis, including:
Displaying the first 5 rows of the dataset.
Providing general descriptions of the features, including statistics like mean, standard deviation, min, and max values.
Identifying missing values and duplicates.
Generating a data summarization table for numerical features.
Analyzing correlations between variables.
Identifying outliers and suggesting possible new features.
Variable-Specific Analysis:

The assistant allows you to explore specific variables in-depth. Simply input the variable you are interested in, and the assistant will:
Create visualizations for the chosen variable.
Provide detailed insights such as summary statistics, normality checks, outlier analysis, trends, and missing value assessments.
User Interaction:

The assistant encourages user interaction by asking if there are more variables to explore. If the user is satisfied, the assistant proceeds to inquire about the business problem.
Data Science Problem and ML Algorithms:

Based on the provided business problem, the assistant converts it into a data science problem.
It then suggests a list of the best machine learning algorithms to address the specific data science problem.
Getting Started
To use the AI Data Assistant:

Clone the repository.
Install the required libraries using pip install -r requirements.txt.
Set up your OpenAI API key as specified in the documentation.
Run the Streamlit application using streamlit run your_app_file.py.
