test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          1a182ccdac5b512e78d2db0e7cd35aae
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          bec7b0c91bdcb548cda9e9f3546cf0d7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          400b880bd4ddd7622658a2c6ab1656de
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
