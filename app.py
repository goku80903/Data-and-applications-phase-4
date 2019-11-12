import subprocess as sp
import pymysql
import pymysql.cursors

def ViewTheTeams():
    try:
        cur.execute("select * from TEAM;")
        results = cur.fetchall()
        for r in results:
            team_id = r['TEAM_ID']
            name = r['NAME'] 
            Owner_name = r['OWNER_NAME'] 
            matches_won = r['MATCHES_WON'] 
            matches_lost = r['MATCHES_LOST'] 
            matches_drawn = r['MATCHES_DRAWN'] 
            matches_no = r['MATCHES_WITHOUT_A_RESULT']
            print("TEAM_ID : ",team_id,", NAME: ",name," ,OWNER NAME: ",Owner_name," ,MATCHES WON: ",matches_won," ,MATCHES LOST: ",matches_lost," ,MATCHES DRAWN: ",matches_drawn," , MATCHES WITHOUT A RESULT: ",matches_no )

    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def ViewThePlayers():
    try:
        cur.execute("select * from PLAYER")
        results = cur.fetchall()
        for r in results:
            player_id = r['PLAYER_ID']
            first_name = r['FIRST_NAME']
            middle_name = r['MIDDLE_NAME']
            last_name = r['LAST_NAME']
            date_of_birth = r['DATE_OF_BIRTH']
            nationality = r['NATIONALITY']
            role = r['ROLE']
            matches_batting = r['MATCHES(BATTING)']
            innings_batting = r['INNINGS(BATTING)']
            runs_scored_batting = r['RUNS(BATTING)']
            average_batting = r['AVERAGE(BATTING)']
            highest_score_batting = r['HIGHEST_SCORE(BATTING)']
            strike_rate_batting = r['STRIKE_RATE(BATTING)']
            matches_bowling = r['MATCHES(BOWLING)']
            innings_bowling = r['INNINGS(BOWLING)']
            wickets_taken_bowling = r['WICKETS_TAKEN(BOWLING)']
            average_bowling = r['AVERAGE(BOWLING)']
            strike_rate_bowling = r['STRIKE_RATE(BOWLING)']
            best_figures_bowling = r['BEST_FIGURES(BOWLING)']
            matches_fielding = r['MATCHES(FIELDING)']
            innings_fielding = r['INNINGS(FIELDING)']
            catches_fielding = r['CATCHES(FIELDING)']
            run_outs_fielding = r['RUN_OUTS(FIELDING)']
            capped_status = r['CAPPED_STATUS']
            match_fee = r['MATCH_FEE']
            auctioned_price = r['AUCTIONED_PRICE']
            team_id = r['TEAM_ID']
            print("Player id: ",player_id," ,First name: ",first_name," ,Middle name: ",middle_name," ,Last name: ",last_name," ,Date of birth: ",date_of_birth," ,Nationality: ",nationality)
            print("Role: ",role," ,Capped Status: ",capped_status," ,Match Fee: ",match_fee," ,Auctioned Price ",auctioned_price," ,Team ID: ",team_id)
            print("Batting Stats: Matches: ",matches_batting," ,Innings: ",innings_batting," ,Runs: ",runs_scored_batting," ,Average: ",average_batting," ,Highest Score: ",highest_score_batting," ,Strike Rate: ",strike_rate_batting)
            print("Batting Stats: Matches: ",matches_batting," ,Innings: ",innings_batting," ,Runs: ",runs_scored_batting," ,Average: ",average_batting," ,Highest Score: ",highest_score_batting," ,Strike Rate: ",strike_rate_batting)
            print("Fielding Stats: Matches: ",matches_fielding," ,Innings: ",innings_fielding," ,Catches: ",catches_fielding," ,Run Outs: ",run_outs_fielding)
            

    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def ViewTheSchedule():
    try:
        cur.execute("SELECT DISTINCT G.DATE_AND_TIME , (SELECT T1.NAME FROM TEAM AS T1 WHERE T1.TEAM_ID=G.TEAM_IDA) AS `TEAM_1` , (SELECT T2.NAME FROM TEAM AS T2 WHERE T2.TEAM_ID=G.TEAM_IDB) AS `TEAM_2` FROM GROUND_USED AS G;")
        results = cur.fetchall()
        for r in results:
            date_and_time = r['DATE_AND_TIME']
            team_1 = r['TEAM_1']
            team_2 = r['TEAM_2']
            print("Date and Time: ",date_and_time , " ,Team 1: ",team_1 , " ,Team 2: ",team_2)

    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def ViewThePointsTable():
    try:
        cur.execute("select T.TEAM_ID,T.NAME from TEAM AS T ORDER BY T.MATCHES_WON*2+T.MATCHES_DRAWN*1+MATCHES_WITHOUT_A_RESULT")
        results = cur.fetchall()
        i=0
        for r in results:
            i+=1
            team_id = r['TEAM_ID']
            name = r['NAME']
            print("Postion: ",i," ,Team ID: ",team_id," ,Name: ",name)
            
    except pymysql.InternalError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def ViewThePlayerhigh():
    print("1.Highest Run Scorer")
    print("2.Highest Wicket Taker")
    check = int(input("Enter choice>>>>"))
    if(check==1):
        try:
            cur.execute("select P.PLAYER_ID , P.FIRST_NAME, P.MIDDLE_NAME , P.LAST_NAME from PLAYER AS P ORDER BY P.`RUNS(BATTING)` DESC;")   
            results = cur.fetchone()
            # for r in results:
            print("Player ID: ",results['PLAYER_ID']," ,First Name: ",results['FIRST_NAME']," ,Middle Name: ",results["MIDDLE_NAME"]," ,Last Name: ",results["LAST_NAME"])

        except pymysql.InternalError as e:
            code , message = e.args
            print(">>>>>>>>>>>>>>>>",code , message)
    elif(check==2):
        try:
            cur.execute("select P.PLAYER_ID , P.FIRST_NAME, P.MIDDLE_NAME , P.LAST_NAME from PLAYER AS P ORDER BY P.`WICKETS_TAKEN(BOWLING)` DESC;")   
            results = cur.fetchone()
            print("Player ID: ",results['PLAYER_ID']," ,First Name: ",results['FIRST_NAME']," ,Middle Name: ",results["MIDDLE_NAME"]," ,Last Name: ",results["LAST_NAME"])

        except pymysql.InternalError as e:
            code , message = e.args
            print(">>>>>>>>>>>>>>>>",code , message)

def WithdrawFromTeam():
    pla = input("Enter the id of player who wants to withdraw>>>>>")
    try:
        cur.execute("UPDATE PLAYER SET TEAM_ID="+'NULL'+" WHERE PLAYER_ID="+pla)
        con.commit()
    except pymysql.IntegrityError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def ModifyPersonaldetails():
    print("1.Modify personal details of Player")
    print("2.Modify personal details of Referee")
    choice = int(input("Enter choice>"))
    if(choice==1):
        player_id = input("Enter the ID of player for modifying details> ")
        print("Which deatail do you want to modify:")
        print("1.First Name")
        print("2.Middle Name")
        print("3.Last Name")
        print("4.Date of birth")
        print("5.Nationality")
        print("6.Role")
        print("7.Capped Status")
        print("8.Auctioned Price")
        choi = int(input("Enter Choice>"))
        i = input("Enter the detail>")
        if(i==''):
            inp="NULL"
        else:
            inp="'"
            inp+=i
            inp+="'"
        try:
            if(choi==1):
                cur.execute("UPDATE PLAYER SET FIRST_NAME="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==2):
                cur.execute("UPDATE PLAYER SET MIDDLE_NAME="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==3):
                cur.execute("UPDATE PLAYER SET LAST_NAME="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==4):
                cur.execute("UPDATE PLAYER SET DATE_OF_BIRTH="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==5):
                cur.execute("UPDATE PLAYER SET NATIONALITY="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==6):
                cur.execute("UPDATE PLAYER SET ROLE="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==7):
                cur.execute("UPDATE PLAYER SET CAPPED_STATUS="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
            if(choi==8):
                cur.execute("UPDATE PLAYER SET AUCTIONED_PRICE="+inp+" WHERE PLAYER_ID="+player_id+";")
                con.commit()
        except pymysql.IntegrityError as e:
            message = e.args
            print(">>>>>>>>>>>>>>>>",message)
    elif(choice==2):
        try:
            referee_id = input("Enter the ID of Referee for modifying details> ")
            print("Which deatail do you want to modify> ")
            print("1.First Name")
            print("2.Middle Name")
            print("3.Last Name")
            print("4.Date of birth")
            print("5.Nationality")
            print("6.SALARY")
            print("7.Matches refereed Domestic")
            print("8.Matches refereed International")
            choi = int(input("Enter Choice> "))
            i = input("Enter the detail>")
            if(i==''):
                inp="NULL"
            else:
                inp="'"
                inp+=i
                inp+="'"
            if(choi==1):
                cur.execute("UPDATE PLAYER SET FIRST_NAME="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==2):
                cur.execute("UPDATE PLAYER SET MIDDLE_NAME="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==3):
                cur.execute("UPDATE PLAYER SET LAST_NAME="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==4):
                cur.execute("UPDATE PLAYER SET DATE_OF_BIRTH="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==5):
                cur.execute("UPDATE PLAYER SET NATIONALITY="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==6):
                cur.execute("UPDATE PLAYER SET SALARY="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==7):
                cur.execute("UPDATE PLAYER SET MATCH_REFEREED_DOMESTIC="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
            if(choi==8):
                cur.execute("UPDATE PLAYER SET MATCH_REFEREED_INTERNATIONAL="+inp+" WHERE PLAYER_ID="+referee_id+";")
                con.commit()
        except pymysql.IntegrityError as e:
            code , message = e.args
            print(">>>>>>>>>>>>>>>>",code , message)
    
def DeleteFromTournament():
    try:
        pla = input("Enter the player you want to delete from the tournament>")
        cur.execute("SELECT CAPTAIN_ID FROM CAPTAINS;")
        results = cur.fetchall()
        captain = 0
        for r in results:
            if int(pla)==r['CAPTAIN_ID']:
                captain=1
        if (captain!=1):
            cur.execute("DELETE FROM PLAYER WHERE PLAYER_ID="+pla)
            con.commit()
        else:
            print("The player is a captain and cannot be removed")
            
    except pymysql.IntegrityError as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        ViewTheTeams()
    elif(ch==2):
        ViewThePlayers()
    elif(ch==3):
        ViewTheSchedule()
    elif(ch==4):
        ViewThePointsTable()
    elif(ch==5):
        ViewThePlayerhigh()
    elif(ch==6):
        WithdrawFromTeam()
    elif(ch==7):
        ModifyPersonaldetails()
    elif(ch==8):
        DeleteFromTournament()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")
    flag = 0

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='CRICKET_TOURNAMENT',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

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
            try:
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==20:
                    flag=1
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
            except:
                print("Invalid input")
    if(flag):
        break