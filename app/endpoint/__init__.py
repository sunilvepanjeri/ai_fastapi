from fastapi import APIRouter
from . import agentroutes

router = APIRouter()

router.include_router(agentroutes.router, tags=["agentroutes"], prefix="/agent")