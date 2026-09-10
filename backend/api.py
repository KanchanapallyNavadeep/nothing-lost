from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from backend.found_item_service import register_found_item
from backend.matching_service import find_matches
from backend.auth import register_user, authenticate_user


app = FastAPI(
    title="Nothing Lost API",
    description="AI Lost and Found System",
    version="1.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Nothing Lost API is running"
    }


# --------------------------------------------------
# FOUND ITEM
# --------------------------------------------------

@app.post("/found-items")
async def create_found_item(

    id: int = Form(...),

    description: str = Form(...),

    category: str = Form(...),

    color: str = Form(...),

    latitude: float = Form(...),

    longitude: float = Form(...),

    image: UploadFile = File(None)

):

    image_path = None


    # Save found-item image
    if image:

        upload_dir = "uploads/found"

        os.makedirs(
            upload_dir,
            exist_ok=True
        )


        image_path = os.path.join(
            upload_dir,
            image.filename
        )


        with open(
            image_path,
            "wb"
        ) as file:

            file.write(
                await image.read()
            )


    # Create found item
    found_item = {

        "id": id,

        "description": description,

        "category": category,

        "color": color,

        "image": image_path,

        "latitude": latitude,

        "longitude": longitude

    }


    # Register in storage
    registered_item = register_found_item(
        found_item
    )


    return {

        "message":
            "Found item registered successfully",

        "item":
            registered_item

    }


# --------------------------------------------------
# LOST ITEM AI MATCHING
# --------------------------------------------------

@app.post("/match")
async def match_lost_item(

    description: str = Form(...),

    category: str = Form(...),

    color: str = Form(...),

    latitude: float = Form(...),

    longitude: float = Form(...),

    image: UploadFile = File(None)

):

    image_path = None


    # Save lost-item image
    if image:

        upload_dir = "uploads/lost"

        os.makedirs(
            upload_dir,
            exist_ok=True
        )


        image_path = os.path.join(
            upload_dir,
            image.filename
        )


        with open(
            image_path,
            "wb"
        ) as file:

            file.write(
                await image.read()
            )


    # Create lost item
    lost_item = {

        "id": 1,

        "description": description,

        "category": category,

        "color": color,

        "image": image_path,

        "latitude": latitude,

        "longitude": longitude

    }


    # Run AI matching
    matches = find_matches(
        lost_item
    )


    return {

        "message":
            "AI matching completed",

        "matches":
            matches

    }


# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

class AuthRequest(BaseModel):

    email: str

    password: str


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

@app.post("/register")
def register(
    request: AuthRequest
):

    user = register_user(

        request.email,

        request.password

    )


    # Email already exists
    if user is None:

        return {

            "success": False,

            "message":
                "Email already registered"

        }


    return {

        "success": True,

        "message":
            "Account created successfully",

        "user": {

            "id":
                user["id"],

            "email":
                user["email"],

            "role":
                user["role"]

        }

    }


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.post("/login")
def login(
    request: AuthRequest
):

    user = authenticate_user(

        request.email,

        request.password

    )


    # Invalid login
    if user is None:

        return {

            "success": False,

            "message":
                "Invalid email or password"

        }


    return {

        "success": True,

        "message":
            "Login successful",

        "user": {

            "id":
                user["id"],

            "email":
                user["email"],

            "role":
                user["role"]

        }

    }