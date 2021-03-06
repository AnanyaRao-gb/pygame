from typing import Tuple, Union, List, overload, Sequence

def get_pressed() -> Tuple[bool, bool, bool, bool, bool]: ...
def get_pos() -> Tuple[int, int]: ...
def get_rel() -> Tuple[int, int]: ...
@overload
def set_pos(pos: Union[List[float], Tuple[float, float]]) -> None: ...
@overload
def set_pos(x: float, y: float) -> None: ...
def set_visible(value: bool) -> int: ...
def get_visible() -> bool: ...
def get_focused() -> int: ...
def set_cursor(
    size: Union[Tuple[int, int], List[int]],
    hotspot: Union[Tuple[int, int], List[int]],
    xormasks: Sequence[int],
    andmasks: Sequence[int],
) -> None: ...  # This needs to be checked
def get_cursor() -> Tuple[
    Tuple[int, int], Tuple[int, int], Sequence[int], Sequence[int]
]: ...
