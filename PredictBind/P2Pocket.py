import re

class Pocket():

    def keep_numbers(self, string):
        return int(re.sub(r'\D', '', string))

    def res_ids_to_dict(self, residue_ids):
        chain_ids = residue_ids.split(' ')
        chain_dict = {}
        while '' in chain_ids:
            chain_ids.remove('')
        for entry in chain_ids:
            chain, id = entry.split("_")
            if chain not in chain_dict:
                chain_dict[chain] = []
            chain_dict[chain].append(self.keep_numbers(id))
        return chain_dict

    def surface_atoms_to_list(self, surface_atom_ids):
        surface_atoms = surface_atom_ids.split(' ')
        surface_atoms_int_list = []
        for atom in surface_atoms:
            surface_atoms_int_list.append(int(atom))
        return(surface_atoms_int_list)
    
    def residue_names_to_type(self, residue_names_dict):
            # 'N' represents non-polar amino acids
            # 'P' represents polar amino acids
            # '+' represents positively charged amino acids
            # '-' represents negatively charged amino acids

        aa_to_type = {'ALA': 'N', 'CYS': 'N', 'ASP': '-', 'GLU': '-', 'PHE': 'N', 'GLY': 'N',
                      'HIS': '+', 'ILE': 'N', 'LYS': '+', 'LEU': 'N', 'MET': 'N', 'ASN': 'P',
                      'PRO': 'N', 'GLN': 'P', 'ARG': '+', 'SER': 'P', 'THR': 'P', 'VAL': 'N',
                      'TRP': 'N', 'TYR': 'N', 'PYL': 'N', 'SEC': 'N', 'DAL': 'N', 'DSN': 'P',
                      'DCY': 'N', 'DPR': 'N', 'DVA': 'N', 'DTH': 'P', 'DLE': 'N', 'DIL': 'N',
                      'DSG': 'P', 'DAS': '-', 'MED': 'N', 'DGN': 'P', 'DGL': '-', 'DLY': '+',
                      'DHI': '+', 'DPN': 'N', 'DAR': '+', 'DTY': 'N', 'DTR': 'N', 'MSE': 'P'
                      }
        
        residue_type_dict = {}
        for chain in residue_names_dict:
            residue_type_dict[chain] = []
            for name in residue_names_dict[chain]:
                try: 
                    residue_type_dict[chain].append(aa_to_type[name])
                except:
                    residue_type_dict[chain].append('0')
        return residue_type_dict

    def __init__(self, name, rank, score, probability, 
                 sas_points, surface_atoms, center_x, center_y, 
                 center_z, residue_ids, surface_atom_ids) -> None:
        self.__name = name
        self.__rank = rank
        self.__score = score
        self.__probability = probability
        self.__sas_points =sas_points
        self.__surface_atoms = surface_atoms
        self.__center_x = center_x
        self.__center_y = center_y
        self.__center_z = center_z
        self.__residue_ids = self.res_ids_to_dict(residue_ids)
        self.__surface_atom_ids = self.surface_atoms_to_list(surface_atom_ids)

    def set_residue_names(self, residue_names_dict):
        self.__residue_names = residue_names_dict
        self.__residue_type = self.residue_names_to_type(residue_names_dict)

    def get_residue_names(self):
        return self.__residue_names
    
    def get_residue_type(self):
        return self.__residue_type

    def get_name(self):
        return self.__name
    
    def get_rank(self):
        return self.__rank
    
    def get_score(self):
        return self.__score
    
    def get_probability(self):
        return self.__probability
    
    def get_sas_points(self):
        return self.__sas_points
    
    def get_surface_atoms(self):
        return self.__surface_atoms
    
    def get_center_x(self):
        return self.__center_x

    def get_center_y(self):
        return self.__center_y
    
    def get_center_z(self):
        return self.__center_z

    def get_residue_ids(self):
        return self.__residue_ids

    def get_atom_ids(self):
        return self.__surface_atom_ids

    def __str__(self) -> str:
        return self.__name

def get_pocket_objects(filename):

    i = 0
    pockets = []

    with open(filename, 'r') as file:
        for line in file:
            i+=1
            if i == 1: continue
            pocket = line.replace('\t','').replace('\n','').split(',')
            pocket = [ent.strip() for ent in pocket]
            pockets.append(pocket)

    pocket_objects = []
    
    for pocket in pockets:
        pocket_objects.append(Pocket(pocket[0], pocket[1], pocket[2], 
                                            pocket[3], pocket[4], pocket[5], 
                                            pocket[6], pocket[7], pocket[8],
                                            pocket[9], pocket[10]))

    return pocket_objects
