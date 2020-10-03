
test = {
  'name': 'Question total1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You will need to define a "total1" variable.
          >>> 'total1' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Oops - did you accidentally include 13?
          >>> total1 != 91
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Not there yet...
          >>> total1 == 78
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
