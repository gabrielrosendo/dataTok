from TikTokApi import TikTokApi
import asyncio
import os

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
        




async def trending_videos():
    api = TikTokApi()
    i=0
    await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
    try:
        async for video in api.trending.videos(count=30):
            await get_video_attributes(video)

            if hasattr(video, 'author') and video.author is not None:
                i+=1
                print("Video ",i)
                await get_author_info(video.author)

            await get_hashtags_info(video)
            await get_stats_info(video)

            # Exit the loop after processing the first video for demonstration
            if i > 3:
                break

    except Exception as e:
        print(f"An exception occurred: {e}")

if __name__ == "__main__":
    asyncio.run(trending_videos())
