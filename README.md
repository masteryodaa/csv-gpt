# CSV GPT

This is a Streamlit app that uses OpenAI language model to generate text from CSV data.


## How to use

1. Upload a CSV file to the app.
2. Enter a query about your CSV data.
3. The app will generate text that answers your query.


## Requirements

* Streamlit
* OpenAI's API key


## Installation

1. Install Streamlit: ```pip install streamlit```

2. Create a .env file in the root directory of this project and add your OpenAI API key to the file. For example:
OPENAI_API_KEY=YOUR_API_KEY


3. Run the app: ```streamlit run app.py```


## Example

Here is an example of how to use the app:

1. Upload the `products.csv` file to the app.
2. Enter the query `What are the most popular products?`.
3. The app will generate text that answers your query, such as:

The most popular products are:

Product A

Product B

Product C


## License

This project is licensed under the MIT License.