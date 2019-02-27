test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          5b7ac87ccebc8b42d86dfe269dcf89e7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          2252870f2a5c1955c880d5162a566d4f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          9745228a0aa06e7508a35823c92bac86
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          99664260ecd386c62f28106482facddd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          99664260ecd386c62f28106482facddd
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
