def parse_problem_filename(filename):
    # Remove the file extension
    filename = filename.replace('.go', '')
    
    # Split the filename into problem number and problem name
    parts = filename.split('.')
    problem_number = parts[0]
    problem_name = parts[1].replace('-', ' ')
    return problem_number, problem_name
