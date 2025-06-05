from Node import *
from helpers import *


class DistanceVector(Node):
    
    def __init__(self, name, topolink, outgoing_links, incoming_links):
        """ Constructor. This is run once when the DistanceVector object is
        created at the beginning of the simulation. Initializing data structure(s)
        specific to a DV node is done here."""

        super(DistanceVector, self).__init__(name, topolink, outgoing_links, incoming_links)
        
        # TODO: Create any necessary data structure(s) to contain the Node's internal state / distance vector data
        # B. Represent distance vector
        print(f"name: {name}, outgoing_links: {str(outgoing_links)}, incoming_links: {str(incoming_links)}")
        self.name = name
        self.topolink = topolink
        self.outgoing_links = outgoing_links
        self.incoming_links = incoming_links
        self.distance_vector = {self.name: 0}
        # for neighbor in self.outgoing_links:
        #     self.distance_vector[neighbor.name] = neighbor.weight

    def send_initial_messages(self):
        """ This is run once at the beginning of the simulation, after all
        DistanceVector objects are created and their links to each other are
        established, but before any of the rest of the simulation begins. You
        can have nodes send out their initial DV advertisements here. 

        Remember that links points to a list of Neighbor data structure.  Access
        the elements with .name or .weight """

        # TODO - Each node needs to build a message and send it to each of its neighbors
        # HINT: Take a look at the skeleton methods provided for you in Node.py
        message = Message(self.name, self.distance_vector)
        for neighbor in self.incoming_links:
            print(f"Sending initial message to neighbor: {neighbor.name}")
            self.send_msg(message, neighbor.name)

    def process_BF(self):
        """ This is run continuously (repeatedly) during the simulation. DV
        messages from other nodes are received here, processed, and any new DV
        messages that need to be sent to other nodes as a result are sent. """

        # Implement the Bellman-Ford algorithm here.  It must accomplish two tasks below:
        # TODO 1. Process queued messages     
        print(self.name + " processing messages...")  
        for msg in self.messages:
            sender_name = msg.sender_name
            sender_vector = msg.distance_vector
            print(f"{sender_name},{sender_vector}")


            # # Update distance vector based on received message
            # for neighbor, distance in sender_vector.items():
            #     if neighbor not in self.distance_vector:
            #         self.distance_vector[neighbor] = float('inf')
        
        # Empty queue
        self.messages = []

        # TODO 2. Send neighbors updated distances               

    def log_distances(self):
        """ This function is called immedately after process_BF each round.  It 
        prints distances to the console and the log file in the following format (no whitespace either end):
        
        A:(A,0) (B,1) (C,-2)
        
        Where:
        A is the node currently doing the logging (self),
        B and C are neighbors, with vector weights 1 and 2 respectively
        NOTE: A0 shows that the distance to self is 0 """
        
        # TODO: Use the provided helper function add_entry() to accomplish this task (see helpers.py).
        # An example call that which prints the format example text above (hardcoded) is provided.        
        print(f"Logging distances for node {self.name}: {self.distance_vector}")
        
        # add_entry("A", "(A,0) (B,1) (C,-2)")
        


class Message:

    def __init__(self, sender_name, distance_vector):
        self.sender_name = sender_name
        self.distance_vector = distance_vector

    def __str__(self):
        return f"Message from {self.sender_name}: {self.distance_vector}"

    def __repr__(self):
        return self.__str__()