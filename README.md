# YouTube Comments Summarizer

This is a Flask-based web application that allows users to input a YouTube video URL and receive a structured summary of the viewer comments. The summary captures the key themes, opinions, sentiments, and tone of the discussion using Google's Gemini AI model.

## Features

* Extracts comments from YouTube videos.
* Uses Gemini (Google's LLM) to generate summaries.
* Presents structured summaries with an introduction and detailed sections.
* Simple web interface for user interaction.

## Dependencies

* [Flask](https://flask.palletsprojects.com/)
* [youtube-comment-downloader](https://pypi.org/project/youtube-comment-downloader/)
* [pytubefix](https://pypi.org/project/pytubefix/)
* [google-generativeai](https://pypi.org/project/google-generativeai/)
* [pydantic](https://pydantic-docs.helpmanual.io/)

Install all dependencies using:

```bash
pip install flask youtube-comment-downloader pytubefix google-generativeai pydantic
```

## Environment Variables

The app uses an API key for Google's Gemini AI. You need to set the following environment variable:

```bash
export GEMINI_API_KEY='your-gemini-api-key-here'
```

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abed5/youtube-comments-summarizer.git
   cd youtube-comments-summarizer
   ```

2. **Run the application:**

   ```bash
   python app.py
   ```

3. **Access it in your browser:**

   Open http://127.0.0.1:5000 in your web browser.

4. **How it works:**

   * Enter a YouTube video URL in the input form.
   * The app downloads comments, generates a summary using Gemini, and displays it on the page.

## How it Works

* The app extracts the video title and comments from the URL.
* It prompts Gemini with a structured summary request.
* Gemini responds with JSON adhering to a Pydantic schema (`Summary`), which includes:

  * An introduction.
  * A list of titled sections with summarized content.

##  Project Structure

```
.
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # HTML template
└── README.md             # Project documentation
```

## ⚠️ Notes

* Be sure your API key has access to the Gemini model `gemini-2.0-flash`.
* This app may not work with videos that have disabled or no comments.