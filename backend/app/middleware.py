from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import json

class CustomResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # ✅ Skip docs and openapi routes
        if request.url.path.startswith("/openapi") or request.url.path.startswith("/docs") or request.url.path.startswith("/redoc"):
            return await call_next(request)

        try:
            response = await call_next(request)

            if response.headers.get("content-type") == "application/json":
                body = [section async for section in response.body_iterator]
                raw_body = b"".join(body).decode()
                try:
                    payload = json.loads(raw_body)
                except json.JSONDecodeError:
                    payload = raw_body

                new_response = JSONResponse(
                    status_code=response.status_code,
                    content={
                        "success": True,
                        "data": payload
                    }
                )
                return new_response

            return response

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "error": str(e)
                }
            )
