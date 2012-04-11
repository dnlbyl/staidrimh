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
    units = _normalize_newlines(px).split(';')
    def tok_px(x): return x.split('=')
    units = map(tok_px, units)
    
    def filter_empties(x): return len(x) > 1
    units = filter(filter_empties, units)
    
    print units
    return units
    
## {{{ http://code.activestate.com/recipes/435882/ (r1)
def _normalize_newlines(string):
    import re
    # use pipe for future convenience
    return re.sub(r'(\r\n|\r|\n)', '|', string)
## end of http://code.activestate.com/recipes/435882/ }}}

def _px_to_csv(px):
    """
    Extracts the relevant parts of the px data and builds a csv formated version
    """
    

    
    
def px_to_csv(px):
    """
    Converts the provided text in px format to csv text.
    """
    if not verify_cx_text(px):
        # TODO raise exception
    data = flatten_px(px)
    
    
    return px

