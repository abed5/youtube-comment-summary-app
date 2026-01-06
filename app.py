from flask import Flask, render_template, request
from youtube_comment_downloader import YoutubeCommentDownloader
from google import genai
from pydantic import BaseModel
import json
import os

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)


app = Flask(__name__)


class Section(BaseModel):
    title: str
    paragraph: str

class Summary(BaseModel):
    introduction: str
    summaries: list[Section]

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        downloader = YoutubeCommentDownloader()
        video_url = request.form['content']
        try:
            #youtube_title = YouTube(video_url, 'WEB').title
            video_url_id = video_url.split("v=")[1]
            comments = downloader.get_comments(video_url_id)
            comments_text = [i["text"] for i in comments]
            comments_text_blob = ''
            for i in comments_text:
                comments_text_blob += i
                comments_text_blob += "\\n"
            
            prompt = "Summarize the key themes, opinions, and sentiments expressed in the following YouTube comments. Focus on the most common viewpoints, any notable praise or criticism, and overall tone of the discussion. The comments are as follows, each comment separated by a newline: {}".format(comments_text_blob)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": Summary,
                },
            )
            response_text = response.text
            response_json = json.loads(response_text)
        except:
            return "There was an issue summarizing the video."
        
        return render_template('index.html', summary = response_json, video_url = video_url)
    else:
        summary = None
        return render_template('index.html', summary = summary)

if __name__ == "__main__":
    app.run(debug=False)