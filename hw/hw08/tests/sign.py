test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          56dd53120ef1986c202a7ccf82080809
          # locked
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          56dd53120ef1986c202a7ccf82080809
          # locked
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          fd2f1e10fd8310f4d5b75ff1f88e0e4e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign -42)
          def5a8c3e39d76dfbcb66189bf0d3593
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          5ca79ce4fb57688138ae494e7845eb74
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          38dac9033a8f5e8edb2dbe6428e02d1d
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
