import uvicorn

from src.lantern.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'src.lantern.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
