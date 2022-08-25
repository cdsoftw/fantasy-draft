# ========================================================================================
# Name        : draft.sh
# Author      : Cole Dapprich
# Version     : 2.0
# Date        : 8/22/2017
# Description : This bash script runs a draft by using sed commands to delete picked play-
#		        ers (input by the user) and then using head commands to print out the top
#		        five options in each category.
# Copyright   : © 2017 CDSoftworks ( AMDG )
# ========================================================================================

#!/bin/bash
PICK="start"
PICK_COUNT=1

echo "Enter \"done\" when draft is complete."
echo "To view the top 5 remaining players in a specific category, enter that category."

while [ "$PICK" != "done" ]
do
	echo -n "Enter pick #$PICK_COUNT: "
	read PICK
	
	if [ "$PICK" = "def" ]; then
		echo ""
		head -6 ./dst.csv
		echo ""
	elif [ "$PICK" = "k" ]; then
		echo ""
		head -6 ./k.csv
		echo ""
	elif [ "$PICK" = "idp" ]; then
		echo ""
		head -6 ./idp.csv
		echo ""
    elif [ "$PICK" = "qb" ]; then
		echo ""
		head -6 ./qb.csv
		echo ""
    elif [ "$PICK" = "wr" ]; then
		echo ""
		head -6 ./wr.csv
		echo ""
    elif [ "$PICK" = "rb" ]; then
		echo ""
		head -6 ./rb.csv
		echo ""
    elif [ "$PICK" = "te" ]; then
		echo ""
		head -6 ./te.csv
		echo ""
	elif [ "$PICK" = "--" ]; then
		((PICK_COUNT--))
	elif [ "$PICK" = "all" ]; then
		echo -e "\nWR:\n"
		head -6 ./wr.csv
        echo -e "\nRB:\n"
		head -6 ./rb.csv
        echo -e "\nTE:\n"
		head -6 ./te.csv
		echo -e "\nQB:\n"
		head -6 ./qb.csv
		echo -e "\nOVERALL:\n"
		head -11 ./rankings.csv
		echo ""
	
	else
		if [ "$PICK" != "done" ]; then
			sed -i "/$PICK/d" ./rankings.csv
            sed -i "/$PICK/d" ./qb.csv
            sed -i "/$PICK/d" ./wr.csv
            sed -i "/$PICK/d" ./rb.csv
            sed -i "/$PICK/d" ./te.csv
			sed -i "/$PICK/d" ./dst.csv
			sed -i "/$PICK/d" ./k.csv
			sed -i "/$PICK/d" ./idp.csv
			((PICK_COUNT++))
			echo -e "\nWR:\n"
			head -6 ./wr.csv
			echo -e "\nRB:\n"
			head -6 ./rb.csv
			echo -e "\nTE:\n"
			head -6 ./te.csv
			echo -e "\nQB:\n"
			head -6 ./qb.csv
			echo -e "\nOVERALL:\n"
			head -11 ./rankings.csv
			echo ""
		fi
	fi
done
