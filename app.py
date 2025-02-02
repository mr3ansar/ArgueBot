import nltk
nltk.download("stopwords")
nltk.download('punkt_tab')
nltk.download("punkt")
import streamlit as st
from search import search_web, filter_results
from scrape import extract_content
from generate import generate_response

# Streamlit app
st.title("AI Assistant")
query = st.text_input("Enter your query:")

if query:
    # Step 1: Search the web
    st.write("Searching the web...")
    results = search_web(query)
    if not results:
        st.error("Failed to fetch results. Please try again.")
    else:
        # Step 2: Filter results
        filtered_results = filter_results(results)
        if not filtered_results:
            st.warning("No reliable sources found.")
        else:
            # Step 3: Extract and summarize content
            st.write("Extracting content from reliable sources...")
            url = filtered_results[0]["link"]
            content = extract_content(url)
            if content:
                # Step 4: Generate response with context
                st.write("Generating response...")
                response = generate_response(query, content, url)
                st.write("**Generated Response:**")
                st.write(response)

                # Step 5: Allow user to rephrase
                if st.button("Rephrase Response"):
                    new_response = st.text_input("Enter your rephrased response:")
                    if new_response:
                        st.write("**Final Response:**")
                        st.write(new_response)
            else:
                st.error("Failed to extract content from the source.")