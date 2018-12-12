# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:39:57 2018

@author: Leila
"""

#%%

import requests

def new_toot(username,toot):
    
    url = "http://127.0.0.1:5000/new_toot/" + username + "/" + toot
    
    response = requests.get(url)
    toot = response.json()
    
    return username + " has tooted : " + toot

new_toot("javi","coucou")

#%%

def follow(username,user_to_follow):
    
    url = "http://127.0.0.1:5000/follow/" + username + "/" + user_to_follow
    
    response = requests.get(url)
    user_to_follow = response.json()       
             
    return "You are now following " + str(user_to_follow)

follow("javi","theRealDonaldTrump")

#%%

def unfollow(username,user_to_unfollow):
    
    url = "http://127.0.0.1:5000/unfollow/" + username + "/" + user_to_unfollow
    
    response = requests.get(url)
    user_to_unfollow = response.json()
    
    return username + " has unfollowed " + str(user_to_unfollow)

unfollow("javi","theRealDonaldTrump")

#%%

def timeline(username):
    
    url = "http://127.0.0.1:5000/timeline/" + username
    
    response = requests.get(url)
    timeline = response.json()
    
    return "Here is your timeline " , timeline

timeline("javi")