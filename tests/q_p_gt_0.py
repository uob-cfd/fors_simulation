
test = {
  'name': 'Question p_gt_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_gt_0'
          >>> 'p_gt_0' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_gt_0'
          >>> # from its initial state (of ...)
          >>> p_gt_0 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_gt_0 should be a proportion.
          >>> 0 <= p_gt_0 <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Look at the difference values in the notebook.
          >>> # How many are negative or 0?
          >>> p_gt_0 == 1
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
