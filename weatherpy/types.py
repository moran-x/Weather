from .translate import *
from gettext import gettext as _
set_up()

class Units(object):
    METRIC = "metric"
    ENGLISH = "english"

    @staticmethod
    def to_array():
        return [Units.METRIC, Units.ENGLISH]


class TimeFormats(object):
    MILITARY = "military"
    CIVILIAN = "civilian"

    @staticmethod
    def to_array():
        return [TimeFormats.MILITARY, TimeFormats.CIVILIAN]


class Direction(object):
    @staticmethod
    def shorthand(direction):
        normalized = direction.lower()
        if normalized == "east":
            return _("E")
        if normalized == "west":
            return _("W")
        if normalized == "south":
            return _("S")
        if normalized == "north":
            return _("N")
        return direction

class DateFormats(object):
    DATE  = "date"
    DAY   = "weekday"

    @staticmethod
    def to_array():
        return [DateFormats.DATE, DateFormats.DAY]
