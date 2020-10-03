test = {
  'name': 'Question outcome_ideal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'likely_outcome_from_ideal'
          >>> 'likely_outcome_from_ideal' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'likely_outcome_from_ideal'
          >>> # from its initial state (of ...)
          >>> likely_outcome_from_ideal is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Value should be from 1 through 5.
          >>> 1 <= likely_outcome_from_ideal <= 5
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
