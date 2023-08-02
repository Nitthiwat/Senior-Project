import os

import googleapiclient.discovery
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyA-PAoari4oz3St0MFDlSjVnyaSnIKv7ZY")

def get_comments(video_id,keyword):
    request = youtube.commentThreads().list(
        part="id,snippet",
        videoId=video_id,
        textFormat="plainText",
    )

    comments = []
    while request is not None:
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]
            comments.append(comment["snippet"]["textDisplay"])
        request = youtube.commentThreads().list_next(request, response)
    file = open("{}_{}.txt".format(keyword,video_id),"w+",encoding="utf-8")
    data = str()
    for i in comments:
        data+=i+"\n"
    file.write(data)
    file.close()

def search_videos(query):
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q=query,
        maxResults=1,
    )
    response = request.execute()

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        print(url)
        get_comments(video_id,query)
        
if __name__ == "__main__":
    search_videos(input("Please Enter Your keyword : "))