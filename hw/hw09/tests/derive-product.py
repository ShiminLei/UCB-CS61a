test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          17c904758d7c0462b49135eebe9c3ca4
          # locked
          scm> (make-product 'x 0)
          023f53b43f605b7580be5aa5c3e5ee7e
          # locked
          scm> (make-product 1 'x)
          b07308dadf589c670387415df24205dc
          # locked
          scm> (make-product 'a 'x)
          2cc941e3af1d094472c924e620661e57
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
