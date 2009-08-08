import time
from getpass import getpass

import tweepy

def callback(t, stream_object):
  if t == 'status':
    print(stream_object.text)   
  elif t == 'delete':
    print('delete!!!  id = %s' % stream_object['id'])
  elif t == 'limit':
    print('limit!!! track=%s' % stream_object['track'])

# Prompt for login credentials and setup stream object
username = input('Twitter username: ')
password = getpass('Twitter password: ')
stream = tweepy.Stream(username, password, callback)

# Prompt for mode of streaming and connect
while True:
  mode = input('Mode? [spritzer/follow/track] ')
  if mode == 'spritzer':
    stream.spritzer()
    break
  elif mode == 'follow':
    follow_list = input('Users to follow (comma separated): ')
    stream.follow(follow_list)
    break
  elif mode == 'track':
    track_list = input('Keywords to track (comma separated): ')
    stream.track(track_list)
    break
  else:
    print('Invalid choice! Try again.')

# Run in a loop until termination
while True:
  try:
    if stream.running is False:
      print('Stream stopped!')
      break
    time.sleep(1)
  except KeyboardInterrupt:
    break

# Shutdown connection
stream.disconnect()

print('Bye!')

