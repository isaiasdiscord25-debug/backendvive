vimport requests
import random
from flask import Flask, jsonify, request
import json
import os
import base64
import hashlib
from datetime import datetime, timedelta


# make a function for everything below "/api/TitleData" and for the title data use the "/" app route.

class GameInfo:

    def __init__(self):
        self.TitleId: str = "C936A"
        self.SecretKey: str = "PQ3FHH9YECUBRT8AN96QAU51UZAAXSHGPD5Z9UHMDC6H66G3P7"
        self.ApiKey: str = "OC|25644786718509327|a443738de12eb83a63f7bebbbb3835d6s"
        self.PlayfabAuthenticationWebhook: str = "https://discord.com/api/webhooks/1387547548541259876/rbDmOTc-eZglO-LhD-3qlBcDmdvypeg6_8TRzVkpgmtTiyb06EgpevIlTKjj9Dd2GKJJ"
        self.QuestsWebhook: str = "https://discord.com/api/webhooks/1387546201053987006/7EZOrbHNT6numfD7SsAKsP9p6k_SXX9VGBvcaqupdjPqHyV22AP71SpzgiHHVZnahsQI"
        self.PhotonWebhook: str = "https://discord.com/api/webhooks/1387547714673442916/TMtUhSWtjQbeZN_2mtd9a4XULfFKw8mhGKPp08qlSkpiIUKlSf_FAmuJ15QxtjWtZxNd"

    def get_auth_headers(self):
        return {
            "content-type": "application/json",
            "X-SecretKey": self.SecretKey
        }
polls = [
    {
        "pollId": 1,
        "question": "THIS IS A POLL!!!",
        "voteOptions": [
            "YES",
            "NO"
        ],
        "voteCount": [],
        "predictionCount": [],
        "startTime": "2025-06-30T12:00:00",
        "endTime": "2025-06-16T12:00:00",
        "isActive": True
    }
]

def GetAuthHeaders() -> dict:
    return {"Content-Type": "application/json", "X-SecretKey": settings.SecretKey}

item_names = [
    "LBAEY.", "LBAFH.", "LBAFA.", "LBAFB.", "LBAFC.", "LBAFD.", "LBAFE.", "LBAFF.", "LBAFG.", "LBAEZ.", "LBAFP.", "LBAFQ.", "LBAFR.", "LBAEX.", "LBAGJ." 
] 

settings = GameInfo()
app = Flask(__name__)
playfab_cache = {}
mute_cache = {}


def return_function_json(data, funcname, funcparam={}):
    user_id = data["FunctionParameter"]["CallerEntityProfile"]["Lineage"][
        "TitlePlayerAccountId"]

    response = requests.post(
        url=
        f"https://{settings.TitleId}.playfabapi.com/Server/ExecuteCloudScript",
        json={
            "PlayFabId": user_id,
            "FunctionName": funcname,
            "FunctionParameter": funcparam
        },
        headers=settings.get_auth_headers())

    if response.status_code == 200:
        return jsonify(response.json().get("data").get(
            "FunctionResult")), response.status_code
    else:
        return jsonify({}), response.status_code


def nonce_validator(nonce, oculus_id):
    response = requests.post(
        url=
        f'https://graph.oculus.com/user_nonce_validate?nonce={nonce}&user_id={oculus_id}&access_token={settings.ApiKey}',
        url1=
        f'https://graph.oculus.com/user_nonce_validate?nonce={nonce}&user_id={oculus_id}&access_token={settings.ApiKey1}',
        headers={"content-type": "application/json"})
    return response.json().get("is_valid")

PLAYFAB_AUTH_URL = f"https://{settings.TitleId}.playfabapi.com/Client/LoginWithCustomID"
PLAYFAB_BAN_URL = f"https://{settings.TitleId}.playfabapi.com/Admin/BanUsers"

Quests = {"AllActiveQuests": {
		"DailyQuests": [
			{
				"selectCount": 1,
				"name": "Gameplay",
				"quests": [
					{
						"disable": False,
						"questID": 11,
						"weight": 1,
						"questName": "PLAY INFECTION",... (486 KB left)
