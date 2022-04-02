
from pydoc import ModuleScanner
import random
from turtle import pos, title
from typing import Optional, List

from fastapi import Depends, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body

from random import Random, randrange

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schema, helper
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

from .routers import post, user, auth, vote
from pydantic import BaseSettings

from app import database
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)
origins = ["https://www.google.com"]
origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


my_posts = [{"title": "Post 1", "content": "Content Post 1", "id": 1},
            {"title": "Post 1", "content": "Content Post 1", "id": 2}]


def get_post_by_id(id):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_post_index(id):
    for i,  p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():

    return {"message": "Hello World"}
