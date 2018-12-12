# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:39:36 2018

@author: Leila
"""

#%%

from flask import Flask, jsonify

server = Flask("tooter")

users = {"javi":{
                    "followers":["pepegar"],
                      "toots":["hi"]},
        "pepegar":{
                     "followers":[],
                      "toots":["hey"]},

        "theRealDonaldTrump":{
                      "followers":[],
                      "toots":[]}}

@server.route("/new_toot/<username>/<toot>")
def new_toot(username,toot):   
    users[username]["toots"].append(toot)
            
    return jsonify(users)

@server.route("/follow/<username>/<user_to_follow>")
def follow(username,user_to_follow):   
    users[user_to_follow]["followers"].append(username)
            
    return jsonify(users[user_to_follow]["followers"])

@server.route("/unfollow/<username>/<user_to_unfollow>")
def unfollow(username,user_to_unfollow):     
    users[user_to_unfollow]["followers"].pop(username)
            
    return jsonify(users[user_to_unfollow]["followers"])

@server.route("/timeline/<username>")    
def timeline(username):
    timeline = []
    for toot in users[username]["toots"]:
        timeline.append(toot)
    for follower in users[username]["followers"]:
        for toot in users[follower]["toots"]:
            timeline.append(toot)
    
    return timeline
                
server.run()