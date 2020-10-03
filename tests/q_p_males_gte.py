test = {
  'name': 'Question p_males_gte',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_males_gte'
          >>> 'p_males_gte' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_males_gte'
          >>> # from its initial state (of ...)
          >>> p_males_gte is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_males_gte should be a proportion
          >>> 0 <= p_males_gte <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The proportion will be small
          >>> 0 <= p_males_gte <= 0.001
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Really small
          >>> 0 <= p_males_gte <= 0.00001
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
