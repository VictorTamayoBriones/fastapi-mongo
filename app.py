from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="Rest API with fastapi and MongoDB",
    description="This is a simple fastapi with mongodb",
    version="0.0.1",
    openapi_tags=tags_metadata
);

app.include_router(user)
