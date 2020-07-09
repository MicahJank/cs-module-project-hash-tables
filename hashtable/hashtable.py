class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        # creates a list with the length of the capacity, each item in the list will be None initially and as values are hashed and put into storage the None values will change to
        # linked lists i.e the HashTableEntry
        self.storage = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # FNV offset basis computed using "chongo <Landon Curt Noll> /\../\" when expressed in ASCII?
        # 64 bit offset basis = 14695981039346656037
        # 64 bit prime = 1099511628211
        # XOR operator in python is ^
        key_utf8 = key.encode()
        hash = 14695981039346656037
        FNV_prime = 1099511628211
        
        for byte in key_utf8:
            hash = hash * FNV_prime
            hash = hash ^ byte
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # - get the index where this value needs to be added - can do that by using the hash index function and passing it the value
        # - use the index to update the correct spot in the storage, also use HashTable entry to make the new entry in the storage a linked list passing in the key and value
        storage_index = self.hash_index(key)
        # check if the storage already has a value stored in it at the given index - if it does, i need to traverse the linked list until the next value becomes None
        # once there is an empty spot in the linked list i can set the new value to that node in the linked list
        if self.storage[storage_index] is not None:
            current_node = self.storage[storage_index]
            while current_node.key != key:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    current_node.next = HashTableEntry(key, value)

            else:
                current_node.value = value
        else:
            self.storage[storage_index] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # I need to hash the key to get the index
        # use the index to find the correct spot in the storage to delete from
        # check if the the key exists
            # if there is no linked list at the hashed index then can print the warning
            # if there is i still need to traversal the linked list and look for the key, ie i need to check the next value and compare keys until i find the right key
        # if it does - remove it

        storage_index = self.hash_index(key)
        
        if self.storage[storage_index] is not None:
            current_node = self.storage[storage_index]
            while current_node.key != key:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    print("Unable to find the Key in the Hash Table")
                    return        
            else:
                # rather than just set the storage to None, there is a possiblity of deleting a node but still wanting to keep the next nodes in the list alive
                # so it would be better to just set the node to the next node in the list rather than simply setting it to None
                self.storage[storage_index] = self.storage[storage_index].next


        else:
            print("Unable to find the Key in the Hash Table")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # use the hash index function to get the index of the key in the storage
        # check if the value at the index is None - if it is return None, if not
        # traverse the linked list at the index and compare the key we are searching for with the key and the current_node
        # if we find the key, return the value associated with that key, otherwise return None if we traverse the whole linked list without finding the key

        storage_index = self.hash_index(key)
        # print("storage_index", storage_index)
        if self.storage[storage_index] is not None:
            current_node = self.storage[storage_index]
            while current_node.key != key:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    return None
            else:
                return current_node.value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
