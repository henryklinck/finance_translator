# Finance Transalator

## UofTHacks X

## Inspiration
Our group was immediately intrigued by the The Advice Company Challenge: "Most Innovative Use of AI for Personal Finance". We wanted to build a project that helps people explore the subject of Finance as well as their own Personal Finance. 

When we began discussing the topic, we all agreed that the **heavy use of technical terminology and jargon amongst Finance professionals acts as a barrier to inexperienced individuals** who wish to become more involved in their Personal Finance. 

The film, "The Big Short", defines the problem well when one of the characters states: "Wall Street loves to use confusing terms to make you think only they can do what they do."

We wanted to create a tool which allows non-technical users to engage in conversations about Finance without a needing a dictionary by their side to look-up every other word.

## What it does
**Our Website translates the finance-related input text (or speech) into understandable text which is displayed on our website and can be played out loud via a button click.**

Additionally, each technical term in the output text is linked to its corresponding definition. This feature allows users to learn the meaning of technical terms related to their input.

Finally, if a user's input relates to a specific stock, our program will recognize this. The stock ticker and current stock information (price, etc) will be displayed with the output. Users can see real-time information about the exact investment they're learning about.

## How we built it
The process of transforming technical input text into understandable text is not simple.

After hours of experimenting with co:here, we established that the only way co:here is able to consistently output understandable text (while maintaining the underlying message of the text) is when co:here is given the input text along with context of the text itself. For example, given the input text "Apple's stock responding positively to the Apple Card FICO Score adjustment", co:here is able to produce an understandable version of this text if the underlying context is also given, in this case: "input is stock-related". 

Therefore, we use a the co:here Classifier to determine the context of the input text (related to the overall economy, specific stock). Using the context of the input text, we use the co:here command endpoint to produce the understandable output text.

To give users even more information with our tool, we search our output for key terms and phrases and give hyperlinks pointing to their definitions. We also search for the names and stock symbols of any companies on the S&P 500 to give users their current prices. To accomplish this, we first implemented two web scrapers. Our first web scraper was used to scrape the Investopedia Financial Terms Dictionary and get every term available along with links to their corresponding webpages. The second web scraper was used to scrape Wikipedia for a list of companies on the S&P 500 along with their stock symbol. 

To efficiently search through our output text for these key terms, we implemented a Trie data structure to search for terms while iterating through the text. This allowed us to minimize the number of comparisons needed to find terms and thus improve the overall efficiency of our application. Any time we found a key term or phrase, we replaced it with a hyperlink to it's corresponding Investopedia page. Similarly, whenever we found a company from the S&P 500, we added it to a list of stock prices to display. 

This project was primarily built with Python, Django, HTML with some Javascript.

