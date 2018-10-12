from lxml import etree

from src.Article import Article
from src.TableWrap import TableWrap



def getTableHead(article):
    listTableWrap = article.listTableAlternatives
    for tableWrap in listTableWrap:
        listTable = tableWrap.listTable
        for table in listTable:
            for element in table:
                if element.tag == 'thead':
                   for row in element:
                        tableWrap.setListTableHearder(row.getchildren())


def getTable(article):
    listTableWrap = article.listTableAlternatives
    for tableWrap in listTableWrap:
        for element in tableWrap.alternative:
            if element.tag == 'table':
                tableWrap.setTable(element)


def getTableElements(article):
    for subTag in article.listTableWrap:
        id = subTag.get('id')
        orientation = subTag.get('orientation')
        myTableWrap = TableWrap(id)
        myTableWrap.setOrientation(orientation)
        listOfSubTag = subTag.getchildren()

        for tableTag in listOfSubTag:
            if tableTag.tag == 'object-id':
                myTableWrap.setObjectIdValue(objectvalue=tableTag.text)
            if tableTag.tag == 'label':
                myTableWrap.setLabel(label=tableTag.text)
            if tableTag.tag == 'caption':
                title = tableTag.getchildren()
                if title[0].tag == 'title':
                    myTableWrap.setCaption(caption=title[0].text)
            if tableTag.tag == 'alternatives':
                myTableWrap.setAlternative(alternative=tableTag)
        article.setListOfTableWrapAlternatives(myTableWrap)


def searchTable(rootTag, article):

    if rootTag.tag == 'table-wrap':
        article.setListOfTableWrap(rootTag)
    else:
        if len(rootTag) > 0:
            for child in rootTag:
                searchTable(child, article)


def main():
    file2 = '../data/PMC2515340.xml'
    file1 = '../data/PMC3968010.xml'
    file3 = '../data/data.xml'

    tree = etree.parse(file2)
    articlePaper = tree.xpath("/article")
    articleMeta = tree.xpath('/article/front/article-meta/title-group/article-title')
    title = articleMeta[0].text
    article = articlePaper[0]
    # print(article.tag)
    # print(len(article))
    myArticle = Article(title)
    searchTable(article, myArticle)
    print('####################1###################')
    for tableTag in myArticle.listTableWrap:
        print(tableTag)
    print('####################1###################\n\n\n')
    getTableElements(myArticle)
    print('####################2###################')
    for tableElement in myArticle.listTableAlternatives:
        print(tableElement.label)
    print('####################2###################\n\n\n')
    getTable(myArticle)
    print('####################3###################')

    print('####################3###################\n\n\n')
    getTableHead(myArticle)
    print('####################3###################')
    print(myArticle.listTableWrap[0].listOfTableHead)
    print('####################3###################\n\n\n')

if __name__ == '__main__':
    main()