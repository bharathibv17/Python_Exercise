import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
import streamlit as st

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load Excel file
file_path = "C:\\Users\\bhara\\Downloads\\Invoicestatus1.csv"
df = pd.read_csv(file_path)

# Function to preprocess user query
def preprocess_query(query):
    tokens = word_tokenize(query.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens

# Function to extract invoice number from query
def extract_invoice_number(query):
    # This regex assumes invoice numbers are purely numeric. Adjust the pattern if needed.
    match = re.search(r'\b\d+\b', query)
    if match:
        return match.group()
    return None

# Function to answer query
def answer_query(query, df):
    invoice_number = extract_invoice_number(query)

    if invoice_number:
        # Use the correct column name here
        result = df[df['Invoice Number'] == int(invoice_number)]
        if not result.empty:
            return result.to_dict(orient='records')[0]  # Return the first matching record as a dictionary
        else:
            return f"Invoice number {invoice_number} not found."
    else:
        return "Please specify a valid invoice number."

# Streamlit App
import streamlit as st
# Streamlit App
st.set_page_config(page_title="Invoice Query App", page_icon=":file_invoice:", layout="wide")

# Adding a logo and title
st.image("C:\\Users\\bhara\\Downloads\\waterfalls-1908788_960_720.jpg", width=150)  # Replace with your logo URL
st.title("Invoice Query App")
st.write("Enter your query about an invoice:")

# Sidebar with additional information
st.sidebar.header("About")
st.sidebar.write("""
    This app allows you to query invoice information by entering an invoice number. 
    Please make sure to enter a valid invoice number to get accurate results.
""")

# Main section with query input and result
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Invoice Query")
    query = st.text_input("Your Query", placeholder="Enter your invoice query here...", key="main_query")
    if st.button("Submit", key="main_submit"):
        if query:
            answer = answer_query(query, df)
            st.write(answer)
        else:
            st.write("Please enter a query.")

with col2:
    st.subheader("Instructions")
    st.write("""
        - Enter the invoice number in the query field.
        - Click the 'Submit' button to get the invoice details.
    """)

# Footer with contact information
st.markdown("---")
st.write("© 2024 Your Company Name. All rights reserved.")
st.write("For support, contact [support@yourcompany.com](mailto:support@yourcompany.com).")