length_func = lambda x: len(x)
chain = prompt | length_func | output_parser
