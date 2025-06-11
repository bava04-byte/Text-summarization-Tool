import streamlit as st
from transformers import pipeline

# Page settings
st.set_page_config(page_title="Text Summarization Tool", layout="centered")
st.title("📝 Text Summarization Tool")

# Load model only once using cache
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small", tokenizer="t5-small", framework="pt")

summarizer = load_summarizer()

# User input
input_text = st.text_area("Enter the text you want to summarize:", height=300)

# Summary length selection
max_tokens = st.slider("Max summary length (tokens):", 20, 5000, 50)

# Summarize button
if st.button("Generate Summary"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            # T5 requires a prefix
            preprocessed_text = "summarize: " + input_text.strip()
            result = summarizer(preprocessed_text, max_length=max_tokens, min_length=10, do_sample=True)
            summary = result[0]['summary_text']

        st.subheader("📌 Summary")
        st.success(summary)

# Footer
st.markdown("---")
st.caption("Built with Hugging Face Transformers and Streamlit")
