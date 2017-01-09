import re
import sys

# Script usage
if len(sys.argv) < 3:
    print "Usage:\n\t./instacompare.py followers_file following_file"
    exit()


# Lists
followers_file = sys.argv[1]
following_file = sys.argv[2]

i_am_followed_by = []
i_am_following = []
mutual_follows = []
no_follow_back_by_them = []
no_follow_back_by_me = []

# Process  for who user is followed by
with open(followers_file) as followers:
    followers = re.findall("(?P<username>\S+)\n(.+\n)*(\S+)\n\n",followers.read(), re.MULTILINE)
    for f in followers:
        i_am_followed_by.append(f[0])


# Process for who user is following
with open(following_file) as followers:
    following = re.findall("(?P<username>\S+)\n(.+\n)*(\S+)\n\n",followers.read(), re.MULTILINE)
    for f in following:
        i_am_following.append(f[0])

# Determine no follow by them (and mutual follows)
for person_i_follow in i_am_following:
    if person_i_follow not in i_am_followed_by:
        no_follow_back_by_them.append(person_i_follow)
    else:
        mutual_follows.append(person_i_follow)

# Determine no follow by me
for person_following_me in i_am_followed_by:
    if person_following_me not in i_am_following:
        no_follow_back_by_me.append(person_following_me)

# Sort alphabetically
no_follow_back_by_them.sort()
no_follow_back_by_me.sort()

# Output
print "\n=== The {} people I follow but who don't follow me back ===\n".format(len(no_follow_back_by_them))
for p in no_follow_back_by_them:
    print p.strip()

print "\n=== The {} people who follow me but I don't follow back ===\n".format(len(no_follow_back_by_me))
for p in no_follow_back_by_me:
    print p.strip()

print "\n=== Your {} mutual follows ===\n".format(len(mutual_follows))
for p in mutual_follows:
    print p.strip()
