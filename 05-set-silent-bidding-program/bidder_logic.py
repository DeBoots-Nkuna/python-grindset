
def determining_bid_winner(bidding_dict):
    
    #varible declarations
    highest_bidder_name = ""
    highest_bid_amount = 0
    
    #for loop
    for key , value in bidding_dict.items():
        
        #if statement 
        if value > highest_bid_amount:
            highest_bid_amount = value
            highest_bidder_name = key
    
    return highest_bidder_name, highest_bid_amount    