class WordNet:

    def __init__(self, file_synsets, file_hypernyms):
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
        # Binary search -- synsets are already alphabetically sorted
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

    # TODO
    def distance(self, noun_a, noun_b):
        pass

    # TODO
    def sap(self, noun_a, noun_b):
        pass

