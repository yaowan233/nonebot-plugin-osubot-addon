from functools import wraps
from typing import TypeVar, Callable
from typing_extensions import ParamSpec
from loguru import logger

T = TypeVar("T")
P = ParamSpec("P")


def auto_retry(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        for i in range(5):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"{e} | Retrying... {i + 1}/5")
        logger.error("多次重试失败，请检查网络连接")

    return wrapper
