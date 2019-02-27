test = {
  'name': 'add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add odds 2)
          0fafc98a97c0c2ec1f5a633f3687f2f3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 5)
          9620ecf82d823002be27d832ece9da20
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 6)
          fe23c2388f24f36595658a14bab1a219
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 10)
          5f5aabcf061148d704c0db8c5c2d8613
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
