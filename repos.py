# pip install --user PyGithub
from github import Github

#your github access token : github.com/setting/tokens
g = Github("")

names = ["baesy0",
		"carmineomiga",
		"jeongsunyong",
		"khj6165",
		"kokodakdak",
		"niceinjeolmi",
		"penpenguin2018",
		"pieisland",
		"pyr53540",
		"qdimomibp",
		"sinewpark",
		"sohi9732",
		"YujinHa"]

for name in names:
	print name
	user = g.get_user(name)
	for repo in user.get_repos():
		print "\t"+repo.name

