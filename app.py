import subprocess as sp
import pymysql
import pymysql.cursors

def ViewTheTeams():
    try:
        cur.execute("select * from persons")
        results = cur.fetchall()
        for r in results:
            print(r)
    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def change_player_stats(player_id,matches,innings_batting,runsscored_batting,avg_batting,highestscore_batting,strikerate_batting,innings_bowling,wickets_bowling,avg_bowling,strikerate_bowling,bestfig_bowling,innings_fielding,catches_fielding,runouts_fielding,capstatus,matchfee,autionedprice):
    try:
        cur.execute("update PLAYER set MATCHES(BATTING) = %s, INNINGS(BATTING) = %s, RUNS_SCORED(BATTING) = %s, AVERAGE(BATTING) = %s, HIGHEST_SCORE(BATTING) = %s, STRIKE_RATE(BATTING) = %s, MATCHES(BOWLING) = %s, INNINGS(BOWLING) = %s, WICKETS_TAKEN(BOWLING) = %s, AVERAGE(BOWLING) = %s, STRIKE_RATE(BOWLING) = %s, BEST_FIGURE(BOWLING) = %s, MATCHES(FIELDING) = %s, INNINGS(FIELDING) = %s, CATCHES(FIELDING) = %s, RUN_OUTS(FIELDING) = %s, CAPPED_STATUS = %s,MATCH_FEE = %s, AUCTIONED_PRICE = %s where PLAYER_ID = %d",matches,innings_batting,runsscored_batting,avg_batting,highestscore_batting,strikerate_batting,matches,innings_bowling,wickets_bowling,avg_bowling,strikerate_bowling,bestfig_bowling,matches,innings_fielding,catches_fielding,runouts_fielding,capstatus,matchfee,autionedprice,player_id)
        con.commit()
    
    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def change_team_stats(team_id,matches_won,matches_lost,matches_drawn,matches_withoutresults):
    try:
        cur.execute("update TEAM set  MATCHES_WON = %d  MATCHES_LOST = %d MATCHES_DRAWN = %d MATCHES_WITHOUT_A_RESULT = %d where TEAM_ID = %d",matches_won,matches_lost,matches_drawn,matches_withoutresults,team_id)
        con.commit()
        
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_player(player_id,fname,mname,lname,dob,nationality,role,capstatus):
    try:
        cur.execute("insert into PLAYER( PLAYER_ID,FIRST_NAME, MIDDLE_NAME ,LAST_NAME , DATE_OF_BIRTH , NATIONALITY , ROLE , MATCHES(BATTING) , INNINGS(BATTING) , RUNS(BATTING) , AVERAGE(BATTING) , HIGHEST_SCORE(BATTING), STRIKE_RATE(BATTING) , MATCHES(BOWLING) , INNINGS(BOWLING) , WICKETS_TAKEN(BOWLING) , AVERAGE(BOWLING) , STRIKE_RATE(BOWLING) , BEST_FIGURES(BOWLING) , MATCHES(FIELDING) , INNINGS(FIELDING) , CATCHES(FIELDING) , RUN_OUTS(FIELDING) , CAPPED_STATUS , MATCH_FEE , AUCTIONED_PRICE ) values (%d, %s, %s, %s, %s, %s, %s,0,0,0,0,0,0,0,0,0,0,0,'0-0-0-0',0,0,0,%s,0,0,0 )",player_id,fname,mname,lname,dob,nationality,role,capstatus)
        con.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_team(name,owner,team_id):
    try:
        cur.execute("insert into TEAM(TEAM_ID,NAME, OWNER_NAME, MATCHES_WON , MATCHES_LOST , MATCHES_DRAWN , MATCHES_WITHOUT_A_RESULT) values (%d, %s , %s , 0, 0, 0, 0)",team_id,name,owner)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def add_new_ground(ground_id,name,location,capacity,no_of_available_pitches,longest_boundary,team_id):
    try:
        cur.execute("insert into GROUND(GROUND_ID , NAME , LOCATION , CAPACITY , LONGEST_BOUNDARY , TEAM_ID ) values (%s,%s,%s,%s,%s,%s)",ground_id,name,location,capacity,longest_boundary,team_id)
        for i in (0,no_of_available_pitches):
            pitch = input("Pitch type : ")
            cur.execute("insert into AVAILABLE_PITCHES(GROUND_ID ,PITCH_TYPE ) values (%s,%s)",ground_id,pitch)
            cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def buy_player(player_id,team_id,price,salary):
    try:
        cur.execute("update PLAYER set TEAM_ID = %d, AUCTIONED_PRICE = %d ,MATCH_FEE = %d where PLAYER_ID = %d",team_id,price,salary,player_id)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message) 
    
def change_captian(player_id,team_id):
    try:
        cur.execute("update CAPTAIN set CAPTAIN_ID = %d where TEAM_ID = %d",player_id,team_id)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
    
def remove_player(player_id,team_id):
    try:
        cur.execute("")
        
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_supportstaff(staff_id,Fname,Mname,Lname,salary,role_played,coach_type,field_advising,team_id):
    try:
        cur.execute("insert into TEAM_SUPPORT_STAFF(STAFF_ID,TEAM_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,SALARY,ROLE_PLAYED,COACH_TYPE,FIELD_ADVISING) values (%d,%d,%s,%s,%s,%d,%s,%s,%s)",staff_id,team_id,Fname,Mname,Lname,salary,role_played,coach_type,field_advising)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def remove_supportstaff(staff_id,team_id):
    try:
        cur.execute("delete from TEAM_SUPPORT_STAFF where STAFF_ID = %d and TEAM_ID = %d",staff_id,team_id)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        ViewTheTeams()
    # elif(ch==2):
    #     fireAnEmployee()
    # elif(ch==3):
    #     promoteEmployee()
    # elif(ch==4):
    #     employeeStatistics()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='test',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1.View list of teams")
                print("2.View the list of players")
                print("3.View the match schedule")
                print("4.View the points table")
                print("5.View the player with most runs/most wickets")
                print("6.Withdraw from a team")
                print("7.Modify personal details")
                print("8.Disqualify a player")
                print("9.Change the stats of the player")
                print("10.Change the stats of the team")
                print("11.Add a new player to the tounrament")
                print("12.Add a new team")
                print("13.Add a new ground")
                print("14.Assign grounds to a team(Home ground)")
                print("15.Buy a player")
                print("16.Change the captain")
                print("17.Remove the player from the team")
                print("18.Add a support staff")
                print("19.Remove a support staff")
                print("20.Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==20:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        

    