# -*- coding: utf-8 -*-
import emoji
confessions = open('IIIT-H Confessions-revampd')
confessions = confessions.readlines()
confessions = [j[:-1] for j in confessions]

posts = []
for k in range(len(confessions)):
	# print repr(confessions[k])
	if confessions[k]=='IIIT-H Confessions':
		confession = {}
		confession['date-time'] = confessions[k+1] 
		confession['id'] = confessions[k+2]
		temp_list = []
		l = k+3
		while (confessions[l]!= 'IIIT-H Confessions'):
			temp_list.append(confessions[l])
			# if ('like' in confessions[l].lower()) or ('comment' in confessions[l].lower()):
			# 	break
			# print confessions[l]
			if l==(len(confessions)-1):
				break
			l +=1
		if not temp_list:
			print confessions[l]
		# print temp_list
		if ('like' in temp_list[-1].lower()) or ('comment' in temp_list[-1].lower()):
			temp_list = temp_list[:-1]
		if temp_list:
			confession['admin-notes'] = temp_list[-1]
		confession['confession'] = '. '.join(temp_list)
		# print confession
	if confession not in posts:
		posts.append(confession)

print len(posts)
for post in posts:
	if post['id'][0]!= '#':
		posts.remove(post)

for post in posts:
	# if not post['confession']:
	print post
# print posts
#Confession template.
# 29 August at 13:42 ·
# #93
# This is an honest confession.
# There is this guy who plays awesome guitar. He even played in the Freshers for the Agni House. I think that Agni came second just because of him. I see him around often in Vindhya canteen but I don't know his name. I would really like to know him more and become friends. I bet everyone is fan of his electric guitar.
# Please comment his name.
# UG1-F
# 12 Likes10 comments
