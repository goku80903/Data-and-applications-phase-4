import subprocess as sp
import pymysql
import pymysql.cursors
def smfg(i):
    if i == '':
        i = 'NULL'
    return i

def smtg(i):
    if i == '':
        i = 'NULL'
    else:
        i = "'"+i+"'"
    return i
def ViewTheTeams():
    try:
        cur.execute("select TEAM.NAME,TEAM.TEAM_ID from TEAM;")
        results = cur.fetchall()
        teams=[]
        for r in results:
            team ={}
            team['Team_ID']=r['TEAM_ID']
            team['Name']=r['NAME']
            team['Captain']=""
            team['Coaches']=[]
            team['Sponsors']=[]
            team['Players']=[]
            teams.append(team)
        cur.execute("SELECT P.FIRST_NAME,P.MIDDLE_NAME,P.LAST_NAME ,C.TEAM_ID FROM PLAYER AS P , CAPTAINS AS C WHERE P.PLAYER_ID = C.CAPTAIN_ID;")
        results = cur.fetchall()
        for r in results:
            for j in teams:
                if(j['Team_ID']==r['TEAM_ID']):
                    # j['Captian']=''
                    j['Captain']+=r['FIRST_NAME']+" "
                    if(r['MIDDLE_NAME']):
                        j['Captain']+=r['MIDDLE_NAME']+" "
                    j['Captain']+=r['LAST_NAME']

        cur.execute("SELECT P.FIRST_NAME,P.MIDDLE_NAME,P.LAST_NAME,P.ROLE_PLAYED ,T.TEAM_ID FROM TEAM_SUPPORT_STAFF AS P , TEAM AS T WHERE P.TEAM_ID = T.TEAM_ID AND P.ROLE_PLAYED='COACH';")
        results = cur.fetchall()
        for r in results:
            for j in teams:
                if(j['Team_ID']==r['TEAM_ID']):
                    coach = ""
                    coach+=r['FIRST_NAME']+" "
                    if(r['MIDDLE_NAME']):
                        coach+=r['MIDDLE_NAME']+" "
                    coach+=r['LAST_NAME']
                    j['Coaches'].append(coach)
        cur.execute("SELECT TS.NAME , TS.TEAM_ID FROM TEAM_SPONSOR AS TS;")
        results = cur.fetchall()
        for r in results:
            for j in teams:
                if(j['Team_ID']==r['TEAM_ID']):
                    coach = ""
                    coach +=r['NAME']
                    j['Sponsors'].append(coach)
        cur.execute("SELECT P.FIRST_NAME ,P.MIDDLE_NAME,P.LAST_NAME,P.TEAM_ID FROM PLAYER AS P;")
        results = cur.fetchall()
        for r in results:
            for j in teams:
                if(j['Team_ID']==r['TEAM_ID']):
                    coach = ""
                    coach+=r['FIRST_NAME']+" "
                    if(r['MIDDLE_NAME']):
                        coach+=r['MIDDLE_NAME']+" "
                    coach+=r['LAST_NAME']
                    j['Players'].append(coach)
        for j in teams:
            print("Team ID: ",j['Team_ID']," ,Name: ",j['Name']," ,Captain: ",j['Captain'])
            print("Coaches: ")
            for r in j['Coaches']:
                print("\t",r)
            print("Sponsors: ")
            for r in j['Sponsors']:
                print("\t",r)
            print("Players: ")
            for r in j['Players']:
                print("\t",r)
            print()
    except Exception as e:
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
            

    except Exception as e:
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

    except Exception as e:
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
            
    except Exception as e:
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

        except Exception as e:
            code , message = e.args
            print(">>>>>>>>>>>>>>>>",code , message)
    elif(check==2):
        try:
            cur.execute("select P.PLAYER_ID , P.FIRST_NAME, P.MIDDLE_NAME , P.LAST_NAME from PLAYER AS P ORDER BY P.`WICKETS_TAKEN(BOWLING)` DESC;")   
            results = cur.fetchone()
            print("Player ID: ",results['PLAYER_ID']," ,First Name: ",results['FIRST_NAME']," ,Middle Name: ",results["MIDDLE_NAME"]," ,Last Name: ",results["LAST_NAME"])

        except Exception as e:
            code , message = e.args
            print(">>>>>>>>>>>>>>>>",code , message)

def WithdrawFromTeam():
    pla = input("Enter the id of player who wants to withdraw>>>>>")
    try:
        flag =0
        cur.execute("select PLAYER_ID , TEAM_ID from PLAYER")
        result = cur.fetchall()
        for r in result:
            if(r['PLAYER_ID']==int(pla)):
                flag = 1
                cur.execute("UPDATE PLAYER SET TEAM_ID="+'NULL'+" WHERE PLAYER_ID="+pla)
                con.commit()
        if(flag==0):
            print("player doesn't exist")
    except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
            
    except Exception as e:
        message = e.args
        print(">>>>>>>>>>>>>>>>",message)

def change_player_stats():
    try:
        player_id = smfg(input("PLAYER_ID>"))
        matches = smfg(input("MATCHES>"))
        innings_batting = smfg(input("INNINGS(BATTING)>"))
        runsscored_batting = smfg(input("RUNS_SCORED(BATTING)>"))
        avg_batting = smfg(input("AVERAGE(BATTING)>"))
        highestscore_batting = smfg(input("HIGHEST_SCORE(BATTING)>"))
        strikerate_batting = smfg(input("STRIKE_RATE(BATTING)>"))
        innings_bowling = smfg(input("INNINGS(BOWLING)>"))
        wickets_bowling = smfg(input("WICKETS_TAKEN(BOWLING)>"))
        avg_bowling = smfg(input("AVERAGE(BOWLING)>"))
        strikerate_bowling = smfg(input("STRIKE_RATE(BOWLING)>"))
        bestfig_bowling = smtg(input("BEST_FIGURES(BOWLING)>"))
        innings_fielding = smfg(input("INNINGS(FIELDING)>"))
        catches_fielding = smfg(input("CATCHES(FIELDING)>"))
        runouts_fielding = smfg(input("RUN_OUTS(FIELDING)>"))
        capstatus = smfg(input("CAPPED_STATUS>"))
        matchfee = smfg(input("MATCH_FEE>"))
        autionedprice = smfg(input("AUCTIONED_PRICE>"))
        cur.execute("update PLAYER set `MATCHES(BATTING)` = "+matches+", `INNINGS(BATTING)` = "+innings_batting+", `RUNS(BATTING)` = "+runsscored_batting+", `AVERAGE(BATTING)` = "+avg_batting+", `HIGHEST_SCORE(BATTING)` = "+highestscore_batting+", `STRIKE_RATE(BATTING)` = "+strikerate_batting+", `MATCHES(BOWLING)` = "+matches+", `INNINGS(BOWLING)` = "+innings_bowling+", `WICKETS_TAKEN(BOWLING)` = "+wickets_bowling+", `AVERAGE(BOWLING)` = "+avg_bowling+", `STRIKE_RATE(BOWLING)` = "+strikerate_bowling+", `BEST_FIGURES(BOWLING)` = "+bestfig_bowling+", `MATCHES(FIELDING)` = "+matches+", `INNINGS(FIELDING)` = "+innings_fielding+", `CATCHES(FIELDING)` = "+catches_fielding+", `RUN_OUTS(FIELDING)` = "+runouts_fielding+", CAPPED_STATUS = '"+capstatus+"',MATCH_FEE = "+matchfee+", AUCTIONED_PRICE = "+autionedprice+" where PLAYER_ID = "+player_id)
        con.commit()
    
    except Exception as e:
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def change_team_stats():
    try:
        team_id = smfg(input("TEAM_ID>"))
        matches_won = smfg(input("MATCHES_WON>"))
        matches_lost = smfg(input("MATCHES_LOST>"))
        matches_drawn = smfg(input("MATCHES_DRAWN>"))
        matches_withoutresults = smfg(input("MATCHES_WITHOUT_A_RESULT>"))
        cur.execute("update TEAM set  MATCHES_WON = "+matches_won+" , MATCHES_LOST = "+matches_lost+", MATCHES_DRAWN = "+matches_drawn+" ,MATCHES_WITHOUT_A_RESULT = "+matches_withoutresults+" where TEAM_ID = "+team_id)
        con.commit()
        
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_player():
    try:
        player_id = smfg(input("PLAYER_ID>"))
        fname = smtg(input("FIRST_NAME>"))
        mname = smtg(input("MIDDLE_NAME>"))
        lname = smtg(input("LAST_NAME>"))
        dob = smtg(input("DATE_OF_BIRTH>"))
        nationality = smtg(input("NATIONALITY>"))
        role = smtg(input("ROLE>"))
        capstatus = smtg(input("CAPPED_STATUS>"))
        cur.execute("insert into PLAYER( PLAYER_ID,FIRST_NAME, MIDDLE_NAME ,LAST_NAME , DATE_OF_BIRTH , NATIONALITY , ROLE , `MATCHES(BATTING)` , `INNINGS(BATTING)` , `RUNS(BATTING)` , `AVERAGE(BATTING)` , `HIGHEST_SCORE(BATTING)`, `STRIKE_RATE(BATTING)` , `MATCHES(BOWLING)` , `INNINGS(BOWLING)` , `WICKETS_TAKEN(BOWLING)` , `AVERAGE(BOWLING)` , `STRIKE_RATE(BOWLING)` , `BEST_FIGURES(BOWLING)` , `MATCHES(FIELDING)` , `INNINGS(FIELDING)` , `CATCHES(FIELDING)` , `RUN_OUTS(FIELDING)` , CAPPED_STATUS , MATCH_FEE , AUCTIONED_PRICE ) values ("+player_id+", "+fname+", "+mname+", "+lname+", "+dob+", "+nationality+", "+role+",0,0,0,0,0,0,0,0,0,0,0,'0-0-0-0',0,0,0,0,"+capstatus+",0,0 )")
        con.commit()
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def add_new_team():
    try:
        name = smtg(input("NAME>"))
        owner = smtg(input("OWNER_NAME>"))
        team_id = smfg(input("TEAM_ID>"))
        cur.execute("insert into TEAM(TEAM_ID,NAME, OWNER_NAME, MATCHES_WON , MATCHES_LOST , MATCHES_DRAWN , MATCHES_WITHOUT_A_RESULT) values ("+team_id+", "+name+" , "+owner+" , 0, 0, 0, 0)")
        con.commit()
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def add_new_ground():
    try:
        ground_id = smfg(input("GROUND_ID>"))
        name = smtg(input("NAME>"))
        location = smtg(input("LOCATION>"))
        capacity = smfg(input("CAPACITY>"))
        no_of_available_pitches = int(input("NO_OF_AVAILABLE_PITCHES>"))
        longest_boundary = smfg(input("LONGEST_BOUNDARY>"))
        team_id = smfg(input("TEAM_ID>"))
        cur.execute("insert into GROUND(GROUND_ID , NAME , LOCATION , CAPACITY , LONGEST_BOUNDARY , TEAM_ID ) values ("+ground_id+","+name+","+location+","+capacity+","+longest_boundary+","+team_id+")")
        for i in range(0,no_of_available_pitches):
            # print(i)
            pitch = smtg(input("Pitch type : "))
            cur.execute("insert into AVAILABLE_PITCHES(GROUND_ID ,PITCH_TYPE ) values ("+ground_id+","+pitch+")")
            con.commit()
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)
        
def buy_player():
    try:
        player_id = smfg(input("PLAYER_ID>"))
        team_id = smfg(input("TEAM_ID>"))
        price = smfg(input("AUCTIONED_PRICE>"))
        salary = smfg(input("MATCH_FEE>"))
        flag =0
        cur.execute("select PLAYER_ID from PLAYER")
        result = cur.fetchall()
        cur.execute("select TEAM_ID from TEAM")
        res = cur.fetchall()
        for r in result:
            for rr in res:
                if(r['PLAYER_ID']==int(player_id) and rr['TEAM_ID']==int(team_id)):
                    flag = 1
                    cur.execute("update PLAYER set TEAM_ID = "+team_id+", AUCTIONED_PRICE = "+price+" ,MATCH_FEE = "+salary+" where PLAYER_ID = "+player_id)
                    con.commit()
        if(flag==0):
            print("The player or team doesn't exist")
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message) 
    
def change_captian():
    try:
        player_id = smfg(input("PLAYER_ID>"))
        team_id = smfg(input("TEAM_ID>"))
        flag =0
        cur.execute("select PLAYER_ID , TEAM_ID from PLAYER")
        result = cur.fetchall()
        for r in result:
            if(r['PLAYER_ID']==int(player_id) and r['TEAM_ID']==int(team_id)):
                flag = 1
                cur.execute("update CAPTAINS set CAPTAIN_ID ="+player_id+" where TEAM_ID ="+team_id)
                con.commit()
        if(flag==0):
            print("The player does not belng to team")
                
    except Exception as e:    
        message = e.args
        print(">>>>>>>>>>>>>>>>",message)

def add_supportstaff():
    try:
        staff_id = smfg(input("STAFF_ID>"))
        Fname = smtg(input("FIRST_NAME>"))
        Mname = smtg(input("MIDDLE_NAME>"))
        Lname = smtg(input("LAST_NAME>"))
        salary = smfg(input("SALARY>"))
        role_played = smtg(input("ROLE_PLAYED>"))
        coach_type = smtg(input("COACH_TYPE>"))
        field_advising = smtg(input("FIELD_ADVISING>"))
        team_id = smfg(input("TEAM_ID>"))
        cur.execute("insert into TEAM_SUPPORT_STAFF(STAFF_ID,TEAM_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,SALARY,ROLE_PLAYED,COACH_TYPE,`FIELD ADVISING`) values ("+staff_id+","+team_id+","+Fname+","+Mname+","+Lname+","+salary+","+role_played+","+coach_type+","+field_advising+")")
        con.commit()
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def remove_supportstaff():
    try:
        staff_id = smfg(input("STAFF_ID>"))
        team_id = smfg(input("TEAM_ID>"))
        flag =0
        cur.execute("select STAFF_ID , TEAM_ID from TEAM_SUPPORT_STAFF")
        result = cur.fetchall()
        for r in result:
            if(r['STAFF_ID']== int(staff_id) and r['TEAM_ID']==int(team_id)):
                flag = 1
                cur.execute("delete from TEAM_SUPPORT_STAFF where STAFF_ID ="+staff_id+" and TEAM_ID = "+team_id)
                con.commit()
        if(flag==0):
            print("staff doesn't belong to team or either staff or team doesn't exist")
    except Exception as e:    
        code , message = e.args
        print(">>>>>>>>>>>>>>>>",code , message)

def remove_player():
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
            
    except Exception as e:
        message = e.args
        print(">>>>>>>>>>>>>>>>",message)

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
    elif(ch==9):
        change_player_stats()
        # change_player_stats(player_id,matches,innings_batting,runsscored_batting,avg_batting,highestscore_batting,strikerate_batting,innings_bowling,wickets_bowling,avg_bowling,strikerate_bowling,bestfig_bowling,innings_fielding,catches_fielding,runouts_fielding,capstatus,matchfee,autionedprice)
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
    flag = 0

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='CRICKET_TOURNAMENT',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)
        break

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
        print("14.Buy a player")
        print("15.Change the captain")
        print("16.Remove the player from the team")
        print("17.Add a support staff")
        print("18.Remove a support staff")
        print("19.Logout")
        try:
            ch = int(input("Enter Choice>"))
            tmp = sp.call('clear',shell=True)
            if ch==19:
                flag=1
                break
            else:
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")
        except:
            print("Invalid input")
