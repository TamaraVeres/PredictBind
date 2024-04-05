#!/usr/bin/env python3

import sys, subprocess
import Cli, P2Rank, Utils, Files, TSV

method, files, verbose, chimera, pymol, threads, evalpredict = Cli.cli()

def open_chimera_pymol(output_dir, file, chimera, pymol):
    if chimera == True:
        ch_out = subprocess.run(['which', 'chimera'], capture_output=True, text=True)
        ch_out = len(ch_out.stdout)
        if ch_out == 0:
            print("Chimera is not installed.")
            chimera = False
        else: 
            pdb = file[:-4]
            subprocess.run(['chimera', f'{output_dir}/visualizations/chimera_{pdb}.cmd'])
    if pymol == True:
        py_out = subprocess.run(['which', 'pymol'], capture_output=True, text=True)
        py_out = len(py_out.stdout)
        if py_out == 0:
            print("Pymol is not installed.")
            pymol = False
        else: 
            subprocess.run(['pymol', f'{output_dir}/visualizations/{file}.pml'])

def process_one_file(file_with_DOT_PDB, chimera, pymol, verbose):
    file = file_with_DOT_PDB
    output_dir = P2Rank.rank(file, threads, eval = evalpredict, verbose = verbose)
    if output_dir == None:
        return None
    predictions_csv_path, out_dir, pdb, list_of_pocket_objects = Utils.create_pdb_cmd_file_and_set_residue_types(output_dir, file)
    if len(list_of_pocket_objects) == 0:
        print('NO P2POCKETS PREDICTED, REMOVING FILES.', file=sys.stderr)
        subprocess.run(['rm', '-r', output_dir])
    else:
        TSV.to_tsv(predictions_csv_path, out_dir, pdb, list_of_pocket_objects)
        print(f"Output stored in: {output_dir}", file=sys.stderr)
        if chimera == True or pymol == True:
            open_chimera_pymol(output_dir, file, chimera, pymol)

# If we process only one file
if method == 'FILE':
    files_to_go = Files.single(files)
    process_one_file(files_to_go, chimera, pymol, verbose)

# If we process a directory
if method == 'DIRECTORY':
    files_to_go = Files.directory(files) 
    for file in files_to_go:
        process_one_file(file, chimera=False, pymol=False, verbose=verbose)

# If we process multiple files
if method == 'FILES':
    files_to_go = Files.multiple(files, verbose)
    for file in files_to_go:
        process_one_file(file, chimera=False, pymol=False, verbose=verbose)
