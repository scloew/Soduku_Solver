from collections import namedtuple

_Status = namedtuple('_Status', ['no_change', 'options_update', 'value_set', 'puzzle_error_found'])

cell_status = _Status(0, 1, 2, -1)
