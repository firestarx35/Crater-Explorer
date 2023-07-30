import os
import uvicorn

from fastapi import FastAPI, Request #, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware


class cdm_data(BaseModel):
    image_location: str
    planet: str
    output_name: Optional[str] = ''
    optional_parameters: bool
    image_dim: Optional[str] = ''
    image_res: Optional[str] = ''
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''
    planet_radius: Optional[str] = ''


def run_cdm(data):
    """Runs the inference model

    Returns:
        list: Contains annnoted image and csv file names 
    """

    if (data.optional_parameters and data.latitude != '' and data.longitude != ''):
        planet = data.planet
        image_location = data.image_location
        latitude = data.latitude
        longitude = data.longitude
        image_res = float(data.image_res)
        image_dim = data.image_dim.upper().split('X')
        image_dim = {'W': float(image_dim[0]), 'H': float(image_dim[-1])}
        planet_radius = float(data.planet_radius)
        # images, csvs = model.run_model(planet, image_location, latitude, longitude, image_res, image_dim, planet_radius)
        # images = [image for image in images if '.png' in image]
        # images = sorted(images)
        # cdm_data = [images, csv]

        images = os.listdir("./static/detection")
        images = [image for image in images if '.png' in image or '.jpg' in image or 'tif' in image or 'jpeg' in image]
        images = sorted(images)
        csv = os.listdir("./static/csv")
        cdm_data = [images, csv[0]]

    else:        
        planet = data.planet
        image_location = data.image_location
        
        # images, csvs = run_model(planet, image_location)
        # images = [image for image in images if '.png' in image]
        # images = sorted(images)
        # cdm_data = [images, csv]

        print(planet, image_location)
        images = os.listdir("./static/detection")
        images = [image for image in images if '.png' in image or '.jpg' in image or 'tif' in image or 'jpeg' in image]
        print(images)
        images = sorted(images)
        csv = os.listdir("./static/csv")
        cdm_data = [images, csv[0]]
        
    return cdm_data



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Landing site for GUI

    Args:
        request (Request): HTTP URL

    Returns:
        HTML, CSS, JS: Renders GUI
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/documentation", response_class=HTMLResponse)
async def docs(request: Request):
    """Documentation

    Args:
        request (Request): HTTP URL for documentation

    Returns:
        HTML, CSS: Renders documentation 
    """
    return templates.TemplateResponse("docs.html", {"request": request})


@app.post("/run_model")
async def run_model(data: cdm_data):
    """Gets the CDM parameters and passes the data to inference model

    Args:
        data (cdm_data): CDM parameters from GUI

    Returns:
        List: List of images generated by the model
    """

    response = run_cdm(data)
    print(response)

    return response


@app.get("/download_csv/")
async def download_csv(file: str):
    """Download the csv data

    Args:
        data (str): csv file name

    Returns:
        csv: csv file of the annoted image
    """
    return FileResponse("./static/csv/" + file)
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
