"""
All custom exceptions related to the DB operaions.
"""



class BaseDBException(Exception):
    """Base Custom exception for failed DB operations."""

    _default_msg = "DB operation failed."

    def __init__(self, *args: object) -> None:
        args = args if args else (self._default_msg,)
        super().__init__(*args)


class NoRecordFoundDBException(BaseDBException):
    """Custom exception when record is not found."""

    _default_msg = "No record found in the database."

    def __init__(self, *args: object) -> None:
        args = args if args else (self._default_msg,)
        super().__init__(*args)
