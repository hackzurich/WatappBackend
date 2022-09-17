from fastapi import FastAPI, BackgroundTasks, UploadFile, HTTPException, Depends
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from uuid import UUID, uuid4
from pathlib import Path
from datetime import datetime
import googlemaps
import shutil
import os

from .main import app
from .user import User
from .auth import get_current_active_user

try:
	with open("__GCP_API_KEY", 'r') as f:
		gmaps = googlemaps.Client(key=f.readline())
except Exception as e:
	print(e)
	gmaps = None

@app.get("/challenge")
async def get_best_challenge(user: User = Depends(get_current_active_user), geolocation = None):
    return {"user": user}

@app.get("/place")
async def is_in_supermarket(latitude: float, longitude: float, user: User = Depends(get_current_active_user)):
	# Place types docs: https://developers.google.com/maps/documentation/places/web-service/supported_types
	# We can also ask for other place types
	place_supermarket= gmaps.places_nearby((latitude, longitude), radius= 30, type= "supermarket")
	print(place_supermarket)
	is_in_supermarket= len(place_supermarket['results'])
	return is_in_supermarket