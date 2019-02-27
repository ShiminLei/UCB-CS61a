test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          b508d9788e632b435080d8782722d95a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          400dd77941418602f756fd5494d75871
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds eight)
          cf2b660c05a45a5cad9c9bfb2077b35f
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
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
