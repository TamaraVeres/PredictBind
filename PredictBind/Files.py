import sys, os

def single(files, verbose =  False):

    if len(files) == 4:
        if verbose:
            print(f'{files} given, attaching .pdb')
        files = files + '.pdb' # Check if extension not given, only ID
    if os.path.isfile(files):
        print(f'File found {files}', file=sys.stderr)
        return files
    else:
        print('File not found!', file=sys.stderr)
        sys.exit(1)

def directory(files, verbose = False):

    dir = files
    if not os.path.isdir(dir):
        print(f'{dir} is NOT a directory', file=sys.stderr)
        sys.exit(1)

    files = []
    for file in os.listdir(dir):
        if file.endswith('.pdb'):
            files.append(file)

    print(f'Directory: {os.path.abspath(dir)}', file=sys.stderr)
    if len(files) == 0:
        if verbose:
            print(f'There are no pdb files in {dir}. Make sure that the files have a ".pdb" extension.', file=sys.stderr)
        print(f'No .pdb file in {len(os.listdir(dir))} files of the given directory. Exiting...')
        sys.exit(1)
    else:
        if verbose:
            print(f'Scanned through {len(os.listdir(dir))} files, found {len(files)} .pdb files. Executing')
        print(f'Found files: {files}', file=sys.stderr)
        return files
    
def multiple(files, verbose = False):

    failed = []
    succeded = []

    for file in files: 

        if len(file) == 4:
            file = file + '.pdb'
        if os.path.isfile(file):
            succeded.append(file)
            if verbose == True:
                print(f'File found {file}', file=sys.stderr)
        else:
            failed.append(file)
            if verbose == True:
                print('File not found!', file=sys.stderr)

    print(f'Files found: {succeded} \
    \nFiles NOT found: {failed}', file=sys.stderr)

    if len(succeded) == 0:
        sys.exit(1)
    else:
        return succeded
