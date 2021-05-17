from typing import List, Optional, Tuple

from .piston2d.graphics import GlGraphics
from .piston2d.window.events import Viewport


class Context:
    @property
    def viewport(self) -> Optional[Viewport]: ...
    def reset(self): ...
    def store_view(self): ...
    def transform(self) -> List[List[float]]: ...
    @property
    def view_size(self) -> Tuple[float, float]: ...


def rectangle(color: List[float], rect: List[float],
              transform: List[List[float]], g: GlGraphics): ...


def circle_arc(color: List[float], start: float, end: float,
               rect: List[float], transform: List[List[float]], g: GlGraphics): ...
