from pyexpat import model
from typing import List, Optional
from fastapi import Depends, Response, status, HTTPException, APIRouter

from app import oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schema, oauth2
from sqlalchemy.orm import Session


router = APIRouter(prefix="/vote", tags=["Votes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote, db: Session = Depends(get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Vote.post_id == vote.id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id:  {vote.id} does not exist")

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.id, models.Vote.user_id == current_user.id)
    found_post = vote_query.first()
    if (vote.dir == 1):
        if found_post:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} already voted on the post {vote.id}")
        new_vote = models.Vote(post_id=vote.id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message", "Successfully created votes"}
    else:
        if not found_post:
            raise HTTPException(
                status_code=status.HTTP_404_CONFLICT, detail=f"Vote {vote.id} does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message", "Successfully delted votes"}
