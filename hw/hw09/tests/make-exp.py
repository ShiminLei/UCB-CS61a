test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          9ab8852f46fab7e7973763b21891fcca
          # locked
          scm> (make-exp 'x 1)
          b07308dadf589c670387415df24205dc
          # locked
          scm> (make-exp 'x 0)
          d7ab3c9f4f7487833d3cb935fc8c712a
          # locked
          scm> x^2
          b1a3364c3a1323efb9f954d772c3de34
          # locked
          scm> (base x^2)
          b07308dadf589c670387415df24205dc
          # locked
          scm> (exponent x^2)
          3940351fe1ecdc23ea60a8fdad9aa11d
          # locked
          scm> (exp? x^2) ; True or False
          7346f33f3682a13d51291338e62f5a0f
          # locked
          scm> (exp? 1)
          eb89d68eec1597c385d6e0ac3e3c6d52
          # locked
          scm> (exp? 'x)
          eb89d68eec1597c385d6e0ac3e3c6d52
          # locked
          """,
          'hidden': False,
          'locked': True
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
