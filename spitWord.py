import random
import sys


class HistogramMaker(object):
    def createHistogram(self, textFileName):
        # 'frequency.txt'
        f = open(textFileName, 'r')
        # file_string = f.read()
        # print(file_string)
        histogramDictionary = {}
        for line in f:
            for word in line.split():
                value = 1
                if word in histogramDictionary:
                    value = histogramDictionary[word]
                    value += 1
                histogramDictionary[word] = value
        f.close()
        return histogramDictionary

    def createList(self, histogram):
        result = []
        for key, value in histogram.items():
            for _ in range(0, value):
                result.append(key)
        return result

    def spitOneWord(self, lista):
        randWordPosition = random.randint(0, len(lista) - 1)
        word = lista[randWordPosition]
        return word

    # sampling = []
    # if value in histogram:
    #     add.sampling
    # for value in histogram:


def main(argv):

    if len(argv) < 2:
        sys.exit()
        pass

    else:
        textFileName = argv[1]
        print('file name is:' + textFileName)
        maker = HistogramMaker()
        print('creating histogram')
        histogram = maker.createHistogram(textFileName)
        print('creating list')
        lista = maker.createList(histogram)
        print('randomizing word')
        word = maker.spitOneWord(lista)
        print('word is: ', word)
        pass


if __name__ == "__main__":
    main(sys.argv)
