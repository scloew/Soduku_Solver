from collections import namedtuple

_Status = namedtuple('_Status', ['no_change', 'options_update', 'value_set',
                                 'group_updated', 'puzzle_error_found', 'solved'])

status = _Status('no_change', 'options_update', 'value_set', 'group_updated', 'puzzle_error_found', 'solved')
