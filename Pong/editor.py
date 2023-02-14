# Nathan Wong, D01, 1663033
# Author Notes: 
# - Every function is implemented except for: sort(), replace(), and parts of delete()
# - User interaction also works 
# - To access the current node -> self.linkedlist.current
# - To access nodes in the DLL -> self.linkedlist.<node you want>
# - Keeping track of line number is not implemented, however, keeping track of the current line is. (IE: Program doesn't show line numbers, but it still knows where the user 'is').
# - the function print() was re-named to print_lines() instead -> Simply to avoid confusion with the built in function print().

class DLinkedListNode:
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if (initPrevious != None):
            initPrevious.next = self
        if (initNext != None):
            initNext.previous = self

    def __str__(self):
        return "%s" % (self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous= newPrevious

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.tail # Current needs to reference a spot in the DLL -> acccess via self.linkedlist.current
        self.size = 0

    def __str__(self):
        s = "[ "
        current = self.head;
        while current != None:
            s += "%s " % (current)
            current = current.getNext()
        s += "]"
        return s

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def search(self, item):
        # Returns a boolean
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        # Returns index (location) of an item
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def add(self, item):
        temp = DLinkedListNode(item, self.head, None)
        if self.head != None:
            self.head.setPrevious(temp)
        else:
            self.tail = temp
        self.head = temp
        self.size += 1

    def append(self, item):
        temp = DLinkedListNode(item, None, None)
        if (self.head == None):
            self.head = temp
        else:
            self.tail.setNext(temp)
            temp.setPrevious(self.tail)
        self.tail = temp
        self.size +=1

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.tail = previous
        self.size -= 1

    def removeitem(self, current):
        previous = current.getPrevious()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.tail=previous
        if previous:
            self.curr = previous.getNext()
        else:
            self.curr = None
        self.size -= 1
    

    def insert(self, current, item, where):
        # Current = Current node you're referencing
        # Item = New node you want to insert
        # Where = 0 (before current)
        # Where = 1 (after current)
        
        # Create new node with the item
        if item != None and item != '':
            item = item + ','
            new_node = DLinkedListNode(item, None, None)
        
        
            # If the file is empty
            if self.length == 0:
                self.append(new_node)
                # Set current
                self.current = new_node
            
            # Put new node behind the current node
            elif where == 0:
                # If the current node is the head or file is empty
                if self.current == None or self.current.getPrevious() == None:
                    # Set new node
                    self.add(new_node)
                    # Set current
                    self.current = new_node                
                
                # If the current node is the tail
                elif self.current.getNext() == None:
                    # Set new node
                    new_node.setPrevious(self.current.getPrevious())
                    new_node.setNext(self.current)
                    
                    # Set old node
                    self.current.getPrevious().setNext(new_node)
                    self.current.setPrevious(new_node)
                    
                    # Set curent
                    self.current = new_node
                    self.size += 1
                    
                # Insert the node
                else:
                    # Set new node
                    new_node.setPrevious(self.current.getPrevious())
                    new_node.setNext(self.current)
                
                    # Set old node's new 'neighbours'
                    self.current.getPrevious().setNext(new_node)
                    self.current.setPrevious(new_node)
                    # Set current
                    self.current = new_node
                    self.size += 1
                
            
            # Put new node in front of current
            elif where == 1:
                # If the current node is the tail -> Or if the file is empty
                if self.current == None or self.current.getNext() == None:
                    self.append(new_node)
                    # Set current
                    self.current = new_node
                
                # If the current node is the head
                elif self.current.getPrevious() == None:
                    # Set new node
                    new_node.setPrevious(self.head)
                    new_node.setNext(self.current.getNext())
                    
                    # Set old node
                    self.current.getNext().setPrevious(new_node)
                    self.current.setNext(new_node)
                    # Set current
                    self.current = new_node
                    self.size += 1
                    
                else:
                    # Set new node
                    new_node.setPrevious(self.current)
                    new_node.setNext(self.current.getNext())
                
                    # Set old node's new 'neighbours'
                    self.current.setNext(new_node)
                    self.current.setPrevious(self.current.getPrevious())
                    
                    # Set current
                    self.current = new_node
                    self.size += 1
                    

            
        
        else:
            # No item is provided to be inserted.
            None
class TextFile:
    # Intialize an empty file when program starts.
    def __init__(self, filename):
        self.filename = filename
        self.current = None
        self.linkedlist = DLinkedList()
    
    def getFilename(self):
        # Getter method that returns the name of the filename
        return self.filename
    
    def getName(self):
        return self.filename
    
    def setName(self, filename):
        self.filename = filename
        
    def getCurr(self):
        return self.linkedlist.current
    
    def setCurr(self, current):
        self.linkedlist.current = current
    
    
    def load(self, filename):
        # textlines_list is a list that contains each line in the read textfile as an element in the list.
        textlines_list = []
        
        # Set new filename
        self.filename = filename
        
        # Interact with file
        try:
            infile = open(filename, 'r')
        
        except FileNotFoundError:
            print('Error: File not found.')
        
        else:
            for line in infile:
                line = line.strip()
                textlines_list.append(line)
            
            infile.close()
            
            # Create a DLL based off the read file
            for line in textlines_list:
                line_node = DLinkedListNode(line, None, None)
                self.linkedlist.append(line_node)
            
            # Last line in file becomes current
            self.linkedlist.current = self.linkedlist.tail
            
            # Write tests here...
            #print('The head of the DLL is:', self.linkedlist.getHead())
            #print('The tail of the DLL is:', self.linkedlist.tail)
            #print('length of DLL: ', self.linkedlist.length())
            #print('The current value (new opened file):', self.linkedlist.current)
            #print('The DLL: ', self.linkedlist)
       
    
    def write(self, filename):
        # If the filename is not found, it'll save into a new textfile.
        # Note, even if the DLL is empty, it'll still write it to a new/exisiting file. 
        edited_text = []
        current = self.linkedlist.getHead()
        
        # Create a regular list with the DLL values (changes nodes into strings).
        for i in range(self.linkedlist.length()):
            edited_text.append(str(current.getData()))
            current = current.getNext()
   
        # Write the edited_text list into the filename
        try:
            infile = open(filename, 'w')
        
        except FileNotFoundError:
            print('Error: Filename is not found.')
        
        else:
            infile = open(filename, 'w')
            for line in edited_text:
                infile.write(line + '\n')
        
            infile.close()
        
        # Write tests here...
        # print('Success! Text was written to the opened file.')

    def linenumber(self, line_no):
        # Sets self.current to the requested line_no -> Must be in range of len(self.linkedlist.length())
        # Current is set to head for traversal -> self.current is still last line in the file.
        try:
            assert line_no >= 0 and line_no <= self.linkedlist.length()
        
        except AssertionError:
            print('Line number is invalid. Must be in the range of the size of the text file!')
            print('The current line is not changed')
        
        else:
            current = self.linkedlist.getHead()
            count = 0            
            while current != None:
                if count == line_no:
                    self.linkedlist.current = current
                    current = None
                    # Uncomment below to affirm the new current value.
                    # print('The NEW current value is:', self.linkedlist.current)
                    
                else:
                    count += 1
                    current = current.getNext()
    
    def print_next(self):
        try:
            self.linkedlist.current.getNext()
        
        # If the DLL is empty (Nothing happens, prompts for a new command)
        except AttributeError:
            None
        
        else:
            if self.linkedlist.current.getNext() == None:
                print(self.linkedlist.current)
            
            else: # set new current and print next line
                self.linkedlist.current = self.linkedlist.current.getNext()
                print(self.linkedlist.current)        
    
    def print_lines(self, offset):
        # Prints line(s) in the DLL. "offset" indiciates the number of lines forward or backward to print to.
        DLL_size = self.linkedlist.length()
        
        # If there's no offset value
        if offset == None or offset == 0:
            print('{}'.format(self.linkedlist.current))
            
        # Print all lines (positive offset)
        elif offset >= DLL_size:
            current = self.linkedlist.getHead()
            
            while current != None:
                for i in range(1, DLL_size+1):
                    if current != None:
                        print('{}: {}'.format(i, current.getData()))
                        current = current.getNext()
        
        # Print all lines (negative offset)
        elif offset < 0 and abs(offset) >= DLL_size:
            current = self.linkedlist.getTail()
            
            while current != None:
                for i in range(1, DLL_size+1):
                    if current != None:
                        print('{}: {}'.format(i, current.getData()))
                        current = current.getPrevious()
        
        # Print according to a positive offset value
        elif offset > 0:
            current = self.linkedlist.current
                                  
            for i in range(offset+1):
                if current != None:
                    print('{}'.format(current.getData()))
                    current = current.getNext()
                    if current == None:
                        current = self.linkedlist.tail                    
                
                elif current == None:
                    current =  self.linkedlist.tail
            
            # Set new current line
            self.linkedlist.current = current.getPrevious()
            
        # Print according to a negative offset value
        elif offset < 0:
            offset = abs(offset)
            current = self.linkedlist.current 
            
            # Iteratively move to the indicated previous element.
            for i in range(offset):
                current = current.getPrevious()
        
            # Output
            for i in range(offset + 1):
                if current != None:
                    print('{}'.format(current))
                    current = current.getNext()
        
        # If there's only 1 line 
        elif DLL_length == 1:
            print('1:', current.getData())
                
    
    def search(self, text, where):
        '''
        Returns a boolean and sets a new value to self.linkedlist.current IF possible.
        Inputs: text (a string), where (a string of either '/' or '?'
        Outputs: String representation of a node -> If a node is successfully found.
        '''
        # Search Forward
        if where == '/':
            
            # If current is the tail
            if self.linkedlist.current.getNext() == None:
                current = self.linkedlist.head
            
            else:
                current = self.linkedlist.current.getNext()
                
            # Search interatively
            searching = True
            while searching:
                # If text is found
                if text in str(current):
                    searching = False
                    # Set new current value
                    self.linkedlist.current = current
                    print(self.linkedlist.current)
                
                else:
                    current = current.getNext()
                    # Wrap around
                    if current == None:
                        current = self.linkedlist.head
                    
                    # After 1 full wrap around of the DLL, search stops
                    elif current == self.linkedlist.current:
                        searching = False
        
        # Search backwards
        elif where == '?':
            
            # If current is head -> Wrap around and start search at tail
            if self.linkedlist.current.getPrevious() == None:
                current = self.linkedlist.tail
            
            else:
                current = self.linkedlist.current.getPrevious()
                                
            # Search interatively
            searching = True
            while searching:
                if text in str(current):
                    searching = False
                    # Set new current value
                    self.linkedlist.current = current
                    # Tests below...
                    print(self.linkedlist.current)
                
                else:
                    current = current.getPrevious()
                    # Wrap around
                    if current == None:
                        current = self.linkedlist.tail
                        
                    # After 1 full wrap around of the DLL, search stops.    
                    elif current ==  self.linkedlist.current:
                        searching = False
        
    def delete(self, offset):
        # Note: Current line is also deleted
        # Function Limitations: Can only delete the current line. Can't delete backwards/fowards.
        # If there's no offset value, delete the current line.
        if offset == None:
            item_removed = self.linkedlist.current
            
            # Set new current
            if self.linkedlist.isEmpty():
                print('Error! File is empty and no lines can be deleted.')
            
            elif self.linkedlist.current.getNext() == None:
                self.linkedlist.current = self.linkedlist.current.getPrevious()
                self.linkedlist.removeitem(item_removed)
            
            else:
                self.linkedlist.current = self.linkedlist.current.getNext()
                self.linkedlist.removeitem(item_removed)
        
#########################################################################################################        
def main():
    # By default, user is writing into a new text file
    textfile = TextFile('NewTextFile.txt')
    filename = textfile.getFilename()
    
    # User Interaction
    user_input = None
    
    ######## Test functions ########### Uncomment below to automatically load in the file.
    #textfile.load('A3-sample.txt')
   
    # User Interaction
    while user_input != 'q':
        user_input = input('<')
        
        # Null command, print the next line (if possible)
        if user_input == '' or user_input == ' ':
            textfile.print_next()
        
        # Load command
        elif user_input.startswith('l'):
            split_string = user_input.split(' ')
            
            # Check if user actually provided a filename
            try:
                filename = split_string[1]
            
            except IndexError:
                print('Please provide a filename to load')
            
            else:
                filename = split_string[1]
                textfile.load(filename)
        
        # Write command
        elif user_input == 'w':
            filename = textfile.getFilename()
            textfile.write(filename)
        
        # Print command
        elif user_input.startswith('p'):
            split_string = user_input.split(' ')
            try:
                printed_lines = split_string[1]
            
            except IndexError:
                print('Please provide the number of lines to print.')
            
            else:
                printed_lines = split_string[1]
                printed_lines = int(printed_lines)
                textfile.print_lines(printed_lines)
        
        # Search command
        elif user_input.startswith('?') or user_input.startswith('/'):
            split_string = user_input.split(' ')
            
            try:
                where = split_string[0]
                text = split_string[1]
            
            except IndexError:
                print('Please provide valid text to search for and where.')
            
            else:
                where = split_string[0]
                text = split_string[1]
                textfile.search(text, where)
        
        # Insert Command
        elif user_input == 'i':
            inserted_line = input('')
            textfile.linkedlist.insert(textfile.linkedlist.current, inserted_line, 0)
            
        # Add Text command
        elif user_input == 'a':
            inserted_line = input('')
            textfile.linkedlist.insert(textfile.linkedlist.current, inserted_line, 1)
        
        # Delete Command
        elif user_input.startswith('d'):
            split_string = user_input.split(' ')
            
            try:
                offset = split_string[1]
            
            except IndexError:
                # Deletes current line (no additional argument provided)
                textfile.delete(None)
            
            else:
                offset = int(split_string[1])
                textfile.delete(offset)
        
        # Linenumber command (always have this as the last command to check for)
        else:
            try:
                int(user_input)
            
            except ValueError:
                # User inputted a command that doesn't exist. Nothing happens and user is prompted again.
                None
            
            else:
                user_input = int(user_input)
                length = textfile.linkedlist.length()
                
                if user_input in range(length):
                    textfile.linenumber(user_input)
            
            
        
        
        
        
        
        
  
main()