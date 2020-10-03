
test = {
  'name': 'Question mean_easy',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'mean_easy'
          >>> 'mean_easy' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mean_easy'
          >>> # from its initial state (of ...)
          >>> mean_easy is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Ooh - close - but - is the starting value for "total" correct?
          >>> mean_easy < 3.7
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Not quite there.
          >>> 3.6073 < mean_easy < 3.6074
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
