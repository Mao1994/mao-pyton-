url = 'https://nips.cc/Conferences/2015/AcceptedPapers';
papers = webread(url);
tree = htmlTree(papers);
subtree = findElement(tree,'div.col-xs-12.col-sm-9 div div div');
str = extractHTMLText(subtree);
str{1}(1:292)