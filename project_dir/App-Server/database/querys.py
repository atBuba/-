from datetime import datetime
from sqlalchemy.orm import Session
from models.dto_models import JiraTaskMessageDTO, JiraTaskCommentsDTO
from models.orm_models import Task, Message, Prediction




def get_comments_on_filter(db: Session, st_time: str = None, task_id: int = None, task_name: str = None):
    result = db.filter(Message)
    
