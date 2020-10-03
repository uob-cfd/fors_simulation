
test = {
  'name': 'Question m_to_all_ratio',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'm_to_all_ratio'
          >>> 'm_to_all_ratio' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'm_to_all_ratio'
          >>> # from its initial state (of ...)
          >>> m_to_all_ratio is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There were more boys born than girls.
          >>> m_to_all_ratio > 0.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.5161 < m_to_all_ratio < 0.51615
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
