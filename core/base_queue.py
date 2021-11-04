import asyncio
from core.session import Session


class BaseQueue:
    def __init__(self, queue: asyncio.Queue, session: Session):
        self.queue = queue
        self.session = session

    async def send_task(self, name_of_task):
        await self._send_task_raw(name_of_task)

    async def _send_task_raw(self, task):
        await self.queue.put(task)

    async def get_task(self):
        return await self._get_task_raw()

    async def _get_task_raw(self):
        return await self.queue.get()
