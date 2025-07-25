from fastapi import Request

async def get_client_ip(request: Request):
    return request.client.host
