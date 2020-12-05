
passport = []
valid = 0
fields = {"byr":0,"iyr":0,"eyr":0,"hgt":0,"hcl":0,"ecl":0,"pid":0,"cid":1}
eyes = ['amb','blu','brn','gry','grn','hzl','oth']

with open("Day4.txt") as file:
  for line in file:
    if line == "\n":
      for field in passport:
        type = field[0]
        val = field[1]
        if type == "byr":
          if int(val) >= 1920 and int(val) <= 2002:
            fields["byr"] = 1
        elif type == "iyr":
          if int(val) >= 2010 and int(val) <= 2020:
            fields["iyr"] = 1
        elif type == "eyr":
          if int(val) >= 2020 and int(val) <= 2030:
            fields['eyr'] = 1
        elif type == 'hgt':
          meas = val[-2:]
          if len(val) > 2:
            num = int(val[:-2])
          else:
            num = 0
          if meas == 'cm':
            if num >= 150 and num <= 193:
              fields['hgt'] = 1
          elif meas == 'in':
            if num >= 59 and num <= 76:
              fields['hgt'] = 1
        elif type == 'hcl':
          if val[0] == '#' and val[1:].isalnum() and len(val[1:]) ==  6: 
            fields['hcl'] = 1
        elif type == 'ecl':
          if val in eyes:
            fields['ecl'] = 1
        elif type == 'pid':
          if val.isnumeric() and len(val) == 9:
            fields['pid'] = 1    
                 
      if 0 in fields.values():
        fields = {"byr":0,"iyr":0,"eyr":0,"hgt":0,"hcl":0,"ecl":0,"pid":0,"cid":1}
        passport = []
      else:    
        valid += 1
        fields = {"byr":0,"iyr":0,"eyr":0,"hgt":0,"hcl":0,"ecl":0,"pid":0,"cid":1}
        passport = []        
    else:
      values = line.split()
      for value in values:
        passport.append(value.split(':'))

print(valid)        


