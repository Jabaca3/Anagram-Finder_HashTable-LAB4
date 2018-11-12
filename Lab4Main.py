'''
Created on Nov 10, 2018

@author: josephbaca
'''

class HashTableNode:
    def __init__(self, word, next):
        self.word = word
        self.next = next

class HashTable:
    def __init__(self, size):
        
        loadFactor = int(size*1.333)
        self.size = loadFactor
        self.table = [None] * loadFactor
        
    def hash(self, word):
        
        location =0
        
        for i in range(len(word)):
            ascii = ord(word[i])
            location += (ascii ** (len(word) - i))
            
        return location % self.size

    def insert(self, word):
        
        global comparisons
        loc = self.hash(word)
        
        if self.table[loc] != None:
            comparisons +=1
            
        self.table[loc] = HashTableNode( word, self.table[loc] )
        print("inserting '",word,"' At Location: ", loc)
        
    def search(self, word):
        
        loc = self.hash(word)
        temp = self.table[loc]
        
        while temp!= None:
            if temp.word == word:
                return True
            temp = temp.next
        return False
    
    def loadFactor(self, totalWords):
        return totalWords / self.size
        
def total_words_in_File(file): 
    
    count =0;
    for word in file:
        count+=1
    return count

def readFile_and_inster(hashTable, file):
    
    for word in file:
        hashTable.insert(word)
        
count = 0
def anagramsFromTable(word, hashtable, prefix="" ):
    
    english_words = hashtable
    global count
    
    if len(word) <= 1:
        stri = prefix + word
        if english_words.search(stri) == True: #Searches for the element in the Given Tree: AVL, RBT
            count+=1
            #print(prefix + word) # Will Print all Anagrams of a given word
           
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                anagramsFromTable(before + after,hashtable, prefix + cur)
                
                
def count_anagrams(word, hashTable):
    global count
    anagramsFromTable(word,hashTable)
    return count

def main():
    
    file = open("words_alpha.txt","r").read().split("\n")
    totalWordsInFile = total_words_in_File(file) #counts all the words in the file
    MyHashTable = HashTable(totalWordsInFile) #initiating the hash table
    
    readFile_and_inster(MyHashTable, file) #reads the file and throws words into the hash table
    
    # Information About The file/Table
    print()
    print ("Total comparisons: ", comparisons)
    print("Size of the Hash Table: ",MyHashTable.size)
    print("Total Words in File: ",totalWordsInFile)
    print("Load Factor: ", MyHashTable.loadFactor(totalWordsInFile))
    print("Average Comparison per Word: ", comparisons/totalWordsInFile)
    
    print()
    word = "spot" #input("Enter your word! ")
    print(count_anagrams(word, MyHashTable))
    
comparisons = 0 #keeping track of amount of comparisons
main()
