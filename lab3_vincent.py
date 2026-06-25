# Vincent Tran | Green Tiger Team | Lab 3

# Ticket 1 -----------
username=  "vt009"
# it will have 5 characters.
num = len(username)
print(num)
# yes.  it was 5 chars.

# Ticket 2 -----------------
# this is the first char
print(username[0])
# and last char:
lastindex = len(username) - 1
print(username[lastindex])
# the last index is len(username) - 1 because the first char starts at 0, not 1.

#Ticket 3 -------------
#concat: 
print("Welcome " + "to " + "Loop, " + "@" + username)
#f string: 
print(f"Welcome to Loop, @{username}")
#i think both will look identical.
# the f string method felt easier because i didnt have to consider the spaces and the commas.

# Ticket 4 -- - - - - - -
#username[0] = "X"
# i think it errors cause it doesnt match the first char of my username
# File "C:\Users\vrtla\OneDrive\Desktop\hustle-summer26\lab3_vincent.py", line 27, in <module>    username[0] = "v"
# immutable: cannot be changed after created.

#LISTS:
#Ticket 5 ----------------
feed = ["Out with my dog", "my boys", "food"]
# i predict it will print 3.
print(len(feed))
print(feed[0])
# i used 0 index to get 1st post.

#Ticket 6 ---------------
feed.append("work")
# it will have index3.
print(feed)
# the 4th post is index 3 because it starts at 0, so 0,1,2,3 which is 4 elements.

#Ticket 7 -- - - -- -- - -- 
feed.pop(0)
print(feed)
# the 1 will become 0, 2 is 1, 3 is 2.
# i used pop, it removed a element at index param, and append adds it to the end.

#Ticket 8 --------------



