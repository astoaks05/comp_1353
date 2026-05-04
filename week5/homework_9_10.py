from ArraySet import ArraySet

def main():
    fem_names = ArraySet()
    male_names = ArraySet()

    with open('femaleNames2016.txt', 'r') as females:
        for line in females:
            parts = line.split()
            if parts:
                name = parts[0]
                fem_names.add(name)
    
    with open('maleNames2016.txt', 'r') as males:
        for line in males:
            parts = line.split()
            if parts:
                name = parts[0]
                male_names.add(name)

    shared_names = male_names.intersection(fem_names)
    print(f'number of common names between both genders: {shared_names.get_size()}')
    print(shared_names)

if __name__ == '__main__':
    main()