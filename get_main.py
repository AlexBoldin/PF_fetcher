#------------- Getting the UI with PF number request -------------
import tkinter as tk
from tkinter.simpledialog import askstring

root = tk.Tk()
# show askstring dialog without the Tkinter window
root.withdraw()

# Get me the PF number
PF = askstring("PF Fetcher", "Enter your PF; example: PF-00835231")

#------------- Getting the PF link to .tar download -------------
import requests
import argparse
import base64
import json
import sys

host = 'http://ccacheservice.pfizer.com'

#Adding quotation marks around the PF number to be used in post func.
PF2 = '{}'.format(PF)

def post(path, data):
    res = requests.post(host + path, json=data)
    return json.loads(res.text)

response = post('/value', {'structure': PF2,
                           'format': 'ID', 'recipe_path': 'Gibbs Solvation'})

fileHash = response[0]['data']['hash']

# print("URL = \"http://ccacheservice.pfizer.com/file/{}/data\"".format(fileHash))

#------------- Using the link to save the file -------------
url = "http://ccacheservice.pfizer.com/file/{}/data".format(fileHash)
r = requests.get(url, allow_redirects=True)

open(PF + '.tar.gz', 'wb').write(r.content)