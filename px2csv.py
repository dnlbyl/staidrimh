"""
 Converts px-axis formatted files to csv.
"""

def verify_cx_text(px):
    """
    Checks that the provided text is cc-axis formated.
    Returns true if it is cx text, otherwise false.
    TODO The pc-axis format probably has several other things that should be checked.
    """
    if not px or not isinstance(px, basestring) or len(px) == 0:
        return False
    return px.startswith('AXIS-VERSION="2000"')
    
def flatten_px(px):
    """
    Parses the px text into a list of tuples, one for each data unit
    """
    
        

def px_to_csv(self, px):
    """
    Converts the provided text in px format to csv text.
    """
    
    return px

