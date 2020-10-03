
test = {
  'name': 'Question differences',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to make a column called 'Difference'
          >>> 'Difference' in list(christenings)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first two values should be 532 and 401
          >>> christenings.loc[0, 'Difference'] == 535
          True
          >>> christenings.loc[1, 'Difference'] == 401
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Nearly there ..
          >>> np.sum(christenings['Difference']) == 30224
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
