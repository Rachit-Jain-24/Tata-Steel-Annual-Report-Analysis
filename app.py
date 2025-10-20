import streamlit as st
import pandas as pd
import PyPDF2
import re
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from wordcloud import WordCloud
import gensim
from gensim import corpora
import io


# --- Page Configuration ---
st.set_page_config(
    page_title="PDF Analysis Dashboard",
    page_icon="📄",
    layout="wide",
)

# --- NLTK Data Download ---
with st.spinner("Checking/Downloading NLTK data (punkt, stopwords)..."):
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

# --- Caching Functions for Performance ---

@st.cache_data
def extract_text_from_pdf(pdf_file_bytes):
    """Extracts text from a PDF file's bytes."""
    pdf_text = []
    try:
        # Create a file-like object from the bytes
        pdf_file_obj = io.BytesIO(pdf_file_bytes)
        reader = PyPDF2.PdfReader(pdf_file_obj)
        for page in reader.pages:
            text = page.extract_text()
            if text: # Ensure text was extracted
                pdf_text.append(text)
        return "\n".join(pdf_text)
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

@st.cache_data
def preprocess_text(text):
    """Cleans and preprocesses the text data."""
    if not text:
        return "", []
    
    stop_words = set(stopwords.words('english'))
    
    # Preprocessing steps from the notebook
    processed_text = text.lower()
    processed_text = re.sub(r'[^\w\s]', '', processed_text)
    processed_text = re.sub(r'\d+', '', processed_text)
    processed_text = re.sub(r'\s+', ' ', processed_text).strip()
    
    # Tokenize and remove stopwords
    tokens = word_tokenize(processed_text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(filtered_tokens), filtered_tokens

@st.cache_resource
def perform_topic_modeling(_tokens_list, num_topics):
    """Performs LDA Topic Modeling."""
    try:
        dictionary = corpora.Dictionary([_tokens_list])
        corpus = [dictionary.doc2bow(_tokens_list)]
        
        lda_model = gensim.models.LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=num_topics,
            random_state=100,
            passes=10
        )
        return lda_model.print_topics(num_words=10)
    except Exception as e:
        st.error(f"An error occurred during topic modeling: {e}")
        return []

# --- Main Analysis Function ---
def run_analysis(pdf_bytes, file_name):
    """Extracts text and runs all analyses, displaying results in tabs."""
    
    # --- Data Loading and Preprocessing ---
    with st.spinner('Extracting text from PDF...'):
        original_text = extract_text_from_pdf(pdf_bytes)
    
    if original_text:
        with st.spinner('Preprocessing text data...'):
            processed_text, tokens = preprocess_text(original_text)

        st.success(f"Analysis of '{file_name}' is complete.")
        st.divider()

        # --- Analysis Tabs ---
        tab1, tab2, tab3 = st.tabs(["Sentiment Analysis", "Word Frequency & Cloud", "Topic Modeling"])

        # --- Sentiment Analysis Tab ---
        with tab1:
            st.header("Sentiment Analysis")
            with st.spinner("Analyzing sentiment..."):
                sentences = sent_tokenize(original_text)
                sentiment_data = [{'polarity': TextBlob(s).sentiment.polarity} for s in sentences]
                sentiment_df = pd.DataFrame(sentiment_data)

                positive = sentiment_df[sentiment_df['polarity'] > 0.05].shape[0]
                neutral = sentiment_df[(sentiment_df['polarity'] >= -0.05) & (sentiment_df['polarity'] <= 0.05)].shape[0]
                negative = sentiment_df[sentiment_df['polarity'] < -0.05].shape[0]
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Positive Sentences", f"{positive}", "😊")
                col2.metric("Neutral Sentences", f"{neutral}", "😐")
                col3.metric("Negative Sentences", f"{negative}", "😞")

                st.subheader("Distribution of Sentiment Polarity")
                fig, ax = plt.subplots()
                sentiment_df['polarity'].hist(bins=50, ax=ax, color='skyblue', edgecolor='black')
                ax.set_title('Distribution of Sentiment Polarity')
                ax.set_xlabel('Polarity')
                ax.set_ylabel('Number of Sentences')
                st.pyplot(fig)
        
        # --- Word Frequency & Word Cloud Tab ---
        with tab2:
            st.header("Word Frequency and Word Cloud")
            with st.spinner("Generating word cloud and frequencies..."):
                word_freq = Counter(tokens)
                top_words = word_freq.most_common(20)
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.subheader("Top 20 Frequent Words")
                    st.dataframe(pd.DataFrame(top_words, columns=['Word', 'Frequency']), use_container_width=True)

                with col2:
                    st.subheader("Word Cloud")
                    try:
                        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(processed_text)
                        fig, ax = plt.subplots()
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.axis('off')
                        st.pyplot(fig)
                    except ValueError:
                        st.warning("Could not generate word cloud. The document might be too short.")

        # --- Topic Modeling Tab ---
        with tab3:
            st.header("Topic Modeling (LDA)")
            num_topics = st.slider("Select the number of topics:", 2, 15, 10, 1)
            
            with st.spinner(f"Building LDA model for {num_topics} topics..."):
                topics = perform_topic_modeling(tokens, num_topics)
                if topics:
                    st.subheader("Discovered Topics")
                    for topic_num, topic_words in topics:
                        st.markdown(f"**Topic #{topic_num+1}:**")
                        st.info(topic_words)
                else:
                    st.warning("Could not perform topic modeling.")
    else:
        st.warning("No text could be extracted from the PDF file.")

# --- UI Layout ---

title_placeholder = st.empty()
st.sidebar.title("Configuration")

source_option = st.sidebar.radio(
    "Choose PDF Source",
    ["Upload your own PDF", "Use the default sample report"]
)

pdf_bytes = None
file_name = ""

if source_option == "Upload your own PDF":
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        pdf_bytes = uploaded_file.getvalue()
        file_name = uploaded_file.name

elif source_option == "Use the default sample report":
    st.markdown("Click the button below to analyze the **'Tata Steel Annual Report 2024-25.pdf'**.")
    st.info("Ensure the default PDF is in the same directory as the app for this option to work.")
    PDF_PATH = "Tata Steel Annual Report 2024-25.pdf"
    
    if st.button("Analyze Default Report"):
        try:
            with open(PDF_PATH, "rb") as f:
                pdf_bytes = f.read()
            file_name = PDF_PATH
        except FileNotFoundError:
            st.error(f"Error: The file '{PDF_PATH}' was not found.")
            st.stop()

# --- Run Analysis if a file is ready ---
if pdf_bytes and file_name:
    base_name = file_name.rsplit('.', 1)[0]
    title_placeholder.title(f"📄 Annual Report Analysis: {base_name}")
    run_analysis(pdf_bytes, file_name)
else:
    title_placeholder.title("📄 Annual Report Analysis")
    st.info("Please select a PDF source from the sidebar to begin the analysis.")

