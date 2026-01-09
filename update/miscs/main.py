from fastapi import APIRouter, Depends, HTTPException, Header
import httpx
import motor.motor_asyncio as motor
import os, jwt
from pydantic import BaseModel
from typing import Optional

app = APIRouter()
SECRET_KEY = os.environ.get("SECRET")
ALGORITHM = "HS256"

async def verify(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    token = authorization.split(" ")[1] if " " in authorization else authorization
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")


async def getDb():
    mongoClient = motor.AsyncIOMotorClient(
        os.environ.get("MONGODB_URI") or "mongodb://localhost:27017"
    )
    return mongoClient[os.getenv("DB_NAME") or "AdmiBlog"]["Miscs"]

class UpdateRequestBody(BaseModel):
    content: str


@app.put("/announcement")
async def updateAnno(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "announcement": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )

@app.put("/commentProtocol")
async def updateCommentProtocol(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "commentProtocol": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )

@app.put("/privacy")
async def updatePrivacy(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "privacy": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )

@app.put("/license")
async def updateLicense(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "license": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )

@app.put("/flinkAnno")
async def updateFlinkAnno(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "flinkAnno": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )

@app.put("/about")
async def updateAbout(
    body: UpdateRequestBody, currentCollection=Depends(getDb), user=Depends(verify)
):
    try:
        await currentCollection.update_one(
            {},
            {
                "$set": {
                    "about": body.content
                }
            },
        )
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "internal server error", "error": str(e)},
        )