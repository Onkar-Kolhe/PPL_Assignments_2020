(terpri)
(princ "Program to return nth element of the list")
(terpri)
(princ "Enter the list with parenthesis:")
(setq l (read))
(princ "Enter the value of n: ")
(setq n (read))
(princ "The element is: ")
(write (car (nthcdr (decf n 1) l)))


