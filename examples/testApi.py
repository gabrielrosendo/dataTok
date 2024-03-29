from TikTokApi import TikTokApi
import asyncio
import os
from matplotlib import pyplot as plt
import pandas as pd


# Get your own ms_token from your cookies on tiktok.com
ms_token = os.environ.get("ms_token", "")

async def get_video_attributes(video):
    print("Video found:", video)
    for attr in dir(video):
        #print(attr)
        pass


# prints are for debugging; ignore
async def get_author_info(author):
    author_attributes = dir(author)
    print("Attributes of the user who posted:")
    for attr in author_attributes:
        #print(attr)
        pass

    if hasattr(author, 'username'):
        print("Username:", author.username)

    if hasattr(author, 'liked'):
        #print("Liked:", author.liked)
        for attr in author_attributes:
            #print(attr)
            pass

    if hasattr(author, 'videos'):
        #print("Videos:", author.videos)
        pass

async def get_hashtags_info(video):
    if hasattr(video, 'hashtags'):
        hashtags = video.hashtags
        print("Has hashtags")
        hashtags_attributes = dir(hashtags)
        print("All attributes of the hashtag object:")
        for attr in hashtags_attributes:
            #print(attr)
            pass
        print("Number of hashtags:", len(hashtags))
        for hashtag in hashtags:
            print("#",hashtag.name)

async def get_stats_info(video):
    if hasattr(video, 'stats'):
        stats = video.stats
        print("Views: ", stats['playCount'])
        print("Likes: ", stats['diggCount'])
        print("Comments: ", stats['commentCount'])
        print("Shares: ", stats['shareCount'])
        print("Saves: ", stats['collectCount'])

async def get_sound_info(video):
    sound_info = video.sound
    print("Audio info: ", sound_info)
    for attr in dir(sound_info):
        #print(attr)
        pass
    print("Play URL: ", sound_info.play_url)
    print("Duration: ", sound_info.duration)

async def analyze_engagement_metrics(videos):
    data_list = []

    for video in videos:
        data = {'Views': 0, 'Likes': 0, 'Comments': 0, 'Shares': 0, 'Saves': 0}

        stats = video.stats
        data['Views'] = stats['playCount']
        data['Likes'] = stats['diggCount']
        data['Comments'] = stats['commentCount']
        data['Shares'] = stats['shareCount']
        data['Saves'] = stats['collectCount']

        data_list.append(data)
        

    df = pd.DataFrame(data_list)

    # Plot engagement metrics
    df.plot(kind='bar', subplots=True, layout=(3,2), legend=False)
    plt.show()        


async def trending_videos():
    api = TikTokApi()
    i=0
    await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
    videos = []
    try:
        async for video in api.trending.videos(count=30):
            videos.append(video)
            await get_video_attributes(video)

            if hasattr(video, 'author') and video.author is not None:
                i+=1
                print("Video ",i)
                await get_author_info(video.author)

            await get_hashtags_info(video)
            await get_stats_info(video)
            await get_sound_info(video)

            # Exit the loop after processing the first video for demonstration
            if i > 10:
               break

        await analyze_engagement_metrics(videos)

    except Exception as e:
        print(f"An exception occurred: {e}")

if __name__ == "__main__":
    asyncio.run(trending_videos())