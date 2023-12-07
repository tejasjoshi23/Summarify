# Summarify - Text Summarizer 

This repository contains the code for a web-based text summarizer application. The application uses the Hugging 
Face API with the `facebook/bart-large-cnn` model for text summarization.

## Overview

The Text Summarizer Application allows users to input text and receive a summarized version of the input. 
It leverages Hugging Face's BART(Facebook's state-of-the-art Sequence-to-Sequence model) to generate meaningful 
and concise summaries.

## Features

- Input Text: Users can input text for summarization.
- Summarization Algorithm: Utilizes the `facebook/bart-large-cnn` model for accurate and coherent text summarization.
- Adjustable Summary Length: Users can control the length of the generated summary with a slider.
- User Interface: A simple web interface built with Flask and HTML/CSS.


## Usage

1. Open the application by running the Flask application (`app.py`).
2. Access the application in your web browser at the specified URL.
3. Enter the text you want to summarize in the input textarea.
4. Adjust the summary length using the slider.
5. Click the "Submit" button to receive the summarized text.
6. Use the "Copy Text" button to copy the summary to the clipboard.

## Project Structure
- `/templates/index.html`: HTML template file for the user interface.
- `app.py` : Flask application handling web routes and text summarization.

## Getting Started

To run the application locally:

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   ```

2. Change into the project directory:

   ```bash
   cd text-summarizer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Dependencies

- Flask
- Requests

## Acknowledgments

- The summarization model is provided by Hugging Face.
