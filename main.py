import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
from tempfile import NamedTemporaryFile


def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("Please set your OpenAI API key in a .env file in the root directory of this project.")
        return
    else:
        print("OpenAI API key found!")

    st.set_page_config(page_title="CSV GPT", page_icon="📈")
    st.title("CSV GPT 📈")
    user_csv = st.file_uploader("Upload a CSV file", type="csv")

    if user_csv is not None:

        with NamedTemporaryFile(delete=False, suffix=".csv") as f:
            f.write(user_csv.getvalue())
            user_query = st.text_input("What do you wanna know about your CSV data?", placeholder="Enter your query here...")

            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, f.name, verbose=True)

            if user_query != "" and user_query is not None:
                st.write(f"Q: {user_query}")

                response = agent.run(user_query)
                st.write(f"A: {response}")




if __name__ == "__main__":
    main()