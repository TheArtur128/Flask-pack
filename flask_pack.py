from typing import Final, Iterable, Callable

from pyhandling.collections_ import MultiRange


class StatusCodeGroup:
    """
    Class for storing the HTTP status codes of responses in the form of a
    structure and declarative access to them.
    """

    INFORMATIONAL: Final[MultiRange] = MultiRange(range(100, 200))
    SUCCESSFUL: Final[MultiRange] = MultiRange(range(200, 300))
    REDIRECTION: Final[MultiRange] = MultiRange(range(300, 400))
    CLIENT_ERROR: Final[MultiRange] = MultiRange(range(400, 500))
    SERVER_ERROR: Final[MultiRange] = MultiRange(range(500, 600))

    GOOD: Final[MultiRange] = MultiRange(range(100, 400))
    ERROR: Final[MultiRange] = MultiRange(range(400, 600))

    ALL: Final[MultiRange] = MultiRange(range(100, 600))
