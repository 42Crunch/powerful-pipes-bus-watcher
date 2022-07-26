from __future__ import annotations

from .interface import BusInterface
from ..exceptions import WatchBusException
from .redis import RedisBusSimpleQueue, RedisBusPubSub

def connect_bus(connection_string: str) -> BusInterface:

    if connection_string.startswith("redis://"):
        return RedisBusSimpleQueue.open(connection_string)

    elif connection_string.startswith("redis+pubsub://"):
        return RedisBusPubSub.open(connection_string)

    else:
        raise WatchBusException("Invalid connection string URI")

__all__ = ("connect_bus", )
