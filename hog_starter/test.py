        # if who == 0:           
        #     NOR = strategy0(score1, score2)                        
        #     score1 += take_turn(NOR, opponent_score, dice)            
        #     who = other(who)                    
        # else:            
        #     NOR = strategy1(score2, score1)            
        #     score2 += take_turn(NOR, opponent_score, dice)            
        #     who = other(who)  



    # def swap(strategy, p0, p1):
    #     nonlocal score, opponent_score
    #     dice = select_dice(p0, p1)
    #     p0_temp = p0 + take_turn(strategy0(p0, p1), p1, dice)
    #     print("1 outside of the while loop.")
    #     if is_swap(p0_temp, p1):
    #         score, opponent_score = p1, p0_temp
    #     else:
    #         score = p0_temp
    #     print("2 ", score, opponent_score)

    # print("starting while loop, goal=", goal)
    # while score < goal and opponent_score < goal:
    #     print("3 inside of while loop.")
    #     if who == 0:
    #         swap(strategy0, score, opponent_score)
    #     else:
    #         dice = select_dice(opponent_score, score)
    #         p1_temp = opponent_score + take_turn(strategy1(opponent_score, score), score, dice)
    #         if is_swap(p1_temp, score):
    #             opponent_score = score
    #             score = p1_temp
    #         else:
    #             score = p1_temp
    #     who = other(who)


        # elif score_with_bacon < opponent_score:
    #     return 0 
    # elif bacon >= BACON_MARGIN:
    #     return 0
    # else: 
    #     return BASELINE_NUM_ROLLS
    

    
    # if score_with_bacon == opponent_score:
    #     if score + bacon < opponent_score:
    #         return 0
    #     elif score + bacon > opponent_score:
    #         return BASELINE_NUM_ROLLS
    #     elif score + bacon == opponent_score:
    #         if bacon >= BACON_MARGIN:
    #             return 0 
    #         else:
    #             return BASELINE_NUM_ROLLS
    # return 5 # Replace this statement