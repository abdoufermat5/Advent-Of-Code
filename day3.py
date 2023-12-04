def gearRatios1(filename: str) -> int:
  import re
  # all special chars except .
  pat=re.compile('[^\w.]')
  sum_parts = 0
  with open(filename) as f:
      data = f.readlines()
      n_rows = len(data)
      n_cols = len(data[0].strip())
      
      res = 0
      for i in range(n_rows):
        start = None
        j = 0
        while j < n_cols:
          is_part = []
          if data[i][j].isdigit():
            if start is None:
              # debut
                start = j
            while data[i][j].isdigit():
              # check voisins
              for x in range(i - 1, i + 2):
                  for y in range(j - 1, j + 2):
                      if 0 <= x < n_rows and 0 <= y < n_cols:
                        is_part.append(len(pat.findall(data[x][y])) != 0)
              j+=1
            if not any(is_part):
              start = None
            # if yes then add to sum
            else:
              res += int(data[i][start:j])
              start = None
          j+=1
          
  return res



def gearRatios2(filename: str) -> int:
  sum_gear = 0
  with open(filename) as f:
      data = f.readlines()
      n_rows = len(data)
      n_cols = len(data[0].strip())
      for i in range(n_rows):
        start = None
        j = 0
        while j < n_cols:
          neighbors = []
          pos = []
          if data[i][j]=="*":
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < n_rows and 0 <= y < n_cols:
                      
                      if data[x][y].isdigit():
                        a = 0
                        s = data[x][y]
                        a = y+1
                        
                        # get right part
                        while a < n_cols and data[x][a].isdigit():
                          s+=data[x][a]
                          a+=1
                        a = y-1
                        # get left part
                        
                        while a>=0 and data[x][a].isdigit():
                          s = data[x][a] + s
                          a -= 1
                        # check if the neighbors not already aded
                        if (x, a) not in pos:
                          pos.append((x,a))
                          neighbors.append(int(s))
            if len(neighbors)==2:
              n1, n2 = neighbors
              sum_gear += n1*n2
              # reset pos et neighbors
              pos = []
              neighbors = []
          j+=1
  return sum_gear                           