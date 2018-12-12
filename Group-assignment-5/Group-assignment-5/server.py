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
            
    return jsonify(toot)

@server.route("/follow/<username>/<user_to_follow>")
def follow(username,user_to_follow):   
    if username not in users[user_to_follow]["followers"]:
        users[user_to_follow]["followers"].append(username)
            
        return jsonify(user_to_follow)
    
@server.route("/unfollow/<username>/<user_to_unfollow>")
def unfollow(username,user_to_unfollow):   
    if username in users[user_to_unfollow]["followers"]:
        i = users[user_to_unfollow]["followers"]
        users[user_to_unfollow]["followers"].pop(i.index(username))
            
        return jsonify(user_to_unfollow)
    
    else:
        return 
    

@server.route("/timeline/<username>")    
def timeline(username):
    timeline = []
    for toot in users[username]["toots"]:
        timeline.append(toot)
    for follower in users[username]["followers"]:
        for toot in users[follower]["toots"]:
            timeline.append(toot)
    
    return jsonify(timeline)

@server.route("/homepage")
def homepage():
    return jsonify(users)

server.run()