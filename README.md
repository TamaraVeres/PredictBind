
# PredictBind

PredictBind is a wrapper inspired and built around [P2Rank](https://github.com/rdk/p2rank/blob/develop/README.md).

## OS: Linux or Mac

This wrapper was written on an M1 mac and tested on UNIX systems.
Requires python3 and java(versions 8 to 20).

## Dependency check

```bash
python3 --version
java --version
```

Should return something like

```bash
Python 3.x.y
```

and

```bash
openjdk version "11.0.22" 2024-01-16
OpenJDK Runtime Environment Homebrew (build 11.0.22+0)
OpenJDK 64-Bit Server VM Homebrew (build 11.0.22+0, mixed mode)
```

# Installation

Make sure you have the listed dependencies and install binder with pip.

```bash
pip install PredictBind
```
  
# Commands

```bash
usage: PredictBind.py [-h] [-d {direcory_name}] [-e {file}.pdb] [-f {file}.pdb] [-t {core_num}]
                 [--files [{file1}.pdb {file2}.pdb ...]] [-v] [-ch] [-pm]

Use PredictBind.py to predict ligand binding sites of proteins from their .pdb files.

options:
  -h, --help            show this help message and exit
  -d {direcory_name}, --directory {direcory_name}
                        Analyse all files located in one local directory.
  -e {file}.pdb, --evalpredict {file}.pdb
                        Path/to/pdb.
  -f {file}.pdb, --file {file}.pdb
                        Path/to/pdb.
  -t {core_num}, --threads {core_num}
                        Specify num. of working threads for parallel dataset processing
  --files [{file1}.pdb {file2}.pdb ...]
                        Analyse many local pdb files.
  -v, --verbose         Get more detailed output of the process to the standard error.
  -ch, --chimera        Open with chimera immediately when file is ready to be visualised
  -pm, --pymol          Open with pymol when file is ready to be visualised
```

## Tutorials

TBD.

## Examples

### One PDB file

```bash
PredictBind.py -f 1gln.pdb 
```

### Dir

* If you have a directory of pdb files you want to analyse, run the --directory (-d) method:

```bash
PredictBind.py -d directory_name/
```

### Multiple files

```bash
PredictBind.py --files 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  
```

### Visualisation

The output can directly visualised with the --chimera (-ch) and --pymol (-pm) switch, given that you have them installed on your computer, by including the switch when running the comand. Note: this only woks for the single-file methods (-f); for the --directory and --local_many you need to open the visualisation cmd files manually (see: *Output* below).

Ex.

```bash
PredictBind.py -f 1gln.pdb -ch
```

# Output

A prediction for a file ```{pdb}.pdb``` will create the following structure in the folder in which PredictBind.py was executed.

```folder
predict_{pdb}/
├── {pdb}.pdb_predictions.tsv
└── visualizations/
    ├── chimera_{pdb}.cmd
    ├── {pdb}.pdb.pml
    └── data/
        ├── {pdb}.pdb_points.pdb.gz
        └── {pdb}.pdb 
```

## TSV file:
The tsv file lists the predicted pockets in order of their score. Each pocket has the following attributes:

* rank 
* score	
* probability 
* sas_points - (int) number of solvent accessible surface points 
* surf_atoms - (int) integer of the number of surface atoms
* center_x - (float) the predicted pockets x center
* center_y - (float) the predicted pockets y center
* center_z - (float) the predicted pockets z center 
* residue_ids - (py dict) the residue sequence numbers that create the pocket { Chain : [ residue sequence numbers ] }
* residue_names - (py dict) the residue names that create the pocket { Chain : [ residue names ] }
* residue_types - (py dict) the character of the residues that create the pocket { Chain : [ characters ] }

    * 'N' represents non-polar amino acids
    * 'P' represents polar amino acids
    * '+' represents positively charged amino acids
    * '-' represents negatively charged amino acids
    * '0' a specific residue for which there is no info in the program

* surf_atom_ids - (py list) the atom serial number of all the atoms that are on the surface of the pocket

Information from the PDB is taken in this fashion:
| Columns | Data | Justification | Data Type |
| ------- | ---- | ------------- | --------- |
| 1-4 | "ATOM" | left | character |
| 7-11 | Atom serial number | right | integer |
| 13-16 | Atom name | left* | character |
| 17 | Alternate location indicator | - | character |
| 18-20 | Residue name | right | character |
| 22 | Chain identifier | - | character |
| 23-26 | Residue sequence number | right | integer |
| 27 | Code for insertions of residues | - | character |
| 31-38 | X orthogonal Angstrom coordinate | right | floating |
| 39-46 | Y orthogonal Angstrom coordinate | right | floating |
| 47-54 | Z orthogonal Angstrom coordinate | right | floating |
| 55-60 | Occupancy | right | floating |
| 61-66 | Temperature factor | right | floating |
| 73-76 | Segment identifier (optional) | left | character |
| 77-78 | Element symbol | right | character |
| 79-80 | Charge (optional) | - | character |


## Chimera CMD file

Has neccessary information to create the visualisations in chimera. The pockets are saved as selections titled "Pocket{NUM}" and colored untill the 18th pockets. 

The colors are ranked the same in all output, so it can be a visual aid for quick understanding of the pockets' rankings. This is true only for the Chimera file, not for the PyMol, because in PyMol the pockets and their colors can be easily viewed in the side panel.

| Color       | Rank |
|-------------|------|
| red         | 1    |
| orange      | 2    |
| yellow      | 3    |
| green       | 4    |
| cyan        | 5    |
| blue        | 6    |
| medium blue | 7    |
| purple      | 8    |
| hot pink    | 9    |
| magenta     | 10   |
| white       | 11   |
| gray        | 12   |
| black       | 13   |
| tan         | 14   |
| slate gray  | 15   |
| dark khaki  | 16   |
| plum        | 17   |
| rosy brown  | 18   |

run :

```bash
chimera {path}/predict_{pdb}/visualizations/chimera_{pdb}.cmd
```

## PyMol CMD file

In PyMol the pockets and their colors are conveniently displayed in the side panel.
run:

```bash
pymol {path}/predict_{pdb}/visualizations/{pdb}.pdb.pml
```

# Theoretical background

TBD

# Analysis

TBD

# References

This software is a lightweight version of [p2rank](https://github.com/rdk/p2rank).

* Krivak R, Hoksza D. [*P2Rank: machine learning based tool for rapid and accurate prediction of ligand binding sites from protein structure.*](https://doi.org/10.1186/s13321-018-0285-8) Journal of Cheminformatics. 2018 Aug.
* Capra JA, Laskowski RA, Thornton JM, Singh M, Funkhouser TA. *Predicting protein ligand binding sites by combining evolutionary sequence conservation and 3D structure.* PLoS
* Connolly M. *Solvent-accessible surfaces of proteins and nucleic acids.* Science. 1983;221(4612):709–13.
* Huang B, Schroeder M. [*LIGSITEcsc: predicting ligand binding sites using the Connolly surface and degree of conservation.*](10.1186/1472-6807-6-19) BMC Struct Biol. 2006 Sep 24;6:19.
* Krivák R, Hoksza D. [*Improving protein-ligand binding site prediction accuracy by classification of inner pocket points using local features.*](10.1186/s13321-015-0059-5) J Cheminform. 2015 Apr 1;7:12.
* Le Guilloux V, Schmidtke P, Tuffery P. [*Fpocket: an open source platform for ligand pocket detection.*](10.1186/1471-2105-10-168) BMC Bioinformatics. 2009 Jun 2;10:168. 
* RICHARDS, E M. (1977). *Ann. Rev. Biophys. Bioeng.* 6, 151-176.
* Zheng X, Gan L, Wang E, Wang J. [*Pocket-based drug design: exploring pocket space.*](10.1208/s12248-012-9426-6) AAPS J. 2013 Jan;15(1):228-41.
