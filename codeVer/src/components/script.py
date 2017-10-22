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

def percentage(inputStrings, dirtyStrings):
	percents = [1.0,1.0,1.0,1.0,1.0]
	j = float(len(inputStrings))
	for i in range(len(dirtyStrings)):
		percents[i] = float(dirtyStrings[i] / j)
#		print percents[i]
		percents[i] = percents[i] * 100.0
		print percents[i]
	return percents


#for repo in g.search_code('for repo in g.search_code(\'tetris\', language=\'python\'):', language='python'):
#	print repo.repository
#	print repo.html_url
#	break

#t = ''
#for i in g.get_user().get_repos():
#	t = i
#	print t
#	break

#print t;

testDirtyStrings = [1, 2, 3, 4, 5] 

#testing = this.$root.dirtyStrings[0]
#	Should only get the top 5 repos for every user input string
#	Can only grab repos when whitespace is still there
counter = 0
it = 0
testInputStrings = ["#for repo in g.search_code('for repo in g.search_code(\'tetris\', language=\'python\'):', language='python'):", "test", "test2", "test3", "test4"]
for gitStr in g.search_code(testInputStrings[counter]):
	print gitStr.html_url
	it = it + 1
	if it == 5:
		it = 0
		counter = counter + 1
		if counter == len(testInputStrings):
			break
#	if counter == 5:
#		break

for i in range(len(testInputStrings)):
	testInputStrings[i] = removeWhiteSpace(testInputStrings[i])

percents = percentage(testInputStrings, testDirtyStrings)

#print 'test'


#g.load(t)

#repo2 = g.get_repos()[1]
#print g.Comparison(repo1, repo2)
#print repo1.id
#print repo2.name