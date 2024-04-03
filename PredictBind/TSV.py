import subprocess, sys

def to_tsv(predictions_csv_path, out_dir, pdb, pocket_objects):
    subprocess.run(['rm', predictions_csv_path])

    print('Creating TSV file', file=sys.stderr)

    file = open(f'{out_dir}/{pdb}.pdb_predictions.tsv', 'w')
    file.write('name\trank\tscore\tprobability\tsas_points\tsurf_atoms\tcenter_x\tcenter_y\tcenter_z\tresidue_ids\tresidue_names\tresidue_types\tsurf_atom_ids\n')

    for pocket in pocket_objects:
        name = pocket.get_name()
        rank = pocket.get_rank()
        score = pocket.get_score()
        probability = pocket.get_probability()
        sas_points = pocket.get_sas_points()
        surf_atoms = pocket.get_surface_atoms()
        center_x = pocket.get_center_x()
        center_y = pocket.get_center_y()
        center_z = pocket.get_center_z()
        residue_ids = str(pocket.get_residue_ids())
        residue_names = str(pocket.get_residue_names())
        residue_types = str(pocket.get_residue_type())
        surf_atom_ids = str(pocket.get_atom_ids())

        line = [name, rank, score, probability, sas_points, surf_atoms, 
                center_x, center_y, center_z, residue_ids, residue_names, 
                residue_types, surf_atom_ids]
        
        line = "\t".join(line) + '\n'
        file.write(line)

    # file.write('\n')
    file.close()