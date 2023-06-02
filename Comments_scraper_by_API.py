import googleapiclient.discovery
import pandas as pd
from tqdm import tqdm
from environment import env_var
from utils import read_yaml

SECRET=read_yaml("config\config.yaml")
# Get your API key from the Google Developers Console
api_key = SECRET["API"]

# Create a YouTube resource object
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Get the video ID from the YouTube video URL
video_id = "liJVSwOiiwg"

# Get the comments for the video
comments_response = youtube.commentThreads().list(
    part=["id","snippet"],
    videoId=video_id,
    maxResults=100,
).execute()

# Extract the comments from the response
comments = comments_response["items"]

# empty list to store the comments
data=[]

# Print the comments
for id,comment in tqdm(enumerate(comments)):
  data.append(comment["snippet"]["topLevelComment"]["snippet"]['textOriginal'])
  #print(comment["snippet"]["topLevelComment"]["snippet"]['textOriginal'])

#DataFrame
data=pd.DataFrame(data)

#storing the data in csv
data.to_csv("comments.csv")