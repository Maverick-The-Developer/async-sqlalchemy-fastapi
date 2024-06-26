from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base

class Todo(Base):
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)

    def __repr__(self):
        return f"<Todo id={self.id} description={self.description} completed={self.completed} date_created={self.date_created}>"