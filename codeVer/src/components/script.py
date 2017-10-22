from github import Github

g = Github("gabdullah","")

def removeWhiteSpace(string):

#	for i in enumerate(string.length()):
#		for j in string[i]:
#			if string[i][j] in (' ', '.', ',', ':', ';', '/', '\\', '`', '\'', '\"', '=', '*', '!', '?', '#', '$', '&', '+', '^', '|', '~', '<', '>', '(', ')', '{', '}', '[', ']', '\t', '\n'):
	for ch in [' ', '.', ',', ':', ';', '/', '\\', '`', '\'', '\"', '=', '*', '!', '?', '#', '$', '&', '+', '^', '|', '~', '<', '>', '(', ')', '{', '}', '[', ']', '\t', '\n']:
		if ch in string:
			string = string.replace(ch, "")

	print string
	return string



#for repo in g.search_code('for repo in g.search_code(\'tetris\', language=\'python\'):', language='python'):
#	print repo.repository
#	print repo.html_url
#	break

t = ''
for i in g.get_user().get_repos():
	t = i
#	print t
	break

print t;

testString = "#for repo in g.search_code('for repo in g.search_code(\'tetris\', language=\'python\'):', language='python'):"
testString = removeWhiteSpace(testString)

#g.load(t)

#repo2 = g.get_repos()[1]
#print g.Comparison(repo1, repo2)
#print repo1.id
#print repo2.name