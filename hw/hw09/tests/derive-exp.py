test = {
  'name': 'derive-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (derive x^2 'x) ; Remember products have the form (* a b)
          ed0ffff90522b09570d873b1ec1b4225
          # locked
          scm> (derive x^3 'x)
          fcf23446ee786acb4b3760d66467ff0f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (derive (make-sum x^3 x^2) 'x)
          (+ (* 3 (^ x 2)) (* 2 x))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
