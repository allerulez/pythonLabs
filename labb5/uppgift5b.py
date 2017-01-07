from calc import *


def handle_statements(statements, file_str):
	""" Takes a list of statements and executes them in order. """
	if isstatements(statements):
		file_str = statement_type(first_statement(statements), file_str)
		return handle_statements(rest_statements(statements), file_str)
	elif empty_statements(statements):
		return file_str
	else:
		raise Exception("Invalid statement")

def statement_type(statement, file_str):
	""" Takes a statement and executes the corresponding function. """
	if isassignment(statement):
		file_str = assign(statement, file_str)
	elif isrepetition(statement):
		file_str = repeat(statement, file_str)
	elif isselection(statement):
		file_str = select(statement, file_str)
	elif isinput(statement):
		file_str = read(statement, file_str)
	elif isoutput(statement):
		write(statement, file_str)
	elif isbinary(statement):
		calculate(statement, file_str)
	elif iscondition(statement):
		logic(statement, file_str)
	return file_str


def assign(statement, file_str):
	""" Assigns a value to a variable in 'file_str'. """
	statement_str = "varables[" + assignment_variable(statement) + "] = " +	calculate(assignment_expression(statement)) + "\n"
	file_str += statement_str
	return file_str


def repeat(statement, file_str):
	""" Loops through statements while the condition is met. """
	#while logic(repetition_condition(statement),file_str):
	
	file_str = handle_statements(repetition_statements(statement), file_str)
	return file_str

def select(statement, file_str):
	""" Checks a logical statement and executes true/false statements"""
	if logic(selection_condition(statement), file_str):
		return handle_statements([selection_true(statement)], file_str)
	elif hasfalse(statement):
		return handle_statements([selection_false(statement)], file_str)


def read(statement, file_str):
	""" Takes input and saves it in a variable """
	inputvar = input("Enter value for " + input_variable(statement) + ": ")
	file_str[input_variable(statement)] = int(inputvar)
	return file_str


def write(statement, file_str):
	""" Takes a variable and outputs it """
	var = output_variable(statement)
	printstr = var + " = " + str(file_str[var])
	print(printstr)


def calculate(statement):
	""" Executes basic arithmetic operations """
	if isinstance(statement, int):
		return statement
	else:
		if isinstance(binary_left(statement), str):
			left = file_str[binary_left(statement)]
		else:
			left = calculate(binary_left(statement), file_str)

		if isinstance(binary_right(statement), str):
			right = file_str[binary_right(statement)]
		else:
			right = calculate(binary_right(statement), file_str)

		if binary_operator(statement) == "+":
			return left + right
		elif binary_operator(statement) == "-":
			return left - right
		elif binary_operator(statement) == "/":
			return left / right
		elif binary_operator(statement) == "*":
			return left * right

def logic(statement, file_str):
	""" Executes a logical statement and returns the result """
	if isinstance(condition_left(statement), str):
		left = file_str[condition_left(statement)]
	else:
		left = calculate(condition_left(statement),file_str)

	if isinstance(condition_right(statement), str):
		right = file_str[condition_right(statement)]
	else:
		right = calculate(condition_right(statement),file_str)

	if condition_operator(statement) == "<":
		return left < right
	elif condition_operator(statement) == ">":
		return left > right
	elif condition_operator(statement) == "=":
		return left == right

def eval_calc(calc):
	""" Executes the given Calc-program """
	if isprogram(calc):
		temp_file = open("calc_prog.py", "w")
		file_str = "variables = {}\n"
		file_str = handle_statements(program_statements(calc), file_str)
		print(file_str, file = temp_file)
		temp_file.close()
	else:
		raise Exception("Invalid program")