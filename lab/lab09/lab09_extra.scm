;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (list 1) 2 '(3 . 4) 5)
)

; Q6
(define (composed f g)
   (lambda (x)(f (g x)))
)

; Q7
(define (remove item lst)
    (cond ((null? lst) '())
         (( = item (car lst )) ( remove item (cdr lst)))
         (else (cons (car lst) (remove item (cdr lst)))))
)
;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)



; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
    (if (or (= a 0) (= b 0))
        (max a b)
      (if (= (modulo (max a b) (min a b)) 0)
        (min a b)
        (gcd (min a b) (remainder (max a b) (min a b)))
        )
    )
)
;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (in-lst s x)
  (if (null? s)
     #f
     (or (= x (car s)) (in-lst (cdr s) x))))
(define (no-repeats s)
  (if (null? s)
        s
        (if (in-lst (cdr s) (car s))
            (no-repeats (cdr s))
            (cons (car s) (no-repeats (cdr s))))))

; Q10
(define (substitute s old new)
   (cond
   ((null? s) s)
   ((pair? (car s)) (cons (substitute (car s) old new)
                          (substitute (cdr s) old new)))
   ((equal? (car s) old) (cons new (substitute (cdr s) old new)))
   (else (cons (car s) (substitute (cdr s) old new))
  )
)
)

; Q11
(define (sub-all s olds news)
   (cond
    ((null? olds) s)
    (else (sub-all
            (substitute
              s
              (car olds)
              (car news))
            (cdr olds)
            (cdr news)))
  )
)