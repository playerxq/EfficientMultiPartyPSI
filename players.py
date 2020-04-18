import message as ms
import bloom_filter
import helpers

# Base player class. Houses properties and methods common to both player types
class Player(object):
    def __init__(self, id, params):
        self.id = id
        self.messages = []
        self.params = params
        print("Player {} created".format(self.id))

    def identify(self):
        return self.id

    def createBloomFilter(self, m, n, hashes):
        self.bloom_filter = bloom_filter.new(m, n, hashes)

    # Choose a bit 1, 0 weighted according to self.params.p as provided by protocol
    def pickBit(self):
        r = helpers.uRandomInt(1) % 100
        return 1 if (r / 100 <= self.params.p) else 0

    def receiveOTMessage(self, message: ms.message):
        self.messages.append(message)

# Imagine a bicycle wheel. A "spoke" player is one on the outside
# All players P2+ will be spoke players
class PlayerSpoke(Player):
    def storeMessage(self, message):
        self.messages.append(message)

# Imagine a bicycle wheel. A "hub" player is one in the middle
# p0 and p1 will both always be hub players
class PlayerHub(Player):
    def storeTransfer(self, transfer):
        self.messages.append(transfer)