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