# salary
to calculate your salary with discount (Brazilian taxes)


'''
I ran into an error that I can't solve, on line 12 :
sbruto = htworked + hextra * (1 + (hovertime / 100)) * vhour
where the main calculation of the equation should happen, I get a return like this:
TypeError: unsupported operand type(s) for /: 'type' and 'int'
'''
pull with solution accepted as long as it contains a description of what happened



the end result should look something like this
Let's take the following values for data entry as an example: hours worked = 20, overtime = 5, and hour value = 10.
worked = 20, overtime = 5, and hourly rate = 10.
in the expression for calculating the gross wage, we will have
sbruto <- (20 + 5*(1+(100/100)))*10
			    (20 + 5*(1+(1)))*10
				  (20 + 5* 2)*10
					(20 + 10)*10
					30*10
					300
