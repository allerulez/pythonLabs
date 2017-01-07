#Anton Gefvert antge210, Aleksi Evansson aleev379
#5. Språk
#Uppgift 5a

"""
vikho: 6/11: Ok!
Ser mycket bättre ut nu, inga speciella anmärkningar förutom att ni kanske har
lite långa varibelnamn (i min mening). sthm istället för statement och vars
istället för variables skulle göra koden lite mera kompakt och lättare att läsa
då det blir större skillnader mellan parametrar och funktionsnamn.
"""

from calc import *


def handle_statements(statements, variables):
	""" Takes a list of statements and executes them in order. """
	if isstatements(statements):
		variables = statement_type(first_statement(statements), variables)
		return handle_statements(rest_statements(statements), variables)
	elif empty_statements(statements):
		return variables
	else:
		raise Exception("Invalid statement")

def statement_type(statement, variables):
	""" Takes a statement and executes the corresponding function. """
	if isassignment(statement):
		variables = assign(statement, variables)
	elif isrepetition(statement):
		variables = repeat(statement, variables)
	elif isselection(statement):
		variables = select(statement, variables)
	elif isinput(statement):
		variables = read(statement, variables)
	elif isoutput(statement):
		write(statement, variables)
	elif isbinary(statement):
		calculate(statement, variables)
	elif iscondition(statement):
		logic(statement, variables)
	return variables


def assign(statement, variables):
	""" Assigns a value to a variable in 'variables'. """
	variables[assignment_variable(statement)] = calculate(assignment_expression(statement), variables)
	return variables


def repeat(statement, variables):
	""" Loops through statements while the condition is met. """
	while logic(repetition_condition(statement),variables):
		variables = handle_statements(repetition_statements(statement), variables)
	return variables

def select(statement, variables):
	""" Checks a logical statement and executes true/false statements"""
	if logic(selection_condition(statement), variables):
		return handle_statements([selection_true(statement)], variables)
	elif hasfalse(statement):
		return handle_statements([selection_false(statement)], variables)


def read(statement, variables):
	""" Takes input and saves it in a variable """
	inputvar = input("Enter value for " + input_variable(statement) + ": ")
	variables[input_variable(statement)] = int(inputvar)
	return variables


def write(statement, variables):
	""" Takes a variable and outputs it """
	var = output_variable(statement)
	printstr = var + " = " + str(variables[var])
	print(printstr)


def calculate(statement, variables):
	""" Executes basic arithmetic operations """
	if isinstance(statement, int):
		return statement
	else:
		if isinstance(binary_left(statement), str):
			left = variables[binary_left(statement)]
		else:
			left = calculate(binary_left(statement), variables)

		if isinstance(binary_right(statement), str):
			right = variables[binary_right(statement)]
		else:
			right = calculate(binary_right(statement), variables)

		if binary_operator(statement) == "+":
			return left + right
		elif binary_operator(statement) == "-":
			return left - right
		elif binary_operator(statement) == "/":
			return left / right
		elif binary_operator(statement) == "*":
			return left * right

def logic(statement, variables):
	""" Executes a logical statement and returns the result """
	if isinstance(condition_left(statement), str):
		left = variables[condition_left(statement)]
	else:
		left = calculate(condition_left(statement),variables)

	if isinstance(condition_right(statement), str):
		right = variables[condition_right(statement)]
	else:
		right = calculate(condition_right(statement),variables)

	if condition_operator(statement) == "<":
		return left < right
	elif condition_operator(statement) == ">":
		return left > right
	elif condition_operator(statement) == "=":
		return left == right

def eval_calc(calc):
	""" Executes the given Calc-program """
	if isprogram(calc):
		handle_statements(program_statements(calc),{})
	else:
		raise Exception("Invalid program")



fibonacci = ['calc', 
				['read', 'n_in_fibo'],
				['set', 'res', 1],
				['set', 'prev', 0],
				['set', 'temp', 0],
				['set', 'i', 0],
				['while', [['n_in_fibo', '-', 1], '>', 'i'],
					['set', 'temp', ['res', '*', 1]],
					['set', 'res' , ['res', '+', 'prev']],
					['set', 'prev', ['temp', '*', 1]],
					['set', 'i', ['i', '+', 1]]],
				['print', 'res']
				]

sum_of_n_numbers = ['calc',
						['read', 'sum_to_n'],
						['set', 'sum', 0],
						['while', ['sum_to_n', '>', 0],
							['set', 'sum', ['sum', '+', 'sum_to_n']],
							['set', 'sum_to_n', ['sum_to_n', '-', 1]]],
						['print', 'sum']]

biggest_value = 	['calc',
						['read', 'n'],
						['read', 'm'],
						['set', 'k', 1337],
						['if', ['n', '>', 'm'], 
							['print', 'n'], 
							['if', ['n', '=', 'm'],
							['print', 'k'],['print', 'm']]]]
division = 			['calc',
						['read', 't'],
						['read', 'n'],
						['set', 'res', ['t', '/', 'n']],
						['print', 'res']]

if __name__  == "__main__":
	eval_calc(fibonacci)
	eval_calc(sum_of_n_numbers)
	eval_calc(biggest_value)
	eval_calc(division)