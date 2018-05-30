class Page:
    def __init__ (self):
        self.rank = None
        self.vertices = None
        self.name = None
        self.outlinks = 0
        self.temprank = None
        self.inlinks = None

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def get_vertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_outlinks(self):
        return self.outlinks

    def set_outlinks(self, outlinks):
        self.outlinks = outlinks

    def get_temprank(self):
        return self.temprank

    def set_temprank(self, temprank):
        self.temprank = temprank

    def get_inlinks(self):
        return self.inlinks

    def set_inlinks(self, inlinks):
        self.inlinks = inlinks

    def __str__(self):
        return " Name :" + (self.name) + " Rank: " + str(self.rank) + " vertices: " + str(self.vertices) + " temprank: " + str(self.temprank) + " outlinks :" + str (self.outlinks)
    def isSink(self):
        if (self.outlinks == 0):
            return True
        return False
