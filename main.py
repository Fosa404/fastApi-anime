from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db import get_db
from models import Animes
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)


@app.get('/')
def home():
    return "Hellow World!"

@app.get('/top/animes')
def get_top_animes(db: Session = Depends(get_db)):
    top_animes = db.query(Animes).all()
    if not top_animes:
        return HTTPException(status_code=404, detail='error_404 item not found')
    return top_animes


@app.get('/anime/{id}')
def get_anime(id: int, db: Session= Depends(get_db)):
    anime = db.query(Animes).filter(Animes.id == id).first()
    if not anime:
        return HTTPException(status_code=404, detail='error_404 item not found')
    return anime
