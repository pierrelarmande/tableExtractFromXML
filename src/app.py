from src.Article import Article


def main():
    file2 = '../data/PMC2515340.xml'
    file1 = '../data/PMC3968010.xml'
    file3 = '../data/data.xml'

    myArticle = Article(file2)
    print('#################### Get article title ###################')
    print(myArticle.title)

    print('#################### Search for tag in article ###################')
    for tag in myArticle.searchTagInArticle('table', rootTag=None):
        print(tag.tag)

    print('#################### Search for tag  Alternatives in article ###################')
    for tag in myArticle.getArticleListOfTableWrapAlternatives():
        print(tag)

    print('#################### Search for table tag in article ###################')
    for tag in myArticle.getArticleListOfTable():
        print(tag)

    print('#################### Search for table thead tag in article ###################')
    nbTableHead = 0
    for tag in myArticle.getArticleListOfTableThead():
        nbTableHead = nbTableHead+ 1
        print("++++++++++++ thead :", nbTableHead)
        for tr in myArticle.getArticleListOfTableTr(tag):
            for td in myArticle.getArticlelistOTableTd(tr):
                myArticle.printTdText(td)

    print('#################### Search for table tbody tag in article ###################')
    nbTableBody = 0

    for tag in myArticle.getArticleListOfTableTbody():
        nbTableBody = nbTableHead + 1
        print("\t++++++++++++ tbody :", nbTableBody)
        nbTableTr = 0
        for tr in myArticle.getArticleListOfTableTr(tag):
            nbTableTr = nbTableTr + 1
            print("\t\t++++++++++++ tr :",  nbTableTr)
            for td in myArticle.getArticlelistOTableTd(tr):
                myArticle.printTdText(td)



if __name__ == '__main__':
    main()