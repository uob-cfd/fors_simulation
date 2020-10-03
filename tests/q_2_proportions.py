test = {
  'name': 'Question 2_proportions',
  'points': 1,
  'suites': [
    {
      # res = np.random.randint(0, 2, size=(10000000, 82))
      # means = res.mean(axis=1)
      # np.min(means), np.max(means)
      'cases': [
        {
          'code': r"""
          >>> # Proportions should be an array.
          >>> isinstance(proportions, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'proportions'
          >>> # from its initial state (of an array of zeros).
          >>> np.all(proportions == 0)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # proportions should have 10000 values.
          >>> len(proportions) == 10000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # All values in proportions should be in this range.
          >>> np.all(proportions > 0.219)
          True
          >>> np.all(proportions < 0.781)
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
