class Unit(object):
    def __init__(self, name, nsecs):
        self.name = name
        self.plural = name + "s"
        self.nsecs = nsecs


MINUTE = Unit("minute", 60)
HOUR = Unit("hour", MINUTE.nsecs * 60)
DAY = Unit("day", HOUR.nsecs * 24)
WEEK = Unit("week", DAY.nsecs * 7)


def format_duration(td):
    remaining_seconds = int(td.total_seconds())
    result = []

    for unit in (WEEK, DAY, HOUR, MINUTE):
        if unit == WEEK and remaining_seconds % unit.nsecs != 0:
            # Say "8 days" instead of "1 week 1 day"
            continue

        v, remaining_seconds = divmod(remaining_seconds, unit.nsecs)
        if v == 1:
            result.append("1 %s" % unit.name)
        elif v > 1:
            result.append("%d %s" % (v, unit.plural))

    return " ".join(result)


def format_mins_secs(td):
    total_seconds = int(td.total_seconds())
    result = []

    mins, secs = divmod(total_seconds, 60)
    if mins:
        result.append("%d min" % mins)

    result.append("%s sec" % secs)

    return " ".join(result)
