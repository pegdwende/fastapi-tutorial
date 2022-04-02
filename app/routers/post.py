
from typing import List, Optional
from fastapi import Depends, Response, status, HTTPException, APIRouter

from app import oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schema, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(prefix="/posts", tags=['Posts'])

# response_model=List[schema.Post]

# response_model=List[schema.PostOut]


@router.get("/", response_model=List[schema.PostOut])
async def get_posts(db: Session = Depends(get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(
    #     models.Post.owner_id == current_user.id).all()

    print(search)
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(posts)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}", response_model=schema.PostOut)
async def get_post(id: int, db: Session = Depends(get_db),  current_user: schema.TokenData = Depends(oauth2.get_current_user)):

    new_post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not new_post:
        #     response.status_code = status.HTTP_404_NOT_FOUND
        #     return {'message': f"post with id :{id} was not found"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"post with id :{id} was not found")

    if new_post.Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f" Not authorized to perform requested action")

    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db),  current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    # deleting post
    # find the index
    # my_posts.pop
    # cursor.execute(
    #     """ DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    # index = find_post_index(id)
    post = db.query(models.Post).filter(models.Post.id == id)

    post_to_Delete = post.first()
    if post_to_Delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")

    if post_to_Delete.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f" Not authorized to perform requested action")

    # my_posts.pop(index)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
async def update_post(id: int, post: schema.PostCreate, db: Session = Depends(get_db),  current_user: schema.TokenData = Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     """ UPDATE posts SET title = %s, content= %s, published = %s WHERE id = %s RETURNING* """, (post.title, post.content, post.published, str(id),))
    # updated_post = cursor.fetchone()
    # conn.commit()

    # print(post)
    # post_dict = post.dict()
    # post_dict['id'] = id
    # index = find_post_index(id)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    existing_post = post_query.first()
    if existing_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")

    if existing_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f" Not authorized to perform requested action")

    post_query.update(post.dict(), synchronize_session=False)

    db.commit()
    return post_query.first()
