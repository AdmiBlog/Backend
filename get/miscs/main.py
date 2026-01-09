from fastapi import APIRouter, Depends, HTTPException
import motor.motor_asyncio as motor
import os

app = APIRouter()


async def getDb():
    mongoClient = motor.AsyncIOMotorClient(
        os.environ.get("MONGODB_URI") or "mongodb://localhost:27017"
    )
    return mongoClient[os.getenv("DB_NAME") or "AdmiBlog"]["Miscs"]

@app.get("/announcement")
async def announcement(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["announcement"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )

@app.get("/commentProtocol")
async def commentProtocol(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["commentProtocol"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )

@app.get("/privacy")
async def privacy(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["privacy"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )

@app.get("/license")
async def license(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["license"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )

@app.get("/flinkAnno")
async def flinkAnno(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["flinkAnno"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )

@app.get("/about")
async def about(currentCollection=Depends(getDb)):
    try:
        res=await currentCollection.find().to_list(length=None)
        return {"message": "success","data" : res[0]["about"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"message": "fail", "error": str(e)}
        )
