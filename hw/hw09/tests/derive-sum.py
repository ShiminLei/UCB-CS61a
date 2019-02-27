test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          afe11f721da99d6cc29c38c6c9f996cb
          # locked
          scm> (make-sum 'x 0)
          b07308dadf589c670387415df24205dc
          # locked
          scm> (make-sum 0 'x)
          b07308dadf589c670387415df24205dc
          # locked
          scm> (make-sum 'a 'x)
          572a031a195b58555c6c8306c459f8ab
          # locked
          scm> (make-sum 'a (make-sum 'x 1))
          d16a9cdb6c616b9f5c7e4d91aa44e203
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
          scm> (derive '(+ x 3) 'x)
          d7ab3c9f4f7487833d3cb935fc8c712a
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
    }
  ]
}
