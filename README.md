# 📝 Text Summarization Tool

This is a simple and interactive web application that allows users to generate summaries of long text passages using a pretrained T5 model. The app is built using **Streamlit** and **Hugging Face Transformers**.

---

## 📖 Project Description

The **Text Summarization Tool** is a lightweight web application that allows users to automatically summarize long pieces of text using a Transformer-based model. Built with **Streamlit** for the user interface and **Hugging Face Transformers** for natural language processing, the app utilizes the `t5-small` model for generating concise summaries.

### 🔍 How It Works

- When a user enters a block of text into the input field, the app prepends it with the prefix `"summarize:"` — this is required by the T5 model.
- The `t5-small` model then processes the input and generates a summary based on the specified maximum token length (controlled by the slider).
- The result is displayed interactively in the app.

### 🔧 Code Components

- `streamlit` is used to build the web interface.
- `transformers.pipeline()` loads the `t5-small` summarization pipeline.
- The model is loaded only once using `@st.cache_resource` for faster performance.
- Users input text via `st.text_area`, select max summary length with `st.slider`, and trigger summarization using a button.
- The app handles empty inputs gracefully with a warning and shows a spinner while generating the summary.

---

## 🚀 Features

- Summarizes long text using the `t5-small` model
- Adjustable maximum summary length (in tokens)
- Interactive and user-friendly interface built with Streamlit
- Displays summarized output instantly

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)


##🧾 Code Explanation

The main application logic is written in app.py using Streamlit and Hugging Face Transformers. Below is a breakdown of the core components:

1. Import Required Libraries

import streamlit as st
from transformers import pipeline
streamlit is used to create the web-based user interface.

pipeline is a Hugging Face utility that allows easy access to pretrained models for tasks like summarization.

2. Configure Streamlit Page

st.set_page_config(page_title="Text Summarization Tool", layout="centered")
st.title("📝 Text Summarization Tool")
Sets the title and layout of the Streamlit web app.

3. Load the Summarization Model (T5-small)

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small", tokenizer="t5-small", framework="pt")

summarizer = load_summarizer()
Loads the T5 model and tokenizer once and caches them using @st.cache_resource for better performance.

Uses the "summarization" pipeline with the t5-small model.

4. User Input Section

input_text = st.text_area("Enter the text you want to summarize:", height=300)
Provides a large text area for the user to input the article or paragraph they want to summarize.

5. Set Maximum Summary Length

max_tokens = st.slider("Max summary length (tokens):", 20, 5000, 50)
Allows the user to select the desired maximum length of the summary using a slider.

6. Generate Summary Button

if st.button("Generate Summary"):
Renders a button that, when clicked, triggers the summarization process.

7. Summarization Logic

if not input_text.strip():
    st.warning("⚠️ Please enter some text.")
else:
    with st.spinner("Generating summary..."):
        preprocessed_text = "summarize: " + input_text.strip()
        result = summarizer(preprocessed_text, max_length=max_tokens, min_length=10, do_sample=True)
        summary = result[0]['summary_text']

    st.subheader("📌 Summary")
    st.success(summary)
If the input is empty, a warning is shown.

Otherwise, the text is prefixed with "summarize:" (required by T5).

The summarizer pipeline generates the summary.

The result is displayed under a "Summary" header.

8. Footer

st.markdown("---")
st.caption("Built with Hugging Face Transformers and Streamlit")
Adds a visual separator and a caption crediting the tools used.

## 📦 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/text-summarization-tool.git
cd text-summarization-tool


### Step 2: Install dependencies

pip install -r requirements.txt

Run the App
