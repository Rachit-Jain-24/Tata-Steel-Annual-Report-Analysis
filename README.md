Annual Report Analysis Dashboard using Streamlit

This project provides an interactive web application built with Streamlit for performing Natural Language Processing (NLP) analysis on annual reports. The primary example used is the "Tata Steel Annual Report 2023-24," but the application also allows users to upload their own PDF files for analysis.

📋 Features

This dashboard takes a PDF as input and provides a multi-tab interface with the following analyses:

Sentiment Analysis:

Calculates the overall sentiment of the document.

Displays metrics for the number of positive, neutral, and negative sentences.

Visualizes the distribution of sentiment polarity with a histogram.

Word Frequency & Cloud:

Identifies and displays the top 20 most frequent words in the report.

Generates an interactive word cloud for a quick visual summary of key terms.

Topic Modeling:

Uses Latent Dirichlet Allocation (LDA) to discover underlying topics in the document.

Allows the user to interactively select the number of topics to model.

Dual PDF Source:

Option to analyze the pre-loaded "Tata Steel Annual Report".

A file uploader to analyze any other PDF document.

🛠️ Technologies Used

Framework: Streamlit

PDF Processing: PyPDF2

NLP & Text Processing: NLTK, TextBlob, Gensim

Data Manipulation: Pandas

Visualization: Matplotlib, WordCloud

🚀 Setup and Installation

To run this application on your local machine, follow these steps:

Clone the Repository

git clone [https://github.com/Rachit-Jain-24/Tata-Steel-Annual-Report-Analysis.git](https://github.com/Rachit-Jain-24/Tata-Steel-Annual-Report-Analysis.git)
cd Tata-Steel-Annual-Report-Analysis


Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install Dependencies
Install all the required libraries from the requirements.txt file.

pip install -r requirements.txt


Download NLTK Data
The app will automatically download the necessary NLTK models (punkt and stopwords) on the first run if they are not found.

Run the Streamlit App

streamlit run streamlit_app.py


Your web browser will open with the application running.

📖 How to Use

Open the application in your browser.

From the sidebar, choose your PDF source:

"Upload your own PDF": Click the "Browse files" button to select a PDF from your computer.

"Use the default sample report": Simply click the "Analyze Default Report" button. Ensure the Tata Steel Annual Report 2023-24.pdf is in the project's root directory.

Once a file is selected, the analysis will start automatically.

Navigate through the tabs ("Sentiment Analysis", "Word Frequency & Cloud", "Topic Modeling") to view the results.

📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.
