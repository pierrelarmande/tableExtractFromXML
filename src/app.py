from src.Article import Article


def main():
    file2 = '../data/PMC2515340.xml'
    file1 = '../data/PMC3968010.xml'
    file3 = '../data/data.xml'

    myArticle = Article(file1)
    print('#################### Get article title ###################')
    print(myArticle.title)

    print('#################### Search for tag in article ###################')
    for tag in myArticle.searchTagInArticle('table', rootTag=None):
        print(tag.tag)

    print('#################### Search for tag in article ###################')
    for tag in myArticle.getArticleListOfTableWrapAlternatives():
        print(tag)

    print('#################### Search for table tag in article ###################')
    for tag in myArticle.getArticleListOfTable():
        print(tag)

    print('#################### Search for table thead tag in article ###################')
    for tag in myArticle.getArticleListOfTableThead():
        for tr in myArticle.getArticleListOfTableTr(tag):
            for td in myArticle.getArticlelistOTableTd(tr):
                myArticle.printTdText(td)



if __name__ == '__main__':
    main()