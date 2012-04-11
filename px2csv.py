"""
 Converts px-axis formatted files to csv.
"""

def verify_cx_text(cx_text):
    """
    Checks that the provided text is cc-axis formated.
    Returns true if it is cx text, otherwise false.
    TODO The pc-axis format probably has several other things that should be checked.
    """
    if not isinstance(cx_text, basestring):
        return False
    return cx_text.startswith('AXIS-VERSION="2000"')
        

def px_to_csv(self, px):
    """
    Converts the provided text in px format to csv text.
    """
    return px

