import sys, os, subprocess

def rank(pdb_file, threads, eval = False, verbose = False):

    # Get the pdb file ID
    print(f'PBFT file: {pdb_file}')
    pdb_dir = "predict_" + os.path.basename(pdb_file).replace('.pdb', '')
    
    if not threads.isdigit() or int(threads) < 1 or int(threads) > 16:
        threads = 1

    # Exit if dir exists
    print(os.path.abspath(pdb_dir))
    if os.path.isdir(os.path.abspath(pdb_dir)):
        print(f"Directory {pdb_dir} already exits. Please change it's name or move it to continue.")
        return None

    # Running analysis
    print(f"Analysing {pdb_file} structure...", file=sys.stderr)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Check if the mode is predict or eval-predict
    mode = 'predict'
    if eval:
        mode = 'eval-predict'
        
    command = [f'{dir_path}/training_data/prank', mode, '-f', pdb_file, '-t', threads]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        print(f'{output}\n')
    except subprocess.CalledProcessError as e:
        if verbose:
            import traceback
            traceback.print_exc()
        else:
            print("An error occurred during subprocess execution. Please check the command and try again.", file=sys.stderr)
        return None

    # If the file is taken to a subfolder, 
    # making the neccessary changes
    if '/' in pdb_file:
        pdb_file = pdb_file.split("/")[-1]

    # Removing temp directories
    print("Removing temporary directories", file=sys.stderr)

    # Getting created directory
    dir_line = output.splitlines()[7]
    dir_start = dir_line.find('[') + 1
    dir_end = dir_line.find(']')
    directory_of_prediction = dir_line[dir_start:dir_end]

    # Removing uneccesarry files
    rm_unn = ['rm', f'{directory_of_prediction}/{pdb_file}_residues.csv', 
            f'{directory_of_prediction}/params.txt', 
            f'{directory_of_prediction}/run.log']
    subprocess.run(rm_unn)

    # Moving to current directory
    mv_cmd = ['mv', directory_of_prediction, './']
    subprocess.run(mv_cmd)

    # Removing the test_directory of the main folder
    test_output_dir_loc = directory_of_prediction.find('test_output/') + 12
    test_output_dir = directory_of_prediction[:test_output_dir_loc]
    rm_cmd = ['rm', '-r', test_output_dir]
    subprocess.run(rm_cmd)

    # Returning the full path of the output folder
    output_dir = os.path.abspath(f"./predict_{pdb_file.replace('.pdb','')}/")
    return output_dir