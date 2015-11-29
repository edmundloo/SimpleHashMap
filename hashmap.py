# HASHMAP KEY,VALUE PAIR CLASS
class Entry:
    def __init__(self, key, value):
        '''
        Stores a key, value pair to insert into the has map.
        :param key: Key to hash.
        :param value: Value to store.
        '''
        self.key = key
        self.value = value

# HASHMAP CLASS, ACCORDING TO PROMPT INSTRUCTIONS
class HashMap:
    def __init__(self, size:int = 0):
        '''
        Initializes the hash map with an array of size, "size", of empty arrays.
        Empty arrays are used for a chaining implementation of the hashmap.
        The table will be double the given size to keep load down and efficiency up.
        This will slightly increase our space complexity, but will increase speed.
        :param size: Max size of the hashmap.
        '''
        self.hash_table = [[] for i in range(size*2)]
        self.size = len(self.hash_table)
        self.elements = 0

    def set(self, key, value):
        '''
        Used to insert a key/value pair into the hashmap, returning true
        or false depending on successful insertion.
        :param key: Key of the pair to insert.
        :param value: Value of the pair to insert.
        :return: True for success and False for failure (i.e. full map).
        '''
        if self.elements >= self.size:
            return False
        for element in self.hash_table[hash(key)%self.size]:
            if element.key == key:
                element.value = value
                return True
        self.hash_table[hash(key)%self.size].append(Entry(key, value))
        self.elements += 1
        return True

    def get(self, key):
        '''
        Returns a value corresponding to the given key in the hash map.
        Returns None if the value doesn't exist in the map.
        :param key: The key to find the value for.
        :return: The value if the key exists, else none.
        '''
        if self.elements <= 0:
            return None
        for element in self.hash_table[hash(key)%self.size]:
            if element.key == key:
                return element.value
        return None

    def delete(self, key):
        '''
        Deletes a key/value pair from the hashmap, opening up a new
        space for elements. Returns None if the key is not found.
        :param key: The key of the pair to delete.
        :return: Value of the deleted pair, else None if the key doesn't exist.
        '''
        if self.elements <= 0:
            return None
        for element in self.hash_table[hash(key)%self.size]:
            if element.key == key:
                temp_val = element.value
                self.hash_table[hash(key)%self.size].remove(element)
                self.elements -= 1
                return temp_val
        return None

    def load(self):
        '''
        Returns the load factor of the hash map. The load factor
        is the items_in_map/size_of_map.
        :return: A decimal value representing the load.
        '''
        return self.elements/self.size if self.size != 0 else None


# VERY BASIC TESTING
hash_map1 = HashMap(5)
assert(hash_map1.get('Edmund')==None)
assert(hash_map1.delete('Edmund')==None)
assert(hash_map1.get('Urjit')==None)
assert(hash_map1.delete('Urjit')==None)
assert(hash_map1.set('Edmund', 'Chinese')==True)
assert(hash_map1.set('Urjit', 'Indian')==True)
assert(hash_map1.load()==2/10)
assert(hash_map1.get('Edmund')=='Chinese')
assert(hash_map1.get('Urjit')=='Indian')
assert(hash_map1.delete('Edmund')=='Chinese')
assert(hash_map1.delete('Urjit')=='Indian')
assert(hash_map1.delete('John')==None)
assert(hash_map1.delete('William')==None)
assert(hash_map1.load()==0)
hash_map2 = HashMap()
assert(hash_map2.load()==None)
hash_map3 = HashMap(1)
assert(hash_map1.get('Edmund')==None)
assert(hash_map1.set('Edmund', 'Chinese')==True)
assert(hash_map1.get('Edmund')=='Chinese')
assert(hash_map1.get('Urjit')==None)
assert(hash_map1.delete('Urjit')==None)
assert(hash_map1.delete('Edmund')=='Chinese')
assert(hash_map1.load()==0/1)
assert(hash_map1.set('Edmund', 'Chinese')==True)
assert(hash_map1.get('Edmund')=='Chinese')
assert(hash_map1.delete('Edmund')=='Chinese')


if __name__ == '__main__':
    # COMMAND-LINE INTERFACE
    print('Welcome to my Hash Map. Please enter a size for the hash map.')
    command = ['None']
    while command[0].lower() != 'x':
        input_size = int(input("Size:"))
        user_map = HashMap(input_size)
        print('Use "set (key) (value)" to set a key and value in the hash map.\n'
              'Use "get (key)" to get a value corresponding to a key in the hash map.\n'
              'Use "delete (key)" to delete a key,value pair from the hash map.\n'
              'Use "load" to get the load on the hash map, elements/size.\n'
              'Use "r" to restart the program.\n'
              'Use "x" to exit the program.')
        command = input('Command:').split()
        while(command[0].lower() not in ['r', 'x']):
            if command[0].lower() == 'set' and len(command) == 3:
                print("Set successful." if user_map.set(command[1], command[2]) else "Set failed.")
            elif command[0].lower() == 'get' and len(command) == 2:
                result = user_map.get(command[1])
                print("Get successful: "+result if result != None else "Get failed.")
            elif command[0].lower() == 'delete' and len(command) == 2:
                result = user_map.delete(command[1])
                print("Delete successful: "+result if result != None else "Delete failed.")
            elif command[0].lower() == 'load' and len(command) == 1:
                result = user_map.load()
                print(result if result != None else "Unable to load with size 0.")
            elif command[0].lower() in ['r', 'x']:
                pass
            else:
                print("Bad command.")
            command = input('Command:').split()

    print("Ending program! Goodbye!")
