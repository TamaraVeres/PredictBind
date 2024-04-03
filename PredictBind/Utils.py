import os, sys
import P2Pocket

def pdb_dict_from_pdb_file(out_dir, pdb):
    if pdb.endswith('.pdb'):
        pdb = pdb[:-4]
    if '/' in pdb:
        pdb = str(pdb.split('/')[-1])

    filename = f'{out_dir}/visualizations/data/{pdb}.pdb'
    
    pdb_dict = {}
    
    with open(filename, 'r') as file:
        for line in file:
            if (line.startswith('ATOM') or line.startswith('HETATM')) and "HOH" not in line:
                
                chain_id = line[21]
                if chain_id == ' ': 
                    chain_id = ''
                residue_num = int(line[22:26])
                residue_name = line[17:20].strip()

                if chain_id not in pdb_dict:
                    pdb_dict[chain_id] = {}

                pdb_dict[chain_id][residue_num] = residue_name

    return pdb_dict

def create_pdb_cmd_file_and_set_residue_types(out_dir, pdb):
    if pdb.endswith('.pdb'):
        pdb = pdb[:-4]
    if '/' in pdb:
        pdb = str(pdb.split('/')[-1])

    filename = f'{out_dir}/visualizations/data/{pdb}.pdb'
    pdb_dict = pdb_dict_from_pdb_file(out_dir, pdb)
    out_cmd_file = f'{out_dir}/visualizations/chimera_{pdb}.cmd'
    file = open(out_cmd_file, 'w')

    colors = ['red', 'orange', 'yellow', 'green', 'cyan', 
            'blue', 'medium blue', 'purple', 'hot pink', 
            'magenta', 'white', 'gray', 'black', 'tan',
            'slate gray', 'magenta', 'plum', 'rosy brown']
    color = 0

    list_of_pocket_objects = P2Pocket.get_pocket_objects(filename = f'{out_dir}/{pdb}.pdb_predictions.csv')
    predictions_csv_path = os.path.abspath(f'{out_dir}/{pdb}.pdb_predictions.csv')

    absolute_path = os.path.abspath(filename)
    file.write(f'open {absolute_path}\n')

    print("Creating visualization files", file=sys.stderr)

    for pocket in list_of_pocket_objects:
        residue_names_dict = {}
        pocket_dict = pocket.get_residue_ids()
        selection = ''
        for chain in pocket_dict:
            residue_names_dict[chain] = []
            for residue_num in pocket_dict[chain]:
                selection += f'{residue_num}.{str(chain).lower()},'
                residue_names_dict[chain].append(pdb_dict[chain][residue_num])
        
        selection = selection[:-1]

        file.write(f'select :{selection}\n')
        if color < len(colors):
            file.write(f'color {colors[color]} :{selection}\n')
        elif color == len(colors):
            print(f'Exceded number of colors. Pockets higher than {len(colors)} will be saved as a selections ONLY, and will not be colored.', file=sys.stderr)
        file.write(f'namesel {pocket.get_name()}\n')
        pocket.set_residue_names(residue_names_dict)
        color += 1

    file.write('select\nsurface\n')
    file.close()
    
    return predictions_csv_path, out_dir, pdb, list_of_pocket_objects
