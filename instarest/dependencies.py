from collections.abc import Generator
import httpx
from .db.session import SessionLocal

# see here for config suggestions: https://stackoverflow.com/questions/74184899/is-having-a-concurrent-futures-threadpoolexecutor-call-dangerous-in-a-fastapi-en/74239367#74239367
limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(10.0, read=20.0)
httpx_client = httpx.AsyncClient(limits=limits, timeout=timeout)


# ********use for DB initialization*****
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
