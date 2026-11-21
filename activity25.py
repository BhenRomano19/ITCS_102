
mid_range_fadeaway =  "LeBron James's midrange fadeaway evolved from a raw,\n " \
" imbalanced childhood imitation of Michael Jordan into one of the most reliable,\n" \
" unguardable signature moves of his later career—including the iconic baseline fadeaway he hit \n " \
" February 2023 to break Kareem Abdul-Jabbar's all-time NBA scoring record."

blocking = "LeBron James is famous for his signature chase-down blocks,\n" \
" ranking 66th on the NBA's all-time career blocks list with\n" \
" 1,193+ career regular-season blocks (averaging 0.7 blocks per game)."

playmaking = "LeBron James is widely regarded as the greatest playmaking forward in NBA history," \
"ranking 3rd on the NBA's all-time career assists list (surpassing Jason Kidd in November 2026)" \
" with a career average of 7.4 assists per game."

three_point_shooting = "LeBron James has evolved from  a slash-first finisher into a high-volume" \
" perimeter shooter over his career," \
" holding a 50.6 percent career field-goal percentage," \
" a 34.8 percent three-point percentage,and a 73.7 percent free-throw " \
"percentage a cross 1,634 regular-season"

lebron_james = [playmaking, three_point_shooting, blocking, mid_range_fadeaway] 
mvp = ["jermy_west", "kobe_bryant", lebron_james, "shaquile _o'_neal", "magic_jhohnson"]
los_angeles_lakers = ["allstar", mvp,  "defensive_player_of_the_year", ]
nba_teams  ={ "bulls" : "chicago_bulls", "lakers" : los_angeles_lakers, "celtics" : "boston_celtics", "warriors" : "golden_state_warriors", "heat" : "miami_heat"}

print(nba_teams["lakers"][1][2][2])