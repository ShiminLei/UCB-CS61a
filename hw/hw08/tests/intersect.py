test = {
  'name': 'intersect',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (intersect odds (list 2 3 4 5))
          7638e8948ede5d3e77ed8398cd51d78b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds (list 2 4 6 8))  ; Empty list is ()
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds eight)
          7af7860867135d752bc977360f3c6558
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
