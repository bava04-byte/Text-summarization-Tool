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

## 📦 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/text-summarization-tool.git
cd text-summarization-tool


### Step 2: Install dependencies

pip install -r requirements.txt

Run the App

streamlit run app.py
