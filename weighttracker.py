import matplotlib.pyplot as plt

have_not_eaten_yet = {'calories':0,'protein':0,'fats':0,'carbs':0}


class user: 
    
	def __init__(self, name, daily_weight, daily_macros): 
		self.name = name
		self.weight = daily_weight
		self.daily_macros = daily_macros
		self.seven_day = [str(daily_weight)+'\n'] * 7
		with open("{}_seven_day".format(self.name),'w') as fptr:
			fptr.write(''.join(self.seven_day))		



Marshall = user("Marshall", 185, have_not_eaten_yet) 

def get_seven_day(user): 
	with open("{}_seven_day".format(user.name),'r') as fptr:
		seven_day = fptr.readlines()
	return seven_day	
		


def update_weight(user, new_weight): 
	user.weight =  new_weight
	seven_day = get_seven_day(user)
	with open("{}_seven_day".format(user.name),'w') as fptr: 
		fptr.seek(0)
		seven_day.append(str(new_weight)+'\n')
		if len(seven_day) > 7:
			fptr.write(''.join(seven_day[1:]))
		else:
			 fptr.write("\n".join(seven_day))
		fptr.truncate()



