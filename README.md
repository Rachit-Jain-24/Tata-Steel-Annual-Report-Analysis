Here’s your **GitHub-ready README.md** version — properly formatted with Markdown, emojis, and sections for readability and professionalism 👇

---

# 📊 Annual Report Analysis Dashboard using Streamlit

An **interactive NLP-powered dashboard** built with **Streamlit** for analyzing **annual reports** through sentiment analysis, topic modeling, and word frequency insights.
The sample report used is the **“Tata Steel Annual Report 2023–24”**, but you can upload and analyze **any PDF document**.

---

## ✨ Features

### 🧠 **Sentiment Analysis**

* Calculates the **overall sentiment** of the document.
* Displays the **number of positive, neutral, and negative sentences**.
* Visualizes **sentiment polarity** distribution using a histogram.

### 🔤 **Word Frequency & Cloud**

* Extracts and displays the **top 20 most frequent words**.
* Generates an **interactive word cloud** to highlight key terms.

### 📚 **Topic Modeling**

* Uses **Latent Dirichlet Allocation (LDA)** to uncover hidden topics in the report.
* Allows users to **adjust the number of topics** interactively.

### 📂 **Dual PDF Source**

* Option 1: Analyze the **default Tata Steel Annual Report (2023–24)**.
* Option 2: **Upload your own PDF** for instant analysis.

---

## 🛠️ Technologies Used

| Category                | Tools / Libraries      |
| ----------------------- | ---------------------- |
| **Framework**           | Streamlit              |
| **PDF Processing**      | PyPDF2                 |
| **NLP & Text Analysis** | NLTK, TextBlob, Gensim |
| **Data Handling**       | Pandas                 |
| **Visualization**       | Matplotlib, WordCloud  |

---

## 🚀 Setup and Installation

Follow the steps below to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rachit-Jain-24/Tata-Steel-Annual-Report-Analysis.git
cd Tata-Steel-Annual-Report-Analysis
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Activate environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK Data

The app will automatically download required NLTK models (`punkt`, `stopwords`) during the first run if they’re missing.

### 5️⃣ Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

Your browser will automatically open the dashboard at **[http://localhost:8501](http://localhost:8501)**.

---

## 📖 How to Use

1. Launch the application in your browser.
2. From the sidebar:

   * **Upload your own PDF:** Click “Browse files” to choose a file.
   * **Use the default sample report:** Click “Analyze Default Report”.
3. The analysis will start automatically once a PDF is selected.
4. Explore the results across the tabs:

   * 📈 *Sentiment Analysis*
   * 🧾 *Word Frequency & Cloud*
   * 🗂️ *Topic Modeling*

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more details.

---

## 👨‍💻 Author

**Rachit Jain**
🔗 [GitHub Profile](https://github.com/Rachit-Jain-24)

---

Would you like me to add **badges** (for Python, Streamlit, license, etc.) and a **preview image section** at the top to make it more visually appealing for GitHub?
