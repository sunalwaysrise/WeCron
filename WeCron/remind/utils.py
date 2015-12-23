# coding: utf-8
from __future__ import unicode_literals, absolute_import
from datetime import datetime, timedelta

from ago import delta2dict
from django.utils.timezone import is_aware, utc


def delta2dict( delta ):
    """Accepts a delta, returns a dictionary of units"""
    delta = abs( delta )
    return {
        '年'   : int(delta.days / 365),
        '天'    : int(delta.days % 365),
        '小时'   : int(delta.seconds / 3600),
        '分' : int(delta.seconds / 60) % 60,
        '秒' : delta.seconds % 60,
        # '毫秒' : delta.microseconds
    }


def nature_time(dt, precision=2, past_tense='{}前', future_tense='{}后'):
    """Accept a datetime or timedelta, return a human readable delta string,
    Steal from ago.human
    """
    now = datetime.now(utc if is_aware(dt) else None)
    delta = dt
    if type(dt) is not type(timedelta()):
        delta = now - dt

    the_tense = past_tense
    if delta < timedelta(0):
        the_tense = future_tense

    d = delta2dict(delta)
    hlist = []
    count = 0
    units = ('年', '天', '小时', '分', '秒')
    for unit in units:
        if count >= precision:
            break  # met precision
        if d[unit] == 0:
            continue  # skip 0's
        hlist.append('%s%s' % (d[unit], unit))
        count += 1
    human_delta = ''.join(hlist)
    return the_tense.format(human_delta)