# Creating Directory Tree

## Getting Started

Creating directories is a hassle, and if you are creating directories within directories, it seems to take forever in
completing the tree structure.
I was wasting a lot of time in doing this, so I decided to create a simple script that will do all the dirty work for
me.


### Input data

If you are familiar with Python, then you can understand the input as simple dictionary format, if not, understand this
as JSON.
```text
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
```

Input will simply be a file structure, as you can understand in the data. The above input format translates to the
directory structure below. 


All the directories that are leaf directories (empty directories), will contain blank
dictionary as the value of their name. As we move higher in the dictionary, the parent directory will act as the key for
the dictionary of directories within the parent directory.

If my explanation doesn't make sense, just look at the input
data and the directory structure.


### Directory Structure

```buildoutcfg
.
├── Books
│   └── Programming_language
│       ├── CS_subjects
│       │   ├── Computer_Networks
│       │   ├── Data_Structure_and_Algorithm
│       │   ├── DBMS
│       │   └── Digital_Logic
│       └── Python
│           ├── Django
│           ├── Flask
│           ├── Python_2.7
│           └── Python_3
................................................
```
---

**Note:** 
1. Data samples taken here are added by my individual understanding, therefore, the code is designed considering the input provided. If someone could find sample data that could break the code, please update me with the code sample and I will do my best to fix the code according to that data also.
2. Pull requests are also welcome.
