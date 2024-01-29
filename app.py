#Import required libraries
import os 


import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.utilities import WikipediaAPIWrapper

#OpenAIKey

os.environ['OPENAI_API_KEY'] = "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" 
load_dotenv(find_dotenv())

#Title
st.title('AI Assistant for Data Science 🤖')

#Welcoming message
st.write("Hello, 👋 I am your AI Assistant and I am here to help you with your data science projects.")

#Explanation sidebar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV File.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset.
    That's why I'd love for you to upload a CSV file.
    Once we have your data in hand, we'll dive into understanding it and have some fun exploring it.
    Then, we'll work together to shape your business challenge into a data science framework.
    I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem. Sounds fun right?**
    ''')


#Initialise the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked ={1:False}

#Function to udpate the value in session state
def clicked(button):
    st.session_state.clicked[button]= True
st.button("Let's get started", on_click = clicked, args=[1])
if st.session_state.clicked[1]:
    user_csv = st.file_uploader("Upload your file here", type="csv")
    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

        #llm model
        llm = OpenAI(temperature = 0)

        #Function sidebar
        @st.cache_data
        def steps_eda():
            steps_eda = llm('What are the steps of EDA')
            return steps_eda

        #Pandas agent
        pandas_agent = create_pandas_dataframe_agent(llm, df, verbose = True)

        #Functions main
        @st.cache_data
        def function_agent():
            st.write("**Data Overview**")
            st.write("The first rows of your dataset look like this:")
            st.write(df.head())
            st.write("**Data Cleaning**")
            columns_df = pandas_agent.run("What are the meaning of the columns?")
            st.write(columns_df)
            missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
            st.write(missing_values)
            duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
            st.write(duplicates)
            st.write("**Data Summarisation**")
            st.write(df.describe())
            correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships.")
            st.write(correlation_analysis)
            outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.")
            st.write(outliers)
            new_features = pandas_agent.run("What new features would be interesting to create?.")
            st.write(new_features)
            return

        @st.cache_data
        def function_question_variable():
            st.line_chart(df, y =[user_question_variable])
            summary_statistics = pandas_agent.run(f"Give me a summary of the statistics of {user_question_variable}")
            st.write(summary_statistics)
            normality = pandas_agent.run(f"Check for normality or specific distribution shapes of {user_question_variable}")
            st.write(normality)
            outliers = pandas_agent.run(f"Assess the presence of outliers of {user_question_variable}")
            st.write(outliers)
            trends = pandas_agent.run(f"Analyse trends, seasonality, and cyclic patterns of {user_question_variable}")
            st.write(trends)
            missing_values = pandas_agent.run(f"Determine the extent of missing values of {user_question_variable}")
            st.write(missing_values)
            return
        
        @st.cache_data
        def function_question_dataframe():
            dataframe_info = pandas_agent.run(user_question_dataframe)
            st.write(dataframe_info)
            return
        
        @st.cache_resource
        def wiki(prompt):
            wiki_research = WikipediaAPIWrapper().run(prompt)
            return wiki_research
        
        @st.cache_data
        def prompt_templates():
            data_problem_template = PromptTemplate(
                input_variables=['business_problem'],
                template='Convert the following business problem into a data science problem: {business_problem}.'
                )

            model_selection_template = PromptTemplate(
                input_variables=['data_problem'],
                template='Give a list of machine learning algorithms that are suitable to solve this problem: {data_problem},while using this wikipedia research: {wikipedia_research}. '
                )
            return data_problem_template, model_selection_template
        
        @st.cache_data
        def chains():
            data_problem_chain = LLMChain(llm=llm, prompt= prompt_templates()[0], verbose= True, output_key = 'data_problem')
            model_selection_chain = LLMChain(llm=llm, prompt= prompt_templates()[1], verbose= True, output_key = 'model_selection')
            sequential_chain = SequentialChain(chains=[data_problem_chain, model_selection_chain], input_variables=['business_problem', 'wikipedia_research'], output_variables=['data_problem', 'model_selection'], verbose=True)
            return sequential_chain
        
        @st.cache_data
        def chains_output(prompt, wiki_research):
            my_chain = chains()
            my_chain_output = my_chain({'business_problem': prompt, 'wikipedia_research': wiki_research})
            my_data_problem = my_chain_output["data_problem"]
            my_model_selection = my_chain_output["model_selection"]
            return my_data_problem, my_model_selection
        
        #Main

        st.header('Exploratory data analysis')
        st.subheader('General information about the dataset')

        with st.sidebar:
            with st.expander('What are the steps of EDA'):
                st.write(steps_eda())

        function_agent()

        st.subheader('Variable of study')
        user_question_variable = st.text_input('What variable are you interested in')
        if user_question_variable is not None and user_question_variable !="":
            function_question_variable()

            st.subheader('Further study')

        if user_question_variable:
            user_question_dataframe = st.text_input( "Is there anything else you would like to know about your dataframe?")
            if user_question_dataframe is not None and user_question_dataframe not in ("","no","No"):
                function_question_dataframe()
            if user_question_dataframe in ("no", "No"):
                st.write("")

                if user_question_dataframe:
                    st.divider()
                    st.header("Data Science Problem")
                    st.write("Now that we have a solid grasp of the data at hand and a clear understanding of the variable we intend to investigate, it's important that we reframe our business problem into a data science problem.")

                    prompt = st.text_area("What is the business problem you would like to solve?")

                    if prompt:
                        wiki_research = wiki(prompt)
                        my_data_problem = chains_output(prompt, wiki_research)[0]
                        my_model_selection = chains_output(prompt, wiki_research)[1]
                        
                        st.write(my_data_problem)
                        st.write(my_model_selection)
