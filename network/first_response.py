import asyncio
from httpx import AsyncClient


async def fetch_url(client: AsyncClient, url):
    try:
        response = await client.get(url)
        return response
    except Exception:
        return None


async def get_first_response(urls: list[str]):
    async with AsyncClient(follow_redirects=True) as client:
        tasks = [asyncio.create_task(fetch_url(client, url)) for url in urls]
        while tasks:
            done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                response = task.result()
                if response is not None and response.status_code == 200:
                    return response.content
            tasks = [task for task in tasks if not task.done()]
        return None
