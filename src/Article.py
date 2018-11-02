from lxml import etree
# artcle
"""
    <?properties ... ?>
    <?DTDIdentifier.IdentifierValue ... ?>
    <?DTDIdentifier.IdentifierType ... ?>
    <?SourceDTD.DTDName ... ?>
    <?SourceDTD.Version ... ?>
    <?ConverterInfo.XSLTName ... ?>
    <?ConverterInfo.Version ... ?>
    The about information are not collected 
    Article :
        title 
        front 
        body 
"""
class Article:

    def __init__(self, xmlFile=None):
        if not xmlFile is None:
            tree = etree.parse(xmlFile)
            articlePaper = tree.xpath("/article")
            article = articlePaper[0]
            self.article = article
            articleMeta = tree.xpath('/article/front/article-meta/title-group/article-title')
            title = articleMeta[0].text
            self.title = title


    """
        searches for all table-wrap and add them in the list of tableTableWrap in the article Class
    """
    def searchTagInArticle(self, tagName, rootTag=None):
        listTag = []
        if rootTag is None:
            listOfRootTag = self.article.getchildren()
        else:
            listOfRootTag = rootTag.getchildren()
        if len(listOfRootTag) > 0:
            list = listOfRootTag.copy()
            for tag in list:
                if tag.tag == tagName:
                    listTag.append(tag)
                elif len(tag.getchildren())> 0:
                    for newTag in tag.getchildren():
                        list.append(newTag)
        return listTag


    def getArticleListOfTableWrap(self, tableWrap='table-wrap'):
        listOfTableWrap = self.searchTagInArticle(tableWrap, rootTag=None)
        return listOfTableWrap

    def getArticleListOfTableWrapAlternatives(self, tagName='alternatives'):
        listOfTableWrapAlternative = []
        listOfTableWrap = self.getArticleListOfTableWrap()
        for tableWrap in listOfTableWrap:
            listOfTableWrapAlternative.append(self.searchTagInArticle(tagName,tableWrap))
        return listOfTableWrapAlternative

    def getArticleListOfTable(self, tagName='table'):
        listOfTable = []
        listOfTableWrapAlternive = self.getArticleListOfTableWrapAlternatives()
        for alternative in listOfTableWrapAlternive:
            listOfTable.append(self.searchTagInArticle(tagName, alternative[0]))
        return listOfTable


    def getArticleListOfTableThead(self, tagName='thead'):
        listOfThead = []
        listOfTable = self.getArticleListOfTable()
        for table in listOfTable:
            listOfThead.append(self.searchTagInArticle(tagName,table[0]))
        return listOfThead


    def getArticleListOfTableTbody(self, tagName='tbody'):
        listOfThead = []
        listOfTable = self.getArticleListOfTable()
        for table in listOfTable:
            listOfThead.append(self.searchTagInArticle(tagName,table[0]))
        return listOfThead


    def getArticleListOfTableTr(self, rootTag, tagName='tr'):
        return  self.searchTagInArticle(tagName, rootTag=rootTag[0])

    def getArticlelistOTableTd(self, rootTag, tagName='td'):
        listOfTd = rootTag.getchildren()
        return listOfTd

    def printTdText(self, rootTag):
        children = rootTag.getchildren()
        if len(children) == 0:
            print(rootTag.text)