from random import choice 

class Person:
    infection_ratio = []
    def __init__(self, i=False, p=False):
        self.is_infected = i
        self.protected = p

    
    # what will happened to "other" and "self" persons if "self" touched "other"? 
    def touch(self, other ):
        if not other.is_infected:
            return

        else:
            if self.protected:
                return

            if not self.protected:
                 self.is_infected = True
            else:
                self.is_infected = choice(Person.infection_ratio)

        # we have 5 saturations where they interact with each other 
        
        # 1st situation
      
    
    def  __str__(self):
        return f"{self.is_infected , self.is_infected}"
    
    
    
# count how many infected
def count_and_print_daily_report( day , people):
    infected = 0
    non_infected = 0

    for p in people:
        if p.is_infected == True:
            infected += 1
        else:
            non_infected += 1
    
    print(f'day {day} infected = {infected:7d}')


def complement100(n):
    return 100 - n

# run a simulation of the spreade of the virus 
# 1st parameter is the number of people
# 2nd parameter is the ratio of how many peple are protecting themeself
# 3rd paramert is the ratio of chance if non-protected fet in touch with protected person 
# 4th paramter is number of days defult value is one day 
def run_simulate( number_of_people_in_city , have_protection_ratio, Low_infection_ratio ,  number_of_days = 2  ):
    ''' run_simulate ([number of people in the city], [have_protection_ratio],[Low_infection_ratio], [number of days (by defult == 1 day )] ) 
        notethat: second and third parameters must between 0 to 100  
        '''
    # set up the protection ratio and arrange the list 
    # dont_have_protection_ratio = (100 -  have_protection_ratio)
    protection_ratio = [True]*have_protection_ratio + [False]*complement100(have_protection_ratio)

    # set up the infection ratio and arrange the list 
    High_infection_ratio = (100 - Low_infection_ratio) 
    infection_ratio = [True]*High_infection_ratio + [False]*Low_infection_ratio

    #assigning ! 
    number_of_people = number_of_people_in_city   
    
    
    if (err):
        print('err')
        return


    # check if the sum of the abs == 100 otherwise the arguments passed in is wrong 
    if abs(have_protection_ratio) + abs(dont_have_protection_ratio) != 100 and abs(High_infection_ratio) + abs(Low_infection_ratio) != 100 :
        print('the total ratio must be between 0 to 100 ')
    else:
        
        # the stupid who will infect them 
        jeddah_people = []
        p = Person(True, False)
        jeddah_people.append(p)
        
        Person.infection_ratio = infection_ratio

        # create people with the random ratio of protection 
        for i in range(number_of_people):    
            p = Person( )
            p.is_infected =  False
            p.protected = choice(protection_ratio)
            jeddah_people.append(p)
    

    
    
        # looping for X of days 
        for day in range(1,number_of_days+1):            
            for person_index in range(number_of_people):
                for _ in range( randint(0,10) ):            
                    p1 = jeddah_people[ person_index ]
                    
                    Toutched_person_index = randint(0,number_of_people-1)
                    p2 = jeddah_people[ Toutched_person_index ]

                    p1.touch( p2 )

                    p2.touch( p1 )
                
                
                
            # printing the simulation day by day    
            Person.count_and_print_daily_report(day,jeddah_people)
        
#----- end function
