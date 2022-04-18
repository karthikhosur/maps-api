import requests

import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(keyword):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.8662653%2C-87.6679668&radius=15&keyword=" + \
        keyword+"&key=AIzaSyCvqWIuttQ-8uwHS5aOD4OxpT7lUq7lbes"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    results = []
    result = {}
    # for r in range(response.text[0]["results"]):
    #     result["name"] = r["name"]
    #     result["latitude"] = r["geometry"]["location"]["lat"]
    #     result["longitude"] = r["geometry"]["location"]["lng"]
    #     coords_1 = [41.8662653, -87.6679668]
    #     coords_2 = [result["latitude"], result["longitude"]]
    #     result["distance"] = str((
    #         (((coords_2[0] - coords_1[0])**2) + ((coords_2[1]-coords_1[1])**2))**0.5))

    #     results.append(result)

    return json.dumps(response.text, indent=4)
