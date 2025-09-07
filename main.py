from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow CORS for Inya.ai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for the payload
class WebsitePayload(BaseModel):
    business_name: str
    business_type: str
    short_tagline: str
    one_liner_value: str
    services_or_products: list[str]
    primary_location_city: str
    service_area: str
    contact: dict
    socials: dict
    brand: dict
    template_type: str
    pages_needed: list[str]
    seo: dict
    plan: dict
    consent_to_deploy: bool

@app.post("/deploy-website")
async def deploy_website(payload: WebsitePayload):
    if not payload.consent_to_deploy:
        raise HTTPException(status_code=400, detail="Consent to deploy is required.")

    # For now, simulate deployment
    simulated_site_url = f"https://{payload.business_name.lower().replace(' ', '')}.netlify.app"

    # In the future, insert code to generate HTML/CSS + Netlify API call

    return {"site_url": simulated_site_url}

@app.get("/")
async def home():
    return {"message": "Chat2Site backend running. Use /docs to interact with the API."}

