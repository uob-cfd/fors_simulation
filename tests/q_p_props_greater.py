
test = {
  'name': 'Question p_props_greater',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_props_greater'
          >>> 'p_props_greater' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_props_greater'
          >>> # from its initial state (of ...)
          >>> p_props_greater is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_props_greater should be a proportion.
          >>> 0 <= p_props_greater <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The chances are very very low
          >>> p_props_greater < 0.00001
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
