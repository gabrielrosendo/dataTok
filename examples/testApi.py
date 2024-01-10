from TikTokApi import TikTokApi
import asyncio
import os

# Get your own ms_token from your cookies on tiktok.com
ms_token = os.environ.get("ms_token", "")

async def get_video_attributes(video):
    print("Video found:", video)
    for attr in dir(video):
        print(attr)
        pass

async def get_author_info(author):
    print("Has an actor")
    author_attributes = dir(author)
    print("All attributes of the author object:")
    for attr in author_attributes:
        #print(attr)
        pass

    if hasattr(author, 'username'):
        print("Username:", author.username)

    if hasattr(author, 'liked'):
        print("Liked:", author.liked)
        for attr in author_attributes:
            #print(attr)
            pass

    if hasattr(author, 'videos'):
        print("Videos:", author.videos)

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
            print(hashtag.name)

async def get_stats_info(video):
    if hasattr(video, 'stats'):
        stats = video.stats
        print("Has stats")
        stats_attributes = dir(stats)
        print("All attributes of the stats object:")
        for attr in stats_attributes:
            attribute_value = getattr(stats, attr)
            print(attr, type(attribute_value))
            if isinstance(attribute_value, dict):
                print("Keys:", list(attribute_value.keys()))  # Print keys if it's a dictionary
            else:
                print("No")
            




async def trending_videos():
    api = TikTokApi()
    await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
    try:
        async for video in api.trending.videos(count=30):
            await get_video_attributes(video)

            if hasattr(video, 'author') and video.author is not None:
                await get_author_info(video.author)

            await get_hashtags_info(video)
            await get_stats_info(video)

            # Exit the loop after processing the first video for demonstration
            break

    except Exception as e:
        print(f"An exception occurred: {e}")

if __name__ == "__main__":
    asyncio.run(trending_videos())
