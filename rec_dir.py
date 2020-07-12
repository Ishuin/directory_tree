dir_structure = {
    'Books': {
        'Programming_language': {
            'Python': {
                'Django': {},
                'Flask': {},
                'Python_2.7': {},
                'Python_3': {},
            }
        },
        'CS_subjects': {
            'Data_Structure_and_Algorithm': {},
            'Computer_Networks': {},
            'Digital_Logic': {},
            "DBMS": {},
        }
    }
}

import os


def create_dir(path):
    try:
        os.makedirs(path)
        return True
    except FileExistsError:
        return True
    except:
        return False


def get_dir(structure, path=os.getcwd()):
    for i in structure.keys():
        if len(structure[i]) > 0:
            path = '/'.join([path, i])
            get_dir(structure[i], path)
        else:
            if create_dir('/'.join([path, i])):
                continue
            else:
                print("Cannot create Directory {}".format(i))
                pass


if __name__ == "__main__":
    get_dir(dir_structure)
    print("Process Completed Successfully!!")
