(terpri)
(princ "Program to calculate factorial of a number recursively and then display it.")
(terpri)
(princ "Enter the number: ")
(setq n (read))

(defun fac(num)
	(cond ((>= num 1)
		(* num (fac (decf num 1))))
		(1)
	)
)

(princ "The result is: ")
(write (fac n))


