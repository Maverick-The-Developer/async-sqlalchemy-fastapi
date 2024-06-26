from models import Todo
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from sqlalchemy import desc


async def get_all_todos(async_session: async_sessionmaker[AsyncSession]):
    async with async_session() as session:
        statement = select(Todo).order_by(desc(Todo.date_created))

        result = await session.execute(statement)

        return result.scalars().all()


async def create_todo(async_session: async_sessionmaker[AsyncSession], description: str, completed: bool = False):
    async with async_session() as session:
        todo = Todo(description=description, completed=completed)
        session.add(todo)
        await session.commit()

        return todo

async def update_todo(async_session: async_sessionmaker[AsyncSession], id: int, description: str, completed: bool):
    async with async_session() as session:
        statement = select(Todo).where(Todo.id == id)
        result = await session.execute(statement)
        todo = result.scalars().first()

        if not todo:
            return None

        todo.description = description
        todo.completed = completed
        await session.commit()

        return todo
    
async def delete_todo(async_session: async_sessionmaker[AsyncSession], id: int):
    async with async_session() as session:
        statement = select(Todo).where(Todo.id == id)
        result = await session.execute(statement)
        todo = result.scalars().first()

        if not todo:
            return None

        await session.delete(todo)
        await session.commit()

        return todo
