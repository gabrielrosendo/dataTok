# TikTok Video Analysis Program

This Python program uses the TikTokApi library to fetch trending videos from TikTok and perform analysis on their attributes, authors, and associated hashtags.

## Prerequisites

- Python 3
- TikTokApi library (`pip install TikTokApi`)

## Setup

1. Clone the repository or download the source code.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set the `ms_token` environment variable in your system with your TikTok token obtained from your TikTok cookies.

## Usage

Run the `trending_videos()` function from `main.py` to fetch and analyze trending TikTok videos.

[...]

## Functionality

- Fetches 30 trending videos from TikTok.
- Displays various attributes of each video, its author, and associated hashtags.
- Demonstrates the usage of TikTokApi library methods to access video data.

## Important Notes

- Ensure to set the `ms_token` environment variable before running the program to access TikTok's API.

## Acknowledgments

- The program utilizes the TikTokApi library to interact with TikTok's API.
- This project is for educational purposes and may require adjustments based on TikTok's API changes.
