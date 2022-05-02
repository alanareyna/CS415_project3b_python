import sys 
import string
import time

class TST_Node(object):
    def __init__(self, char, endOfWord=False):
        self.char = char
        self.leftNode = None
        self.rightNode = None
        self.equalNode = None
        self.endOfWord = endOfWord

# Alana's TST class:
# Ternary Search Tree class
class TST:
  def __init__(self):
    self.rootNode = None

  def get_TST(self, word):
    node = self.search(self.rootNode, word, 0)
    if node is None:
      return None
    return node.char

    # IMPLEMENT SEARCH FUNCTION
  def search(self, node, word, index):
    # must find the word in the tree by first finding the first character of the word
    # start at root node, if node is None (rootNode), search next node
    c = word[index]
    if node is None:
      return node
    if c < node.char:
      return self.search(node.leftNode, word, index)
    elif c > node.char:
      return self.search(node.rightNode, word, index)
    elif index < len(word) - 1:
      return self.search(node.equalNode, word, index + 1)
    else:
      node.endOfWord = True
      return node

  def insert(self, key, value, index):
    self.rootNode = self.insertItem(self.rootNode, key, value, 0)

    # INSERT ITEM PSEUDO CODE FROM: https://codereview.stackexchange.com/questions/230479/ternary-search-tree-implementation-in-python-3
  def insertItem(self, node, word, char, index):
    # create new variable to store character
    # key = word
    # value = first char
    c = word[index]

    if node is None:
      node = TST_Node(c)
    if c < node.char:
      node.leftNode = self.insertItem(node.leftNode, word, char, index)
    elif c > node.char:
      node.rightNode = self.insertItem(node.rightNode, word, char, index)
    elif index < len(word) - 1:
      node.equalNode = self.insertItem(node.equalNode, word, char, index + 1)
    else:
      node.endOfWord = True
      node.char = c
    return node

  def pre_order_traverse(self, node, word, all_words_with_substring):
    if node.endOfWord is True:
      all_words_with_substring.append(word + node.char)
    if node.leftNode:
      self.pre_order_traverse(node.leftNode, word, all_words_with_substring)
    if node.equalNode:
      self.pre_order_traverse(node.equalNode, word + node.char, all_words_with_substring)
    if node.rightNode:
      self.pre_order_traverse(node.rightNode, word, all_words_with_substring)


  # TST autocomplete
  def tst_autocomplete(self, substring):
    node = self.search(self.rootNode, substring, 0)
    all_words_with_substring = []
    word = substring
    if node is None:
        return None
    self.pre_order_traverse(node.equalNode, word, all_words_with_substring)
    return all_words_with_substring

# Create a node of the standard Trie class
class StandardTrieNode():
    # Initialize the node (should take a character parameter)
    def __init__(self):

      #None is equavalent to NULL in C++
      self.OurCharacterArray = [None] * 26
      #All nodes should be initialized to not be the end of the word 
      self.isEndOfWord = False 

# Cody's class 
# Create a standard Trie class
class StandardTrieStructure():
    #Initialize the Standard Trie Structure to get an empty root node to be the start of our Trie data structure 
    def __init__(self):
      self.rootNode = self.getNode()
    
    #returns an empty initialized tree node 
    def getNode(self):
      return StandardTrieNode()

    #takes the current character we are at in our word
    #and returns the index value of where that character should go
    #(Any character greater than "a" also has a greater ASCII value,
    #thus any character other than "a", - "a", will result in a value)
    #0-25
    def turnCharacterIntoIndex(self, ch):
      #return index value for this character we passed in
      return ord(ch)-ord('a')

    #Inserting a word into our trie structure 
    #If the key is a prefix of a trie node, just marks the leaf node
    def insertWord(self, word):
      #We need to start with the root of the Trie structure 
      OurPointer = self.rootNode
      #We need to do as many iterations (walk through the string) as the
      #size/length of the string 
      # SHOULD THERE BE A -1 HERE?
      AmountOfIterations = len(word)
      
      for level in range(AmountOfIterations):
        index = self.turnCharacterIntoIndex(word[level])

        #If the current character we're at is not present in the trie
        if not OurPointer.OurCharacterArray[index]:
          OurPointer.OurCharacterArray[index] = self.getNode()
          
        OurPointer = OurPointer.OurCharacterArray[index]
        
      #We are now at the last node in our trie data structure since
      #we popped out of the for loop. Mark that node as a the end of the
      #word we inserted
      OurPointer.isEndOfWord = True

      #The amount of iterations is equal to the number of characters in our string that we inserted into the trie. Each node created will have a reference to 26 characters it can link to within it's array, which is why we do AmountOfIterations * 26, as we need to account for the total space taken up by a single node along with it's references to other characters in it's array 
      return AmountOfIterations * 26

    #searches for a word in our trie data structure
    #returns true if the word is found, otherwise returns false if the word isn't found
    def searchForWord(self, word):
      #Start at our root node in the trie data structure
      OurPointer = self.rootNode 
      #We need to do as many iterations (walk through the string) as the
      #size/length of the string
      AmountOfIterations = len(word)
      for level in range(AmountOfIterations):
        index = self.turnCharacterIntoIndex(word[level])
        if not OurPointer.OurCharacterArray[index]:
          return False
        OurPointer = OurPointer.OurCharacterArray[index]


      #We've broken out of the for loop and successfully treked through
      #the entire word in our trie data structure. Return True
      return OurPointer.isEndOfWord


        #This function will go to where the last character of the word we pass is, and print all
    #words that may be derived from the word we passed (i.e. our word is a prefix to all words we'll be printing)
    def StandardTrieAutocompleteHelperFunction(self, PointerToNode, ListOfSuffixes, WordToBuild):
    

      #BASE CASES
      #If our recursive call takes us to a null node, return the list of suffixes
      #if PointerToNode == None:
        #return ListOfSuffixes
      #If we've reached the end of a word at the node we're currently at, add the word we've built so far to our list of suffixes
      if PointerToNode.isEndOfWord:
        ListOfSuffixes.append(WordToBuild)
        #return ListOfSuffixes

      #If we are not at a null node, or at the end of a word, we need to keep moving across all possible children of the node we're at to get all possible suffixes for the prefix we initially passed in on the very first call
      #Thus we'll need to loop through all possible children for this node and recursively call this function
        #0-25?????

      for iteration in range(0,26):
        #So long as the index in the array of the node we're currently at isn't a null value, then that means we have a character to append to our word
        if PointerToNode.OurCharacterArray[iteration] != None:
          #Add the character by adding the iteration we are at with the character a's numeric value and converting that sum back to a character which should give you the right character in the alphabet to add
          #WordToBuild = WordToBuild 
          
          #Now that we have our word appended, we can then pass it to a recursive call of this function which will keep moving down until it hits an end of word bool in our base case      
          self.StandardTrieAutocompleteHelperFunction(PointerToNode.OurCharacterArray[iteration], ListOfSuffixes, WordToBuild + chr((iteration + ord('a'))))

      
        


    # NEEDS TO BE MADE TO HANDLE INVALID INPUT 
    # This function will return an empty list if it cannot find the prefix we are passing in
    # Otherwise it will return a list of words that have the prefix as a part of the larger words(suffixes)
    def StandardTrieAutocomplete(self, word):

      #Lets declare an empty list so we can store those suffixes after we get to the end of our prefix
      ListOfSuffixes = []
      #Now we need to get to the end of our prefix (it does not matter if it's a word or not)
      #Start at our root node in the trie data structure
      OurPointer = self.rootNode 
      #We need to do as many iterations (walk through the string) as the
      #size/length of the string
      AmountOfIterations = len(word)
      for level in range(AmountOfIterations):
        #Turn the character we're at in our word into an index and capture that index value
        #index = OurPointer.turnCharacterIntoIndex(word[level])
        index = self.turnCharacterIntoIndex(word[level])
        #If our pointer doesn't find a value at that index in this node's array of pointers we cannot continue down the prefix's path of characters
        if not OurPointer.OurCharacterArray[index]:
          #We should return our empty list of suffixes. This prefix does not exist within our trie 
          return ListOfSuffixes

        #If we reach a valid index (i.e. that is statement did not run) we need to set our pointer to that node 
        OurPointer = OurPointer.OurCharacterArray[index]


      #If we've popped out of our for loop, that means we must be at the node that contains the last character of our prefix. We need to pass this node to our helper function so we can find all suffixes that contain our prefix.
      #We will also need to capture that helper function's return value (a list of autocompleted words)
      #ListOfSuffixes = AutocompleteHelperFunction(OurPointer, ListOfSuffixes, word)
      self.StandardTrieAutocompleteHelperFunction(OurPointer, ListOfSuffixes, word)
      return ListOfSuffixes

  
    

def read_file(filename):
  fileobject = open(filename)
  filetext = fileobject.read().split()
  fileobject.close()
  return filetext

#This function will drive the program
def main():  
  #filename = input("Enter file name:")
  #filelines = read_file(filename)
  filelines = read_file(sys.argv[1])
  #print(filelines)
  table = str.maketrans("","",string.punctuation)
  RemovedPunctuation = [words.translate(table) for words in filelines]
  #print(RemovedPunctuation)
  for i in range (len(RemovedPunctuation)):
      RemovedPunctuation[i] = RemovedPunctuation[i].lower()
  #for i in range(len(RemovedPunctuation)):
    #RemovedPunctuation[i] = RemovedPunctuation[i].split()
  #print(RemovedPunctuation)
  

  #Remember the command line arguements are taken as strings, so we have to read 1 as a string (or we could've converted the arguement to an int)
  #Specific strings are searched for and autocomplete results are computed and shown
  if sys.argv[2] == "1":

    #BUILD STANDARD TRIE AND  TST TRIE HERE 
    #Declaring a standard Trie here
    OurStandardTrieObject = StandardTrieStructure()

    #Declaring a TST tree 
    tst_object = TST()
    
    #We will need a counter for the size of the structure
    NumberOfCharactersCounter = 0
    #We'll need to time how long it'll take to build our standard trie 
    StartTime = time.perf_counter()
    #Inserting all words from input file into our Tire
    for word in RemovedPunctuation:
      NumberOfCharactersCounter = NumberOfCharactersCounter + OurStandardTrieObject.insertWord(word)
    #Once we've broken out of the for loop we can stop the timer for how long it's taken to build the standard trie 
    StopTime = time.perf_counter()

    #We need to get the difference between the two times in order to get how long it took the code between the two calls took to run (StopTime should have a greater time than StartTime)
    TimeTakenToBuildStandardTrie = StopTime - StartTime 
      
    print("Time taken to build the standard Trie is " + str(TimeTakenToBuildStandardTrie) + " and space occupied by it is " + str(NumberOfCharactersCounter))

    # TST size counter 
    tst_size = 0
    # TST build start time
    tst_start_time = time.perf_counter()
        # Inserting all words from input file into our Tire
    for word in RemovedPunctuation:
        for character in word:
            tst_object.insert(word, character, 0)
            tst_size = tst_size + 2

    # TST build stop time
    tst_stop_time = time.perf_counter()
    # TST total build time
    time_taken_to_build_tst = tst_stop_time - tst_start_time
    
    print("Time taken to build the BST based Trie is " + str(time_taken_to_build_tst) + " and space occupied by it is " + str(tst_size))

    prefixToComplete = input("Enter search string: ")

    #Now we can use that string for our trie objects 
    #We also need to time how long it takes to search for that string
    StartTime2 = time.perf_counter()
    OurStandardTrieObject.searchForWord(prefixToComplete)
    StopTime2 = time.perf_counter()
    #Get the difference between the two calls to get the actual time it took to exectute that search function
    TimeTakenToSearchInStandardTrie = StopTime2 - StartTime2

    print("Time taken to search in the standard Trie is " + str(TimeTakenToSearchInStandardTrie))
    
    StartTime3 = time.perf_counter()
    OurListOfSuffixes = OurStandardTrieObject.StandardTrieAutocomplete(prefixToComplete)
    StopTime3 = time.perf_counter()

    TimeTakenToAutocompleteInStandardTrie = StopTime3 - StartTime3

    print("Auto-complete results using standard Trie are: ", OurListOfSuffixes)
    print("Time taken to find auto-complete results in the standard Trie is " + str(TimeTakenToAutocompleteInStandardTrie))

    # TST start time to search for substring 
    tst_start_time_substring = time.perf_counter()
    tst_object.get_TST(prefixToComplete)
    # end time to search for substring
    tst_stop_time_substring = time.perf_counter()
    # total time to search for substring
    time_taken_to_search_tst = tst_stop_time_substring - tst_start_time_substring
    
    print("Time taken to search in the BST based Trie is " + str(time_taken_to_search_tst))

    tst_start_time_autocomplete = time.perf_counter()
    tst_list_of_suffixes = tst_object.tst_autocomplete(prefixToComplete)
    # end time to do tst autocomplete
    tst_end_time_autocomplete = time.perf_counter()
    # total time to do tst autocomplete
    time_taken_to_autocomplete_tst = tst_end_time_autocomplete - tst_start_time_autocomplete
    
    print("Auto-complete results using BST based Trie are: " + str(tst_list_of_suffixes))
    print("Time taken to find auto-complete results in the BST based Trie is " + str(time_taken_to_autocomplete_tst))

  #Remember the command line arguements are taken as strings, so we have to read 2 as a string (or we could've converted the arguement to an int)
  if sys.argv[2] == "2":
     #Declaring a standard Trie here
    OurStandardTrieObject = StandardTrieStructure()

    #Declaring a TST
    tst_object = TST()
    
    #We will need a counter for the size of the structure
    NumberOfCharactersCounter = 0

    #We'll need to time how long it'll take to build our standard trie 
    StartTime = time.perf_counter()
    #Inserting all words from input file into our Tire
    for word in RemovedPunctuation:
      NumberOfCharactersCounter = NumberOfCharactersCounter + OurStandardTrieObject.insertWord(word)
    #Once we've broken out of the for loop we can stop the timer for how long it's taken to build the standard trie 
    StopTime = time.perf_counter()

    #We need to get the difference between the two times in order to get how long it took the code between the two calls took to run (StopTime should have a greater time than StartTime)
    TimeTakenToBuildStandardTrie = StopTime - StartTime 
      
    print("Time taken to build the standard Trie is " + str(TimeTakenToBuildStandardTrie) + " and space occupied by it is " + str(NumberOfCharactersCounter))

    tst_size = 0

    #start time to build TST
    tst_start_time = time.perf_counter()

    for word in RemovedPunctuation:
        for character in word:
            tst_object.insert(word, character, 0)
            tst_size = tst_size + 2
    # TST build stop time
    tst_stop_time = time.perf_counter()
    # TST total build time
    time_taken_to_build_tst = tst_stop_time - tst_start_time
    print("Time taken to build the BST based Trie is " + str(time_taken_to_build_tst) + " and space occupied by it is " + str(tst_size))

    #We need to time how long it takes us to search all strings in the trie
    StartTime2 = time.perf_counter()
    
    #Now we need to search for all strings in the standard trie
    for word in RemovedPunctuation:
        OurStandardTrieObject.searchForWord(word)

    #We've broken out of the for loop, so get the stop time
    StopTime2 = time.perf_counter()

    #We need to get the difference between the two times in order to get how long it took the code between the two calls took to run (StopTime should have a greater time than StartTime)
    TimeTakenToSearchAllStringsInStandardTrie = StopTime2 - StartTime2

    
    
    print("Time taken to search all the strings in the standard Trie is " + str(TimeTakenToSearchAllStringsInStandardTrie))

    #TST search start time 
    tst_start_time_search = time.perf_counter()
    for word in RemovedPunctuation:
      tst_object.get_TST(word)
    #TST search end time 
    tst_stop_time_search = time.perf_counter()
    #TST total search time
    time_taken_to_search_tst = tst_stop_time_search - tst_start_time_search
    print("Time taken to search all the strings in the BST based Trie is " + str(time_taken_to_search_tst))

#Call the main function to run the main functionality of the program 
main()
