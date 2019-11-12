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

def change_player_stats():
    try:
        player_id = input("PLAYER_ID>")
        matches = input("MATCHES>")
        innings_batting = input("INNINGS(BATTING)>")
        runsscored_batting = input("RUNS_SCORED(BATTING)>")
        avg_batting = input("AVERAGE(BATTING)>")
        highestscore_batting = input("HIGHEST_SCORE(BATTING)>")
        strikerate_batting = input("STRIKE_RATE(BATTING)>")
        innings_bowling = input("INNINGS(BOWLING)>")
        wickets_bowling = input("WICKETS_TAKEN(BOWLING)>")
        avg_bowling = input("AVERAGE(BOWLING)>")
        strikerate_bowling = input("STRIKE_RATE(BOWLING)>")
        bestfig_bowling = input("BEST_FIGURES(BOWLING)>")
        innings_fielding = input("INNINGS(FIELDING)>")
        catches_fielding = input("CATCHES(FIELDING)>")
        runouts_fielding = input("RUN_OUTS(FIELDING)>")
        capstatus = input("CAPPED_STATUS>")
        matchfee = input("MATCH_FEE>")
        autionedprice = input("AUCTIONED_PRICE>")
        cur.execute("update PLAYER set MATCHES(BATTING) = %s, INNINGS(BATTING) = %s, RUNS_SCORED(BATTING) = %s, AVERAGE(BATTING) = %s, HIGHEST_SCORE(BATTING) = %s, STRIKE_RATE(BATTING) = %s, MATCHES(BOWLING) = %s, INNINGS(BOWLING) = %s, WICKETS_TAKEN(BOWLING) = %s, AVERAGE(BOWLING) = %s, STRIKE_RATE(BOWLING) = %s, BEST_FIGURE(BOWLING) = %s, MATCHES(FIELDING) = %s, INNINGS(FIELDING) = %s, CATCHES(FIELDING) = %s, RUN_OUTS(FIELDING) = %s, CAPPED_STATUS = %s,MATCH_FEE = %s, AUCTIONED_PRICE = %s where PLAYER_ID = %d",matches,innings_batting,runsscored_batting,avg_batting,highestscore_batting,strikerate_batting,matches,innings_bowling,wickets_bowling,avg_bowling,strikerate_bowling,bestfig_bowling,matches,innings_fielding,catches_fielding,runouts_fielding,capstatus,matchfee,autionedprice,player_id)
        con.commit()
    
    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def change_team_stats():
    try:
        team_id = input("TEAM_ID>")
        matches_won = input("MATCHES_WON>")
        matches_lost = input("MATCHES_LOST>")
        matches_drawn = input("MATCHES_DRAWN>")
        matches_withoutresults = input("MATCHES_WITHOUT_A_RESULT>")
        cur.execute("update TEAM set  MATCHES_WON = "++"  MATCHES_LOST = %d MATCHES_DRAWN = %d MATCHES_WITHOUT_A_RESULT = %d where TEAM_ID = %d",matches_won,matches_lost,matches_drawn,matches_withoutresults,team_id)
        con.commit()
        
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_player():
    try:
        player_id = input("PLAYER_ID>")
        fname = input("FIRST_NAME>")
        mname = input("MIDDLE_NAME>")
        lname = input("LAST_NAME>")
        dob = input("DATE_OF_BIRTH>")
        nationality = input("NATIONALITY>")
        role = input("ROLE>")
        capstatus = input("CAPPED_STATUS>")
        cur.execute("insert into PLAYER( PLAYER_ID,FIRST_NAME, MIDDLE_NAME ,LAST_NAME , DATE_OF_BIRTH , NATIONALITY , ROLE , MATCHES(BATTING) , INNINGS(BATTING) , RUNS(BATTING) , AVERAGE(BATTING) , HIGHEST_SCORE(BATTING), STRIKE_RATE(BATTING) , MATCHES(BOWLING) , INNINGS(BOWLING) , WICKETS_TAKEN(BOWLING) , AVERAGE(BOWLING) , STRIKE_RATE(BOWLING) , BEST_FIGURES(BOWLING) , MATCHES(FIELDING) , INNINGS(FIELDING) , CATCHES(FIELDING) , RUN_OUTS(FIELDING) , CAPPED_STATUS , MATCH_FEE , AUCTIONED_PRICE ) values (%d, %s, %s, %s, %s, %s, %s,0,0,0,0,0,0,0,0,0,0,0,'0-0-0-0',0,0,0,%s,0,0,0 )",player_id,fname,mname,lname,dob,nationality,role,capstatus)
        con.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_team():
    try:
        name = input("NAME>")
        owner = input("OWNER_NAME>")
        team_id = input("TEAM_ID>")
        cur.execute("insert into TEAM(TEAM_ID,NAME, OWNER_NAME, MATCHES_WON , MATCHES_LOST , MATCHES_DRAWN , MATCHES_WITHOUT_A_RESULT) values (%d, %s , %s , 0, 0, 0, 0)",team_id,name,owner)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def add_new_ground():
    try:
        ground_id = input("GROUND_ID>")
        name = input("NAME>")
        location = input("LOCATION>")
        capacity = input("CAPACITY>")
        no_of_available_pitches = input("NO_OF_AVAILABLE_PITCHES>")
        longest_boundary = input("LONGEST_BOUNDARY>")
        team_id = input("TEAM_ID>")
        cur.execute("insert into GROUND(GROUND_ID , NAME , LOCATION , CAPACITY , LONGEST_BOUNDARY , TEAM_ID ) values (%s,%s,%s,%s,%s,%s)",ground_id,name,location,capacity,longest_boundary,team_id)
        for i in (0,no_of_available_pitches):
            pitch = input("Pitch type : ")
            cur.execute("insert into AVAILABLE_PITCHES(GROUND_ID ,PITCH_TYPE ) values (%s,%s)",ground_id,pitch)
            cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def buy_player():
    try:
        player_id = input("PLAYER_ID>")
        team_id = input("TEAM_ID>")
        price = input("AUCTIONED_PRICE>")
        salary = input("MATCH_FEE>")
        cur.execute("update PLAYER set TEAM_ID = %d, AUCTIONED_PRICE = %d ,MATCH_FEE = %d where PLAYER_ID = %d",team_id,price,salary,player_id)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message) 
    
def change_captian():
    try:
        player_id = input("PLAYER_ID>")
        team_id = input("TEAM_ID>")
        cur.execute("update CAPTAINS set CAPTAIN_ID = %d where TEAM_ID = %d",player_id,team_id)
        con.commit()
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
    
def remove_player():
    try:
        player_id = input("PLAYER_ID>")
        team_id = input("TEAM_ID>")
        cur.execute("")                     #   write code for this ------------------------------------------------------------------
        
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_supportstaff():
    try:
        staff_id = input("STAFF_ID>")
        Fname = input("FIRST_NAME>")
        Mname = input("MIDDLE_NAME>")
        Lname = input("LAST_NAME>")
        salary = input("SALARY>")
        role_played = input("ROLE_PLAYED")
        coach_type = input("COACH_TYPE>")
        field_advising = input("FIELD_ADVISING>")
        team_id = input("TEAM_ID>")
        cur.execute("insert into TEAM_SUPPORT_STAFF(STAFF_ID,TEAM_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,SALARY,ROLE_PLAYED,COACH_TYPE,FIELD_ADVISING) values (%d,%d,%s,%s,%s,%d,%s,%s,%s)",staff_id,team_id,Fname,Mname,Lname,salary,role_played,coach_type,field_advising)
        cur.commit()
    except pymysql.InternalError as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def remove_supportstaff():
    try:
        staff_id = input("STAFF_ID>")
        team_id = input("TEAM_ID>")
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
    elif(ch==9):
        change_player_stats()
        # change_player_stats(player_id,matches,innings_batting,runsscored_batting,avg_batting,highestscore_batting,strikerate_batting,innings_bowling,wickets_bowling,avg_bowling,strikerate_bowling,bestfig_bowling,innings_fielding,catches_fielding,runouts_fielding,capstatus,matchfee,autionedprice)
    elif(ch==10):
        change_team_stats()
    elif(ch==10):
        change_team_stats()
    elif(ch==11):
        add_new_player()
    elif(ch==12):
        add_new_team()
    elif(ch==13):
        add_new_ground()
    elif(ch==14):
        buy_player()
    elif(ch==15):
        change_captian()
    elif(ch==16):
        remove_player()
    elif(ch==17):
        add_supportstaff()
    elif(ch==18):
        remove_supportstaff()  
        
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
                db='CRICKET_TOURNAMENT',
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
                print("14.Buy a player")
                print("15.Change the captain")
                print("16.Remove the player from the team")
                print("17.Add a support staff")
                print("18.Remove a support staff")
                print("19.Logout")
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
        

    