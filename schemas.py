from pydantic import BaseModel


class Animes(BaseModel):
    id: int
    title: str
    episodes: int | None
    ranking: int
    score: float
    aired: str
    img: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True