test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3))
          023f53b43f605b7580be5aa5c3e5ee7e
          # locked
          scm> (how-many-dots '(1 2 . 3))
          d7ab3c9f4f7487833d3cb935fc8c712a
          # locked
          scm> (how-many-dots '((1 . 2) 3 . 4))
          3940351fe1ecdc23ea60a8fdad9aa11d
          # locked
          scm> (how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
          17c904758d7c0462b49135eebe9c3ca4
          # locked
          scm> (how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
          023f53b43f605b7580be5aa5c3e5ee7e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
