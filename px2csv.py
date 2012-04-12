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

    def tok_px(x):
        return x.split('=', 1)
    units = map(tok_px, units)

    def filter_empties(x):
        return len(x) > 1
    units = filter(filter_empties, units)

    units = [(x[0].strip('|'), x[1]) for x in units]

    return units


## {{{ http://code.activestate.com/recipes/435882/ (r1)
def _normalize_newlines(string):
    import re
    # use pipe for future convenience
    return re.sub(r'(\r\n|\r|\n)', '|', string)
## end of http://code.activestate.com/recipes/435882/ }}}


def _px_data_to_csv(px_data):
    """
    Extracts the relevant parts of the px data
    and builds a csv formated version
    """
    def find_data(x):
        return x[0].startswith("VALUES") or x[0].startswith("DATA")
    data_parts = filter(find_data, px_data)

    import re
    row_headings = re.split('[|,]', data_parts[0][1].replace(',|', ','))
    column_headings = data_parts[1][1]
    data_rows = data_parts[2][1].split('|')

    csv = ',' + column_headings + ',\n'
    for x,y in zip(row_headings,data_rows):
        csv += x + ',' + y.replace(' ', ',') + '\n'

    return csv


def px_to_csv(px):
    """
    Converts the provided text in px format to csv text.
    """
    #if not verify_cx_text(px):
        # TODO raise exception

    return _px_data_to_csv(flatten_px(px))

import sys


def main():
    px_file = open(sys.argv[1])
    csv = px_to_csv(px_file.read())
    print csv

if __name__ == '__main__':
    main()
