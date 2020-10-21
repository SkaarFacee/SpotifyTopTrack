import requests
import argparse
from secret import spotify_token
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to find stats of users individually or as a group",allow_abbrev=False)
    parser.add_argument('-top',"--top_track", action='store', type=str,help="Enter the artist name")
    #parser.add_argument('-t',"--text", action='store', type=str,help="Use the text file")
    args = parser.parse_args()
    if args.top_track:
        #spotify:artist:5Pwc4xIPtQLFEnJriah9YJ
        song_name="hot girl bummer"
        artist=args.top_track
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?q={}&type=artist".format(
        artist
        )

        response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
        )
        response_json = response.json()
        data = response_json["artists"]["items"][0]

        print(data)
