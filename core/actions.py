import asyncio

from core.base_actions import BaseActions
from core.session import Session

from core.exceptions.NotValidDataInput import NotValidDataInput


class Actions(BaseActions):
    def __init_(self, queue: asyncio.Queue, session: Session):
        super().__init__(queue, session)
        self.queue = queue
        self.session = Session

    async def task_writer(self):
        while True:
            await asyncio.sleep(1)
            try:
                input_data = int(input(
                    'Choose actions, your choices by number:\n'
                    '1 - clear_data\n'
                    '2 - write_data\n'
                    '3 - get_statistic_by_mont\n'
                    '4 - get_statistic_by_year\n'
                    '5 - get_statistic_by_day\n'
                    '6 - get_all_statistic\n'
                    '7 - get_statistic_by_category'
                ))
            except ValueError:
                print("Вы должны ввести число, а не строку")
                return
            if input_data < 1 or input_data > 7:
                raise NotValidDataInput

            await self.queue.put(input_data)

    async def task_reader(self):
        while True:
            await asyncio.sleep(1)
            data = await self.queue.get()
            await self.process_data(data)

    async def process_data(self, data: str) -> None:
        if data == 1:
            await self.clear_data()
        elif data == 2:
            await self.write_data()
        elif data == 3:
            await self.get_statistic_by_month()
        elif data == 4:
           await  self.get_statistic_by_year()
        elif data == 5:
            await self.get_statistic_by_day()
        elif data == 6:
            await self.get_all_statistic()
        elif data == 7:
            await self.get_statistic_by_category()
