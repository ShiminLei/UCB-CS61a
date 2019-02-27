test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)   ; True or False
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 9)   ; True or False
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 6)   ; True or False
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
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
