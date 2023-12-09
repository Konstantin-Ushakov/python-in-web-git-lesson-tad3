from fastapi import FastAPI, HTTPException, status

from typing import Any, Optional
from models import UserToCreate, User
from database import USERS


app = FastAPI(
    title='Learning App'
)



@app.get('/users')
def get_users() -> list[dict[str, Any]]:
    return USERS


@app.post('/users')
def create_user(user: UserToCreate) -> User:
    if not USERS:
        user_id = 1
    else:
        user_id = max(user['id'] for user in USERS) + 1

    user.age
    user = User(id=user_id, **user.model_dump())
    USERS.append(user.model_dump())
    
    return user


@app.get('/users/{user_id}')
def get_user(user_id: int) -> User:
    user = next(User(**user) if user["id"] == user_id else None for user in USERS)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User by id {user_id} not found."
        )
    
@app.delete('/users/{user_id}')
def delete_user(user_id: int) -> Optional[User]:
    try:
        user_from_db = get_user(user_id)
        USERS.remove(user_from_db.model_dump())
        return user_from_db
    except HTTPException:
        return None

@app.put('/users/{user_id}')
def update_user(user: UserToCreate, user_id: int) -> User:
    delete_user(user_id)
    return create_user(user)



# app.put('/users/{user_id}') - change_user_data(user_id: int, new_user_data: UserToCreate) -> None
# app.patch('/users/{user_id}') - change_user_name(user_id: int, new_name: str = Query(min_length=1)) -> None
# app.delete('/users/{user_id}', status_code=204) - delete_user(user_id: int) -> None
# app.get('/users') - get_all_users() -> list[User]
# app.post('/users/from-file') - import_users_from_file(file: UploadFile) -> None
# app.get('/users/as-csv') - export_users_to_csv() -> StreamingResponse
