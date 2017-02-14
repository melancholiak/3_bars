#-------------------------------imports-----------------------------------------
import json
from functools import reduce
from math import sqrt
#--------------------------------core-------------------------------------------
def main():
  with open('data.json',encoding='cp1251') as data_ofc:
    data = json.load(data_ofc)
  x,y = float(input('x coord: ')),float(input('y coord:'))
  distance = lambda ax,ay,bx,by: sqrt( (ax-bx)**2 + (ay-by)**2 )
  distance_to_bar = lambda bar: distance(x,y,*bar['geoData']['coordinates'])
  list_of_steats = [i['SeatsCount'] for i in data]
  list_of_distances = [distance_to_bar(i) for i in data]
  maxseats = max(list_of_steats)
  minseats = min(list_of_steats)
  mindist  = min(list_of_distances)
  biggest  = [i['Name'] for i in data if i['SeatsCount']==maxseats]
  smallest = [i['Name'] for i in data if i['SeatsCount']==minseats]
  nearest  = [i['Name'] for i in data if gimme_dist(i)==mindist]
  print('''
  biggest bar(s): {}, with amount of seats of {}
  smallest bar(s): {},with amount of seats of {}
  nearest bar(s): {}, with distance from u of {}'''.format(
                                                ','.join(biggest),maxseats,
                                                ','.join(smallest),minseats,
                                                ','.join(nearest),mindist))
#---------------------------------main------------------------------------------
if __name__=='__main__':
  main()
#---------------------------------fin-------------------------------------------
