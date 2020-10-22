import requests
import argparse

from secret import spotify_token

def Search(artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?q={}&type=artist".format(artist)

        response = requests.get(query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
        )
        response_json = response.json()
        data = response_json["artists"]["items"][0]
        return data
    
def toptracks(data):
    id=data["uri"].split(":")[-1]
    query="https://api.spotify.com/v1/artists/{}/top-tracks?market=ES".format(id)
    response=requests.get(query,
                          headers={
                              "Content-Type": "application/json",
                              "Authorization": "Bearer {}".format(spotify_token)
                          })
    response_json = response.json()
    tracks=response_json["tracks"]
    for num in range(len(tracks)):
        print(tracks[num]["name"])

def topalbums(data):
    list=[]
    id=data["uri"].split(":")[-1]
    query="https://api.spotify.com/v1/artists/{}/albums".format(id)
    response=requests.get(query,headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })
    response_json=response.json()
    items=response_json["items"]
    for num in range(len(items)-1):
       list.append(items[num]["name"])
    uniqueName = [] 
    for i in list:
        if not i in uniqueName:
            uniqueName.append(i)
    for name in uniqueName:
        print(name)
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script that uses spotify API to search for an artist, displaying there top tracks and albums released in spotify.",allow_abbrev=False)
    parser.add_argument('-xd',"--name", action='store', type=str,help="Enter the artist name")
    args = parser.parse_args()
    if args.name:
        print("Top Tracks are:\n")
        toptracks(Search(args.name))
        print("\nTop Albums are:\n")
        topalbums(Search(args.name))
