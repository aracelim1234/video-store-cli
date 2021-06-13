import requests
import datetime

class Video:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video



    def create_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
<<<<<<< HEAD

        response = requests.post(self.url+"/videos", json=query_params)

        return response 
        

    def update_video(self, video_id, title=None, release_date=None, total_inventory=None):
        
        if not title:
            title = title["title"]
        if not release_date:
            release_date = release_date["release_date"]
        if not total_inventory:
            total_inventory = total_inventory["total_inventory"]
=======
    

    def update_video(self, title=None, release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.total_inventory["total_inventory"]
>>>>>>> edae95775ebc9edcd9c99418dfdb48364d48b6f1
        
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.get(self.url+f"/videos/{video_id}", json=query_params)
        return response.json()


<<<<<<< HEAD
    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
=======
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
>>>>>>> edae95775ebc9edcd9c99418dfdb48364d48b6f1
        return response.json()


    def all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()


    def get_specific_video(self, video_id):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()
