from typing import List, Any

from src.Article import Article


def main():
    file2 = '../data/PMC2515340.xml'
    file1 = '../data/PMC3968010.xml'
    file3 = '../data/data.xml'

    myArticle = Article(file2)
    print('\n\n########################### Get article title ##########################')
    print(myArticle.title)
    print('########################################################################\n\n')

    print('#################### Search for table tag in article ###################')
    for tag in myArticle.searchTagInArticle('table', rootTag=None):
        print(tag.tag)
    print('########################################################################\n')

    #print('#################### Search for tag  Alternatives in article ###################')
    #for tag in myArticle.getArticleListOfTableWrapAlternatives():
        #print(tag)

    #print('######################## Search for table tag in article #######################')
    #for tag in myArticle.getArticleListOfTable():
        #print(tag)
    #print('################################################################################\n')

    print('##################### Search for table thead tag in article ####################')
    nbTableHead = 0
    listThead = []
    for tagHead in myArticle.getArticleListOfTableThead():
        nbTableHead = nbTableHead+ 1
        print("++++++++++++ thead :", nbTableHead)
        listTr = []
        for tr in myArticle.getArticleListOfTableTr(tagHead):
            listTd = []
            for it in tr.iter():
                if it.tag == "td":
                    listTd.append(str(it.text).strip())
                elif it.tag != "tr":
                    tdTag = listTd.pop()
                    tdTag = tdTag + '#' + str(it.text).strip()
                    listTd.append(tdTag)
            listTr.append(listTd)
        listThead.append(listTr)

    for thead in listThead:
        print("\n tr of head : "+ str(len(thead)))
        print(thead)


    print('#################### Search for table tbody tag in article ###################')

    listTbody = []
    for tagTbody in myArticle.getArticleListOfTableTbody():
        listTr = []
        for tr in myArticle.getArticleListOfTableTr(tagTbody):
            listTd = []
            for it in tr.iter():
                if it.tag == "td":
                    listTd.append(str(it.text).strip())
                elif it.tag != "tr":
                    tdTag = listTd.pop()
                    tdTag = tdTag + '#' + str(it.text).strip()
                    listTd.append(tdTag)
            listTr.append(listTd)
        listTbody.append(listTr)
    for tbody in listTbody:
        print("\n tr of body : "+str(len(tbody)))
        print(tbody)




if __name__ == '__main__':
    main()