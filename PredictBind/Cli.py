import argparse
import sys

"""
    Defines the cli & args that can be passed to the python app
"""
def cli():

    parser = argparse.ArgumentParser(prog="PredictBind.py",
                                     description="""Use PredictBind.py to predict ligand binding sites of proteins from their .pdb files.""")

    parser.add_argument('-d', '--directory', metavar='{direcory_name}', help='Analyse all files located in one local directory.')
    parser.add_argument('-e', '--evalpredict', metavar='{file}.pdb', help='Path/to/pdb.')
    parser.add_argument('-f', '--file', metavar='{file}.pdb', help='Path/to/pdb.')
    parser.add_argument('-t', '--threads', metavar='{core_num}', help='Specify num. of working threads for parallel dataset processing')
    parser.add_argument('--files', nargs='*', metavar='{file1}.pdb {file2}.pdb', help='Analyse many local pdb files.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Get more detailed output of the process to the standard error.')
    parser.add_argument('-ch', '--chimera', action='store_true', help='Open with chimera immediately when file is ready to be visualised')
    parser.add_argument('-pm', '--pymol', action='store_true', help='Open with pymol when file is ready to be visualised')

    args = parser.parse_args()

    FILE = args.file
    DIRECTORY = args.directory
    FILES = args.files
    VERBOSE = args.verbose
    EVAL_PREDICT = args.evalpredict

    methods_chosen = 0
    method = ''

    if FILE:
        methods_chosen += 1
        method = 'FILE'
    if DIRECTORY:
        methods_chosen += 1
        method = 'DIRECTORY'
    if FILES:
        methods_chosen += 1
        method = 'FILES'

    if methods_chosen == 1:
        if VERBOSE:
            print(f'Selected method: {method.lower()}\
                \nSelected file(s): {FILES or FILE or DIRECTORY}\
                \nThreads: {args.threads}\
                \nVerbose: {args.verbose == True}\
                \nEval predictions: {args.evalpredict == True}\n', file=sys.stderr)
        if EVAL_PREDICT:
            evaluate = True
        else:
            evaluate = False
        if not args.threads.isdigit() or int(args.threads) < 1 or int(args.threads) > 16:
            args.threads = 1
        if method == 'FILE':
            return(method, args.file, args.verbose, args.chimera, args.pymol, args.threads, evaluate)
        elif method == 'DIRECTORY':
            return(method, args.directory, args.verbose, args.chimera, args.pymol, args.threads, evaluate)
        elif method == 'FILES':
            return(method, args.files, args.verbose, args.chimera, args.pymol, args.threads, evaluate)
    elif methods_chosen == 0:
        parser.print_help()
        print("""\nExamples:\n
        Cli.py -f 1gln.pdb
        Cli.py -d directory_name/ -t 8
        Cli.py --files 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  
        Cli.py --files 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  -t 8 -v
        """, file=sys.stderr)
        sys.exit(0)
    elif methods_chosen > 1:
        print("""\nError! Please choose ONLY ONE method! Examples:
        Cli.py -f 1gln.pdb
        Cli.py -d directory_name/ -t 8
        Cli.py --files 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  
        Cli.py --files 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  -t 8 -v
        """, file=sys.stderr)
        sys.exit(1)


