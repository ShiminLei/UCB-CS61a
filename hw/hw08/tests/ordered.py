test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))  ; True or False
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))  ; True or False
          3cbee9249bf6c5fe6fce86debf3b010a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))  ; True or False
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))  ; True or False
          3cbee9249bf6c5fe6fce86debf3b010a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
