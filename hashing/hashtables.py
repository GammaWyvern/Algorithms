from hashtable import Data;
from hashtable import HashTable;

########################################
# Chain style hash table. This creates
# a link list at the hash location 
# when there are collisions.
########################################

class ChainHashTable(HashTable):
    def insert(self, data: Data) -> int:
        if(not self.table[data.hash()%(len(self.table))]):
            self.table[data.hash()%(len(self.table))] = data;
            return 0;
        else:
            temp = self.table[data.hash()%(len(self.table))];
            collisions = 1;
            while(temp.nextData):
                temp = temp.nextData;
                collisions += 1;
            temp.nextData = data;
            return collisions;

    def __str__(self):
        string = "";
        for row in range(0, len(self.table)):
            string += f"{row}:\t";
            data = self.table[row];
            while(data):
                string += f"{data.value} -> ";
                data = data.nextData;
            string += "\n";

        return string;

########################################
# Linear style hash table.
# This keeps going to the next
# sequential array spot upon collision
########################################

class LinearHashTable(HashTable):
    def insert(self, data: Data) -> int:
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            offset += 1;
            if(offset >= len(self.table)):
               print("Table is full, cannot insert anything else");
               return;
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return offset; #collisions

########################################
# Quadratic style hash table.
# This uses a quadratic equation to 
# find the next insertion spot upon 
# collision
########################################

class QuadraticHashTable(HashTable):
    def insert(self, data: Data) -> int:
        level = 0;
        a = b = 1;
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            level += 1;
            offset = (a*level) + (b*(level**2));
            if(level >= 100):
               print(f"Value {data.value} cannot be inserted in 100 steps, aborting insert");
               return;
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return level; #collisions

########################################
# Double hash style hash table.
# Uses a second hash function to find
# next insert spot upon collision.
########################################

class DoubleHashTable(HashTable):
    def insert(self, data: Data, secondHashNum: int) -> int:
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            level += 1;
            offset = level*data.secondaryHash(secondHashNum);
            if(level >= 100):
               print(f"Value {data.value} cannot be inserted in 100 steps, aborting insert");
               return;
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return level;

