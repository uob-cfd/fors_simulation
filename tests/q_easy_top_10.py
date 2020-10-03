test = {
  'name': 'Question easy_top_10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'easy_top_10'
          >>> 'easy_top_10' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'easy_top_10'
          >>> # from its initial state (of ...)
          >>> easy_top_10 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should be a data frame
          >>> isinstance(easy_top_10, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should have 10 rows.
          >>> len(easy_top_10) == 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # easy_top_10 should be sorted, easiest first.
          >>> all_easy = np.sort(courses['Easiness'])[::-1]
          >>> np.all(easy_top_10['Easiness'] == all_easy[:10])
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
