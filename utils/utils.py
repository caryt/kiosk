"""Various Utility Functions.
"""

def years_between(frm, to):
    """Return the whole number of years between two dates.
    """
    return to.year - frm.year - ((to.month, to.day) < (frm.month, frm.day))

def current_record(records, date):
    """Return the single record effective as as `date` from a list of `records`.
    Note: This returns the first effective record. It does not check for
    inconsistent overlapping periods.
    """
    for rec in records:
        if rec.from_date <= date and rec.to_date > date:
            return rec
    return None

def current_records(records, date):
    """Return a list of records effective as as `date` from a list of `records`.
    """
    result = []
    for rec in records:
        if rec.from_date <= date and rec.to_date > date and rec not in result:
            result.append(rec)
    return result
