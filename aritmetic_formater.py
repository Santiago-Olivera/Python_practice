'''
Enhanced version : 
'''
def arithmetic_arranger(problems, show_answers=False):
    # Error checking for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    second_operands = []
    operators = []
    dashes = []
    results = []

    for problem in problems:
        # Splitting problem into components
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        first_operand, operator, second_operand = parts

        # Validating operators
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Validating digits
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Validating operand length
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculating the space required for formatting
        width = max(len(first_operand), len(second_operand)) + 2
        first_operands.append(first_operand.rjust(width))
        second_operands.append(operator + ' ' + second_operand.rjust(width - 2))
        dashes.append('-' * width)

        # Calculating the result if needed
        if show_answers:
            result = str(eval(problem))  # Using eval for simplicity
            results.append(result.rjust(width))
    
    # Joining the components into formatted strings
    arranged_problems = (
        '    '.join(first_operands) + '\n' +
        '    '.join(second_operands) + '\n' +
        '    '.join(dashes)
    )
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)
    
    return arranged_problems

'''
def arithmetic_arranger(problems, show_answers=False):
    numerator = []
    denominator = []
    dashes = []
    result = []
    if len(problems) > 5:
       return  "Error: Too many problems."
    for problem in problems:
        if problem.find('+') != -1 :
            index = problem.find('+')
            a = problem[:index-1:]
            operand = '+'
            b = problem[index+2::]
            if not a.isdigit() or not b.isdigit():
                return 'Error: Numbers must only contain digits.'
            if len(a) > 4 or len(b) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            total_dashes = max(len(a),len(b))+2 
            result_to_append = str(int(a)+int(b))
            result.append(" "*(total_dashes-len(result_to_append))+result_to_append)
            if(len(a)>len(b)):
                b = ' '*(len(a)-len(b))+b
            else:
                a = ' '*(len(b)-len(a))+a
            a='  '+a
            numerator.append(a)
            denominator.append('+ '+b)
            dashes.append("-"*total_dashes)
            

        
        elif problem.find('-') != -1 :
            index = problem.find('-')
            a = problem[:index-1:]
            operand = '-'
            b = problem[index+2::]
            if not a.isdigit() or not b.isdigit():
                return 'Error: Numbers must only contain digits.'
            if len(a) > 4 or len(b) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            total_dashes = max(len(a),len(b))+2
            result_to_append = str(int(a)-int(b))
            result.append(" "*(total_dashes-len(result_to_append))+result_to_append)
            if(len(a)>len(b)):
                b = ' '*(len(a)-len(b))+b
            else:
                a = ' '*(len(b)-len(a))+a
            a='  '+a
            numerator.append(a)
            denominator.append('- '+b)
            dashes.append("-"*total_dashes)
            

        else:
            return "Error: Operator must be '+' or '-'."

    formated_join ='    '.join(numerator)+'\n'+'    '.join(denominator)+'\n'+'    '.join(dashes)
    if(show_answers):
        formated_join = formated_join+'\n'+'    '.join(result)
        return formated_join
    else:
        return formated_join

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
'''