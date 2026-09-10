from dataclasses import dataclass
from typing import Optional


@dataclass
class LostItem:

    id: int
    description: str
    category: str
    color: str

    image: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class FoundItem:

    id: int
    description: str
    category: str
    color: str

    image: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None