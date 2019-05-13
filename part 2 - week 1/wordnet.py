class WordNet:
    """
    Part II, week 1, Princeton Algorithms course on Coursera.
    Assignment:
    http://coursera.cs.princeton.edu/algs4/assignments/wordnet.html

    This class implements the WordNet assignment. It takes in two files,
    one with the synsets and one with the hypernyms. (See website for format.)
    """

    def __init__(self, file_synsets, file_hypernyms):
        """
        Constructs a directed acyclic graph using a list (ordered by id) of dictionaries,
        each containing a synset and its hypernyms (an int referring to a synset id).
        """
        self._synsets = []
        with open(file_synsets) as syn:
            for line in syn:
                synset = line.split(',')[1]
                self._synsets.append({"synset": synset.split(), "hypernyms": [None]})
        with open(file_hypernyms) as hyp:
            for line in hyp:
                id, *hypernyms = [int(x) for x in line.split(',')]
                self._synsets[id]['hypernyms'] = hypernyms

    def __iter__(self):
        for entry in self._synsets:
            yield entry['synset']

    def is_noun(self, word):
        """
        Uses binary search to see if the given word is contained in the WordNet
        """
        lo = 0
        hi = len(self._synsets) - 1
        while lo < hi:
            mid = (hi + lo) // 2
            cur = self._synsets[mid]["synset"]
            if word.lower() in cur:
                return True
            elif word.lower() > cur[0]:
                lo = mid + 1
            elif word.lower() < cur[0]:
                hi = mid - 1
        return False

    def id(self, word):
        """
        Uses binary search to return the id of 'word'
        """
        lo = 0
        hi = len(self._synsets) - 1
        while lo < hi:
            mid = (hi + lo) // 2
            cur = self._synsets[mid]["synset"]
            if word.lower() in cur:
                return mid
            elif word.lower() > cur[0]:
                lo = mid + 1
            elif word.lower() < cur[0]:
                hi = mid - 1
        return None

    def distance(self, noun_a, noun_b):
        """
        Uses interleaved BFS to find out the distance between the two nouns,
        defined as the length of the path from each noun to their shortest common ancestor.
        """
        id_a = self.id(noun_a)
        id_b = self.id(noun_b)
        if not id_a or not id_b:
            return None
        a_queue = [id_a]
        a_count = 0
        b_queue = [id_b]
        b_count = 0
        a_ancestors = dict()
        b_ancestors = dict()
        if id_a == id_b:
            return 0
        while a_queue or b_queue:
            if a_queue:
                cur = a_queue.pop(0)
                if cur in b_ancestors:
                    return a_count + b_ancestors[cur]
                a_ancestors[cur] = a_count
                if self._synsets[cur]["hypernyms"]:
                    for hypernym in self._synsets[cur]["hypernyms"]:
                        a_queue.append(hypernym)
                a_count += 1
            if b_queue:
                cur = b_queue.pop(0)
                if cur in a_ancestors:
                    return b_count + a_ancestors[cur]
                b_ancestors[cur] = b_count
                if self._synsets[cur]["hypernyms"]:
                    for hypernym in self._synsets[cur]["hypernyms"]:
                        b_queue.append(hypernym)
                b_count += 1
        return None

    def sap(self, noun_a, noun_b):
        """
        Uses interleaved BFS to find out the shortest common ancestor between the two nouns.
        """
        id_a = self.id(noun_a)
        id_b = self.id(noun_b)
        if not id_a and id_b:
            return None
        a_queue = [id_a]
        b_queue = [id_b]
        a_ancestors = set()
        b_ancestors = set()
        if id_a == id_b:
            return 0
        while a_queue or b_queue:
            if a_queue:
                cur = a_queue.pop(0)
                if cur in b_ancestors:
                    return cur, self._synsets[cur]
                a_ancestors.add(cur)
                if self._synsets[cur]["hypernyms"]:
                    for hypernym in self._synsets[cur]["hypernyms"]:
                        a_queue.append(hypernym)
            if b_queue:
                cur = b_queue.pop(0)
                if cur in a_ancestors:
                    return cur, self._synsets[cur]
                b_ancestors.add(cur)
                if self._synsets[cur]["hypernyms"]:
                    for hypernym in self._synsets[cur]["hypernyms"]:
                        b_queue.append(hypernym)
        return None

    def outcast(self, word_list):
        """
        Calculates the distance from each noun to all other nouns, and returns the noun with the largest
        total distance as the "outcast" of the list.
        """
        for word in word_list:
            if not self.is_noun(word):
                raise IndexError(f"{word} not found in WordNet.")
        max_distance = 0
        outcast = None
        for a in range(len(word_list)):
            total = 0
            for word in word_list[a:]:
                distance = self.distance(word_list[a], word)
                total += distance
            if a > 0:
                for word in word_list[:a]:
                    distance = self.distance(word_list[a], word)
                    total += distance
            if total > max_distance:
                max_distance = total
                outcast = word_list[a]
        return outcast
